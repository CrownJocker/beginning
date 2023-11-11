from django.core.exceptions import ValidationError
from django.db import models
from django.contrib.auth.models import Permission
from organisation.models import Department, Filial

all_permissions = Permission.objects.all()


class Position(models.Model):
    position = models.CharField(
        verbose_name="Должность",
        max_length=255,
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name = 'Должность'
        verbose_name_plural = 'Должности'

    def __str__(self):
        return self.position


class Instruction(models.Model):
    name = models.CharField(
        verbose_name="Название инструкции",
        max_length=255,
        blank=True,
        null=True,
    )
    filial = models.ForeignKey(
        Filial,
        on_delete=models.PROTECT,
        verbose_name="Филиал",
        related_name='Instructions',
    )
    #steps = models.ForeignKey(
    #    'StepForInstruction',
    #    on_delete=models.PROTECT,
    #    verbose_name="Steps",
    #    related_name='Instructions',
    #)
    #steps = models.ManyToManyField(
    #    'StepForInstruction',
    #    verbose_name="Steps",
    #    related_name='Instructions',
    #)
    all_view = models.BooleanField(default=False, verbose_name='All_vision')

    class Meta:
        verbose_name = 'Инструкция'
        verbose_name_plural = 'Инструкции'

    def __str__(self):
        return self.name


class StepForInstruction(models.Model):
    name = models.CharField(
        verbose_name="Название шага",
        max_length=255,
        blank=True,
        null=True,
    )
    instruction = models.ForeignKey(
        Instruction,
        on_delete=models.PROTECT,
        verbose_name="Инструкция",
    )
    description = models.TextField(
        verbose_name='Описание',
        max_length=255,
        blank=True,
        null=True,
    )
    illustration = models.ImageField(
        verbose_name="Иллюстрация",
        blank=True,
    )
    caption = models.CharField(
        verbose_name='Подпись',
        max_length=255,
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name = 'Шаг'
        verbose_name_plural = 'Шаги для инструкций'

    def save(self, *args, **kwargs):
        if not self.illustration and not self.description:
            raise ValidationError("Необходимо указать либо изображение, либо описание.")
            # Проверяем, что если указано описание, то также указано изображение
        if self.description and not self.illustration:
            raise ValidationError("Необходимо указать изображение для описания")
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class PublicHoliday(models.Model):
    name = models.CharField(
        verbose_name="Название праздника",
        max_length=60,
        blank=True
    )
    holiday_date = models.DateField(
        verbose_name="Дата праздника"
    )
    descrIPAddresstion = models.TextField(
        verbose_name="Описание праздника",
        null=True,
        blank=True
    )
    updated = models.DateTimeField(
        verbose_name="Время обновления",
        auto_now=True,
        auto_now_add=False,
        blank=True
    )
    created = models.DateField(
        verbose_name="Время создания",
        auto_now=False,
        auto_now_add=True,
        blank=True
    )

    class Meta:
        verbose_name = 'Праздник'
        verbose_name_plural = 'Праздники'

    def __str__(self):
        return str(self.pk) + " " + self.name

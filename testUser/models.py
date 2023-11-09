from django.core.exceptions import ValidationError
from django.db import models
from django.contrib.auth.models import Permission
from organisation.models import Department, Filial

all_permissions = Permission.objects.all()


class Position(models.Model):
    position = models.CharField(
        verbose_name="Position",
        max_length=255,
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.position


class Instruction(models.Model):
    name = models.CharField(
        verbose_name="Instruction name",
        max_length=255,
        blank=True,
        null=True,
    )
    filial = models.ForeignKey(
        Filial,
        on_delete=models.PROTECT,
        verbose_name="Filial",
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

    def __str__(self):
        return self.name


class StepForInstruction(models.Model):
    name = models.CharField(
        verbose_name="Step name",
        max_length=255,
        blank=True,
        null=True,
    )
    instruction = models.ForeignKey(
        Instruction,
        on_delete=models.PROTECT,
        verbose_name="Instruction",
    )
    description = models.TextField(
        verbose_name='Description',
        max_length=255,
        blank=True,
        null=True,
    )
    illustration = models.ImageField(
        verbose_name="Illustration",
        blank=True,
    )
    caption = models.CharField(
        verbose_name='Caption',
        max_length=255,
        blank=True,
        null=True,
    )

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
        verbose_name="Holiday name",
        max_length=60,
        blank=True
    )
    holiday_date = models.DateField(
        verbose_name="Holiday date"
    )
    descrIPAddresstion = models.TextField(
        verbose_name="Holiday description",
        null=True,
        blank=True
    )
    updated = models.DateTimeField(
        verbose_name="Updated datetime",
        auto_now=True,
        auto_now_add=False,
        blank=True
    )
    created = models.DateField(
        verbose_name="Created datetime",
        auto_now=False,
        auto_now_add=True,
        blank=True
    )

    def __str__(self):
        return str(self.pk) + " " + self.name

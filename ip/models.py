from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from django.db import models
from organisation.models import Department, Filial


class TypeSubject(models.Model):
    name = models.CharField(
        verbose_name="Тип устройства",
        max_length=255,
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name = 'Тип устройства'
        verbose_name_plural = 'Типы устройств'

    def __str__(self):
        return self.name


class StartIP(models.Model):
    name = models.CharField(
        verbose_name="Начальный IP",
        max_length=11,
        validators=[RegexValidator(r'^\d{1,3}\.\d{1,3}\.\d{1,3}$', 'Введите значение в формате int.int.int')],
        blank=True,
        null=True,
        unique=True,
    )
    description = models.CharField(
        verbose_name="Описание",
        max_length=255,
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name = 'Начальный IP'
        verbose_name_plural = 'Начальные IP'

    def __str__(self):
        return self.name

    def clean(self):
        if StartIP.objects.filter(name=self.name).exclude(pk=self.pk).exists():
            raise ValidationError("Такой начальный ip уже существует в базе данных.")


class IPAddress(models.Model):
    type_subject = models.ForeignKey(
        TypeSubject,
        on_delete=models.PROTECT,
        verbose_name="Тип объекта",
        null=True,
        blank=True,
   )
    start_ip = models.ForeignKey(
        StartIP,
        on_delete=models.PROTECT,
        verbose_name="Начальный IP",
    )
    filial = models.ForeignKey(
        Filial,
        on_delete=models.PROTECT,
        verbose_name="Филиал",
    )
    department = models.ForeignKey(
        Department,
        on_delete=models.PROTECT,
        verbose_name="Отдел",
    )
    ip_address = models.GenericIPAddressField(
        verbose_name="IP - адрес",
        blank=True,
        null=True,
        unique=True,
    )
    inventory_number = models.IntegerField(
        verbose_name="Инвентарный номер",
        default=None,
        blank=True,
        null=True,
    )
    is_active = models.BooleanField(default=False, verbose_name="Активен")

    class Meta:
        verbose_name = 'IP - адрес'
        verbose_name_plural = 'IP - адреса'
        ordering = ["start_ip"]

    def __str__(self):
        return self.ip_address

    def clean(self):
        # Проверяем, существует ли уже такой инвентарный номер в базе данных
        if self.inventory_number != None and IPAddress.objects.filter(
                inventory_number=self.inventory_number).exclude(pk=self.pk).exists():
            raise ValidationError("Инвентарный номер уже существует в базе данных.")

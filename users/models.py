from django.db import models
from django.contrib.auth.models import AbstractUser

from testUser.models import Filial, Department, Position


class CustomUser(AbstractUser):
    is_active = models.BooleanField(default=False, verbose_name="Active")
    is_admin = models.BooleanField(default=False, verbose_name="Admin")
    position = models.ForeignKey(
        Position,
        on_delete=models.PROTECT,
        verbose_name="Position",
        null=True,
        blank=True
    )
    filial = models.ForeignKey(
        Filial,
        on_delete=models.PROTECT,
        verbose_name="Filial",
        null=True,
        blank=True
    )
    department = models.ForeignKey(
        Department,
        on_delete=models.PROTECT,
        verbose_name="Department",
        null=True,
        blank=True
    )

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

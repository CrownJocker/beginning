from django.db import models
from rest_framework.reverse import reverse_lazy


class Filial(models.Model):
    name = models.CharField(
        verbose_name="Filial name",
        max_length=255,
        unique=True,
    )
    filialCode = models.CharField(
        verbose_name="Filial code",
        max_length=24,
        blank=True,
        unique=True,
    )
    description = models.TextField(
        verbose_name="Filial description",
        null=True,
        blank=True
    )

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["name"]


class Department(models.Model):
    filial = models.ForeignKey(
        Filial,
        on_delete=models.PROTECT,
        verbose_name="Filial",
        related_name='Departments',
    )
    name = models.CharField(
        verbose_name="Department name",
        max_length=255,
        blank=True,
        unique=True,
    )
    deptCode = models.CharField(
        verbose_name="Department code",
        max_length=24,
        blank=True,
        unique=True,
    )
    description = models.TextField(
        verbose_name="Department description",
        null=True,
        blank=True
    )

    def __str__(self):
        return self.name


class SubDepartment(models.Model):
    # id/pk -> integer -> autoincrement
    department = models.ForeignKey(
        Department,
        on_delete=models.PROTECT,
        verbose_name="Department",
        related_name='SubDepartments',
    )
    name = models.CharField(
        verbose_name="SubDept_name",
        max_length=255,
        help_text="Pls add SubDepartment name",
        blank=True,
        unique=True,
    )
    subDeptCode = models.CharField(
        verbose_name="SubDepartment code",
        max_length=24,
        blank=True,
        unique=True,
    )

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse_lazy('testUser: view', kwargs={'pk': self.pk})

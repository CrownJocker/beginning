from django.db import models
from rest_framework.reverse import reverse_lazy


class Filial(models.Model):
    name = models.CharField(
        verbose_name="Название филиала",
        max_length=255,
        unique=True,
    )
    filialCode = models.CharField(
        verbose_name="Код филиала",
        max_length=24,
        blank=True,
        unique=True,
    )
    description = models.TextField(
        verbose_name="Описание филиала",
        null=True,
        blank=True
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Филиал'
        verbose_name_plural = 'Филиалы'
        ordering = ["name"]


class Department(models.Model):
    filial = models.ForeignKey(
        Filial,
        on_delete=models.PROTECT,
        verbose_name="Филиал",
        related_name='Departments',
    )
    name = models.CharField(
        verbose_name="Название отдела",
        max_length=255,
        blank=True,
        unique=True,
    )
    deptCode = models.CharField(
        verbose_name="Код отдела",
        max_length=24,
        blank=True,
        unique=True,
    )
    description = models.TextField(
        verbose_name="Описание отдела",
        null=True,
        blank=True
    )

    class Meta:
        verbose_name = 'Отдел'
        verbose_name_plural = 'Отделы'

    def __str__(self):
        return self.name


class SubDepartment(models.Model):
    department = models.ForeignKey(
        Department,
        on_delete=models.PROTECT,
        verbose_name="Отдел",
        related_name='SubDepartments',
    )
    name = models.CharField(
        verbose_name="Название подотдела",
        max_length=255,
        help_text="Добавьте название подотдела",
        blank=True,
        unique=True,
    )
    subDeptCode = models.CharField(
        verbose_name="Код подотдела",
        max_length=24,
        blank=True,
        unique=True,
    )

    class Meta:
        verbose_name = 'Подотдел'
        verbose_name_plural = 'Подотделы'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse_lazy('testUser: view', kwargs={'pk': self.pk})


class Group(models.Model):
    subDept = models.ForeignKey(
        SubDepartment,
        on_delete=models.PROTECT,
        verbose_name="Подотдел",
        related_name='group',
    )
    name = models.CharField(
        verbose_name="Название группы",
        max_length=255,
        help_text="Добавьте название группы",
        blank=True,
        unique=True,
    )
    groupCode = models.CharField(
        verbose_name="Код группы",
        max_length=24,
        blank=True,
        unique=True,
    )

    class Meta:
        verbose_name = 'Группа'
        verbose_name_plural = 'Группы'

    def __str__(self):
        return self.name

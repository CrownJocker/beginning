from datetime import timedelta, datetime
from django.db import models
from organisation.models import Department
from testUser.models import Position

PERIOD_CHOICES = [(int(i*365/2), int(i*365/2)) for i in range(1, 7)]


class ImportData(models.Model):
    csv_file = models.FileField(upload_to='uploads/')
    date_added = models.DateTimeField(auto_now_add=True)


class EventsForUser(models.Model):
    user = models.ForeignKey(
        "UserForDate",
        on_delete=models.PROTECT,
        verbose_name="Пользователь",
        null=True,
        blank=True,
    )
    medicalExamination = models.ForeignKey(
        "MedicalExamination",
        on_delete=models.SET_NULL,
        verbose_name="Следующий медосмотр",
        null=True,
        blank=True,
    )
    knowledgeTest = models.ForeignKey(
        "KnowledgeTest",
        on_delete=models.PROTECT,
        verbose_name="Следующая проверка знаний",
        null=True,
        blank=True,
    )

    class Meta:
        verbose_name = 'Медосмотры и Аттестация'


class UserForDate(models.Model):
    full_name = models.CharField(
        verbose_name="ФИО",
        max_length=256,
    )
    dept = models.ForeignKey(
        Department,
        on_delete=models.PROTECT,
        verbose_name="Отдел",
        related_name="users",
    )
    position = models.ForeignKey(
        Position,
        on_delete=models.PROTECT,
        verbose_name="Должность",
    )

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = 'Что-то'
        verbose_name_plural = 'Такое'


class Period(models.Model):
    name = models.CharField(
        verbose_name="Название периода",
        max_length=256,
        blank=True,
        null=True,
    )
    period = models.IntegerField(
        verbose_name="Периодичность",
        blank=True,
        null=True,
        choices=PERIOD_CHOICES,
    )

    def __str__(self):
        #return self.name
        return f"{self.name}"

    class Meta:
        verbose_name = 'Периодичность'
        verbose_name_plural = 'Периодичности'


class MedicalExamination(models.Model):
    period = models.ForeignKey(
        Period,
        on_delete=models.PROTECT,
        verbose_name="Периодичность",
        null=True,
        blank=True,
    )
    dateOfMedicalExamination = models.DateField(
        verbose_name="Дата прохождения медосмотра",
        blank=True,
        null=True,
    )

    dateOfNextMedicalExamination = models.DateField(
        verbose_name="Дата прохождения следующего медосмотра",
        blank=True,
        null=True,
    )

    def save(self, *args, **kwargs):
        if self.dateOfMedicalExamination and self.period.period is not None:
            if type(self.dateOfMedicalExamination) == str and self.period.period is not None:
                date_obj = datetime.strptime(self.dateOfMedicalExamination, '%Y-%m-%d')
                next_date_obj = date_obj + timedelta(days=self.period.period)
                self.dateOfNextMedicalExamination = next_date_obj.strftime('%Y-%m-%d')
            elif self.period is None:
                self.dateOfNextMedicalExamination = self.dateOfNextMedicalExamination
            else:
                self.dateOfNextMedicalExamination = self.dateOfMedicalExamination + timedelta(days=self.period.period)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.dateOfNextMedicalExamination}"

    class Meta:
        verbose_name = 'Медосмотр'
        verbose_name_plural = 'Медосмотры'


class KnowledgeTest(models.Model):
    period = models.ForeignKey(
        Period,
        on_delete=models.PROTECT,
        verbose_name="Периодичность",
        null=True,
        blank=True,
    )
    dateOfKnowledgeTest = models.DateField(
        verbose_name="Дата прохождения проверки знаний",
        blank=True,
        null=True,
    )
    dateOfNextKnowledgeTest = models.DateField(
        verbose_name="Дата прохождения следующей проверки знаний",
        blank=True,
        null=True,
    )

    def save(self, *args, **kwargs):
        if self.dateOfKnowledgeTest and self.period and self.period.period:
            self.dateOfNextKnowledgeTest = self.dateOfKnowledgeTest + timedelta(days=self.period.period)
        super().save(*args, **kwargs)

    def __str__(self):
        #return self.dateOfNextKnowledgeTest.strftime("%Y-%m-%d")
        return f"{self.dateOfNextKnowledgeTest}"

    class Meta:
        verbose_name = 'Проверка знаний'
        verbose_name_plural = 'Проверки знаний'

import re
from datetime import datetime

from django.forms import DateInput
from import_export.widgets import ForeignKeyWidget


class CustomDateWidget(ForeignKeyWidget):
    def clean(self, value, row=None, *args, **kwargs):
        if value:
            date_str = re.findall(r'\d{2}.\d{2}.\d{4}', value)
            if date_str:
                extracted_date = date_str[0]
                formatted_date = extracted_date[6:] + '-' + extracted_date[3:5] + '-' + extracted_date[0:2]
                return formatted_date
        return None


class CustomDateForeignKeyWidget(DateInput):
    def __init__(self, rel_model, rel_field_name, attrs=None):
        self.rel_model = rel_model
        self.rel_field_name = rel_field_name
        super().__init__(attrs=attrs)

    def clean(self, value, row=None, **kwargs):
        # Добавьте здесь свою логику очистки значения
        # Убедитесь, что возвращается очищенное значение
        if value is not None:
            print(value)
            date_str = re.findall(r'\d{2}.\d{2}.\d{4}', str(value))
            if date_str:
                date_obj = datetime.strptime(date_str[0], '%d.%m.%Y').date()
                formatted_date = date_obj.strftime('%Y-%m-%d')
                value = formatted_date
                print(value)
        return value
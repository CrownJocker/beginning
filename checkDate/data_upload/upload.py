import pandas as pd
from checkDate.models import EventsForUser, UserForDate

def load_data_from_excel(file_path):
    # Чтение данных из файла Excel
    df = pd.read_excel(file_path)

    # Загрузка данных в модель UserForDate
    for _, row in df.iterrows():
        user_data = {
            'full_name': row['Ф.И.О.'],
            'dept_id': row['Отдел'],
            'position_id': row['Должность']
        }
        user = UserForDate.objects.create(**user_data)

        # Загрузка данных в модель EventsForUser
        #event_data = {
        #    'user_id': user.id,
        #    'medicalExamination_id': row['Медосмотр'],
        #    'knowledgeTest_id': row['Проверка знаний']
        #}
        #event = EventsForUser.objects.create(**event_data)
load_data_from_excel("проверка знаний.xlsx")
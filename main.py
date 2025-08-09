from pprint import pprint
# читаем адресную книгу в формате CSV в список contacts_list
import csv
import re

with open('phonebook_raw.csv', encoding='utf-8') as f:
  rows = csv.reader(f, delimiter=',')
  contacts_list = list(rows)
pprint(contacts_list)

# TODO 1: выполните пункты 1-3 ДЗ
# ФИО
def process_fio(contacts):
    result = []
    
    for contact in contacts:
        fio = ' '.join(contact[:3]).strip().split()
        new_contact = [''] * 7
        if len(fio) >= 1:
            new_contact[0] = fio[0]  
        if len(fio) >= 2:
            new_contact[1] = fio[1]
        if len(fio) >= 3:
            new_contact[2] = fio[2]
        new_contact[3:] = contact[3:]
        result.append(new_contact)
    return result

# Номер
def format_phone(phone):
    if not phone:
        return phone

    pattern = r'\+?7?8?[\s-]*\(?(\d{3})\)?[\s-]*(\d{3})[\s-]*(\d{2})[\s-]*(\d{2})(?:\s*доб\.?\s*(\d+))?'
    match = re.match(pattern, phone.replace(' ', ''))
    
    if match:
        groups = match.groups()
        phone_number = f'+7({groups[0]}){groups[1]}-{groups[2]}-{groups[3]}'
        if groups[4]:
            phone_number += f'доб.{groups[4]}'
        return phone_number
    return phone






# TODO 2: сохраните получившиеся данные в другой файл
# код для записи файла в формате CSV
with open("phonebook.csv", "w", encoding="utf-8") as f:
  datawriter = csv.writer(f, delimiter=',')
  # Вместо contacts_list подставьте свой список
  datawriter.writerows(contacts_list) 
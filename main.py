import re
from pprint import pprint
import csv

# Читаем CSV
with open('phonebook_raw.csv', encoding='utf-8') as f:
    rows = csv.reader(f, delimiter=',')
    contacts_list = list(rows)

#ФИО
def process_name(contact):
    full_name = ' '.join(contact[:3]).strip().split()
    contact[0] = full_name[0] if len(full_name) > 0 else ''
    contact[1] = full_name[1] if len(full_name) > 1 else ''
    contact[2] = full_name[2] if len(full_name) > 2 else ''
    return contact

# Номера
def format_phone(phone):
    if not phone:
        return ''
    pattern = r'(\+7|8)?[\s-]*\(?(\d{3})\)?[\s-]*(\d{3})[\s-]*(\d{2})[\s-]*(\d{2})(?:\s*доб\.?\s*(\d+))?'
    match = re.match(pattern, phone)
    if match:
        groups = match.groups()
        phone_number = f'+7({groups[1]}){groups[2]}-{groups[3]}-{groups[4]}'
        if groups[5]:
            phone_number += f' доб.{groups[5]}'
        return phone_number
    return phone 

# Дубли
def merge_contacts(contacts):
    grouped_contacts = {}
    
    for contact in contacts[1:]:
        contact = process_name(contact)
        key = (contact[0], contact[1])
        
        if key not in grouped_contacts:
            contact[5] = format_phone(contact[5])
            grouped_contacts[key] = contact
        else:
            existing = grouped_contacts[key]
            for i in range(len(contact)):
                if contact[i] and not existing[i]:
                    existing[i] = contact[i]
            existing[5] = format_phone(existing[5])
    
    result = [contacts[0]] + list(grouped_contacts.values())
    return result

result_contacts = merge_contacts(contacts_list)
pprint(result_contacts)

from pprint import pprint
# читаем адресную книгу в формате CSV в список contacts_list
import csv
import re
with open("phonebook_raw.csv", encoding="utf-8") as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)
# pprint(contacts_list)

# TODO 1: выполните пункты 1-3 ДЗ
# ваш код
pattern = r'(\d)|(доб\D*\d*)'
for contacts in contacts_list:
    for index, contact in enumerate(' '.join(contacts[:2]).split()):
        contacts[index] = contact
    phone_list = re.findall(pattern, contacts[5], re.IGNORECASE)
    # pprint(phone_list)
    if phone_list:
        contacts[5] = ''.join(x[0] for x in phone_list[1:12])
        contacts[5] = f"+7({contacts[5][:3]}){
            contacts[5][3:6]}-{contacts[5][6:8]}-{contacts[5][8:10]}"
        if len(phone_list) == 12:
            contacts[5] += ' доб.' + \
                re.search(r'\d+', phone_list[11][1]).group()
# pprint(contacts_list)
new_contacts_list = []
fios = [' '.join(x[:3]) for x in contacts_list]
# pprint(fios)

dublicate = []
for index, fio in enumerate(fios):
    if fios.count(fio) == 1 and index not in dublicate:
        new_contacts_list.append(contacts_list[index])
    elif index not in dublicate:
        dublicate.append(index)
        duplicate_list = [contacts_list[index]]
        for index2, fio2 in enumerate(fios[index+1:]):
            if fio2 == fio:
                dublicate.append(index2+index+1)
                duplicate_list.append(contacts_list[index2+index+1])
        new_contacts_list.append(
            [' '.join([y for y in set(x) if y]) for x in list(zip(*duplicate_list))])
pprint(new_contacts_list)

# TODO 2: сохраните получившиеся данные в другой файл
# код для записи файла в формате CSV
with open("phonebook.csv", "w", encoding="utf-8", newline='') as f:
    datawriter = csv.writer(f, delimiter=',')
    # Вместо contacts_list подставьте свой список
    datawriter.writerows(new_contacts_list)

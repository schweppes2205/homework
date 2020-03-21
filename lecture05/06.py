"""
6. Необходимо создать (не программно) текстовый файл, где каждая
строка описывает учебный предмет и наличие лекционных, практических
и лабораторных занятий по этому предмету и их количество. Важно,
чтобы для каждого предмета не обязательно были все типы занятий.
Сформировать словарь, содержащий название предмета и общее количество
занятий по нему. Вывести словарь на экран.
Примеры строк файла:
Информатика: 100(л) 50(пр) 20(лаб).
Физика: 30(л) — 10(лаб)
Физкультура: — 30(пр) —

Пример словаря:
{“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
"""

raw_data = []
subject_data = {}
with open("06_task_text", encoding="utf-8") as file_descriptor:
    for line in file_descriptor:
        raw_data.append(line.split())
# print(raw_data)
for subject in raw_data:
    subject_data[subject[0]] = sum([int(x.split('(')[0]) for x in subject[1:] if x != "—"])
print(subject_data)
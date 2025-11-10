'''3. Сформировать (не программно) текстовый файл. В нём каждая
строка должна описывать учебный предмет и наличие лекционных,
практических и лабораторных занятий по предмету. Сюда должно входить и
количество занятий. Необязательно, чтобы для каждого предмета были все
типы занятий.
Сформировать словарь, содержащий название предмета и общее
количество занятий по нему. Вывести его на экран.
Примеры строк файла: Информатика: 100(л) 50(пр) 20(лаб).
Физика: 30(л) 10(лаб)
Физкультура: 30(пр)
Пример словаря: {“Информатика”: 170, “Физика”: 40, “Физкультура”:
30}'''

import sys
import importlib
sys.path.append('subjects/script-languages')

import functions as f
from functions import print_full_width_line as line
f = importlib.reload(f)

import re


def main():

    file_s = open('subjects/script-languages/lr-3-12/task-3/subjects.txt', 'r', encoding="utf-8")

    line()
    f.print_task_start(3)
    line()
    subjects = []

    #print(list(file_s.readlines()))
    for subject in file_s:
        colon_pos = subject.find(":")
        
        if colon_pos == -1:
            print(f"памылка! радок не ў правільным фармаце")
            continue   
        
        total_hours = sum(list(map(int, re.findall(r'\d+', subject[colon_pos:]))))
        subjects.append([subject[:colon_pos], total_hours])
        
    my_dict = dict(subjects)
    print("Слоўнік:", my_dict)
    line()
    f.print_task_finished(3)
    (line)

    file_s.close


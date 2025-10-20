'''1. Создать программный файл F1 в текстовом формате, записать в него
построчно данные, вводимые пользователем. Об окончании ввода данных
будет свидетельствовать пустая строка. Скопировать в файл F2 только строки
из F1, которые не содержат цифр. Посчитать количество слов в последней
строке файла F2. – 3 балла'''
import os
import sys

from functions import get_words

if not os.path.exists("task-1"):
    os.makedirs("task-1")

f1 = open("subjects/script-languages/lr-3-12/task-1/f1.txt", "w+", encoding="utf-8")
f2 = open("subjects/script-languages/lr-3-12/task-1/f2.txt", "w+", encoding="utf-8")

i = 1
to_continue = True
while to_continue:
    user_in = input(f"Увядзіце радок {i} (пусты радок - выхад): ")
    if user_in != "":
        f1.write(user_in + "\n")
    else:
        to_continue = False
        print("Увод радкоў закончаны.")
    i += 1

f1.seek(0)

i = 1
for line in f1:
    noDigits = True
    for char in line:
        if char.isdigit():
            noDigits = False
    if noDigits:
        f2.write(line) # + '\n' не патрэбны, бо line ужо заканчваецца новым радком
        print(f"Радок {i} запісаны ў f2")
    i += 1

f2.seek(0)
print(f"Даўжыня апошняга радка ў файле f2: {len(get_words(f2.readlines()[-1]))} слоў/слова")

f1.close()
f2.close()

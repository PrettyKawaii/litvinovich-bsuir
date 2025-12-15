'''1. Создать программный файл F1 в текстовом формате, записать в него
построчно данные, вводимые пользователем. Об окончании ввода данных
будет свидетельствовать пустая строка. Скопировать в файл F2 только строки
из F1, которые не содержат цифр. Посчитать количество слов в последней
строке файла F2. – 3 балла'''
import os
import sys

def main():
    # Получаем путь к директории, где находится task1.py
    task_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Создаем пути к файлам в той же директории
    f1_path = os.path.join(task_dir, "f1.txt")
    f2_path = os.path.join(task_dir, "f2.txt")

    # Открываем файлы
    f1 = open(f1_path, "w+", encoding="utf-8")
    f2 = open(f2_path, "w+", encoding="utf-8")

    # Импортируем get_words из functions
    # Получаем путь к директории functions.py (на 2 уровня выше task_dir)
    script_lang_dir = os.path.dirname(os.path.dirname(task_dir))
    sys.path.insert(0, script_lang_dir)
    
    from functions import get_words

    print("Задача 1.")

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
    
    # Читаем все строки и проверяем, есть ли они
    f2_lines = f2.readlines()
    if f2_lines:
        print(f"Даўжыня апошняга радка ў файле f2: {len(get_words(f2_lines[-1]))} слоў/слова")
    else:
        print("Файл f2 пусты")
    
    print("Канец задачы 1")
    print(f"Файлы созданы в: {task_dir}")

    f1.close()
    f2.close()
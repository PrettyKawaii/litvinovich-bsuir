import sys
import importlib
import os

# Получаем абсолютный путь к текущему файлу (menu.py)
current_dir = os.path.dirname(os.path.abspath(__file__))
# Получаем путь к директории script-languages (на уровень выше)
script_lang_dir = os.path.dirname(current_dir)

# Добавляем путь к functions.py
sys.path.insert(0, script_lang_dir)

import functions as f
from functions import print_full_width_line as line
f = importlib.reload(f)

# Добавляем пути к задачам (они находятся в подпапках текущей директории)
sys.path.append(os.path.join(current_dir, 'task-1'))
sys.path.append(os.path.join(current_dir, 'task-2'))
sys.path.append(os.path.join(current_dir, 'task-3'))
sys.path.append(os.path.join(current_dir, 'task-4'))

import task1 as t1
import task2 as t2
import task3 as t3
import task4 as t4

line()
f.print_lr_start(3)
line()

def menu():
    print('''ЛР№ 3
1 - задача 1
2 - задача 2
3 - задача 3
4 - задача 4          
0 - выхад                                    
''')

keep_going = True

while keep_going:
    menu()
    choice = int(input("> "))
    if choice == 1:
        t1.main()        
        pass
    elif choice == 2:
        t2.main()
    elif choice == 3:
        t3.main()
    elif choice == 4:
        t4.main()
    elif choice == 0:
        keep_going = False
        f.print_lr_end(3)
    else:
        f.print_unkown_choice()
import os
import shutil

def print_full_width_line():
    """
    Prints a line of the specified character spanning the full width of the terminal.
    """
    columns, _ = shutil.get_terminal_size()
    print("-" * columns)

def clear_terminal():
    os.system('cls')

def print_unkown_choice():
    print("Невядомы выбар. Паўтарыце спробу.")

def print_task_start(n):
    print("Задача", n)
    
def print_task_finished(n):
    print(f"Задача нумар {n} завершана!")

def print_task_end(n):
    print(f"Задача нумар {n} завершана!")

def get_words(line):
    punct_table = str.maketrans({char: " " for char in ['.', ',', '?', '!']})
    words = line.translate(punct_table).split()
    return words

def test():
    print("functions.py are working! :)")

def press_key():
    input("Націсніце любую клавішу, каб працягнуць...")

def print_lr_start(n):
    print(f"Літвіновіч Аляксандр, 477901. Лабараторная работа №{n}")

def print_lr_end(n):
    print(f"ЛР №{n} завершана.")
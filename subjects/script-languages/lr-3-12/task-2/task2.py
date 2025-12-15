'''2. Имеется текстовый файл «Клиент банка», строка которого содержит
в себе информацию: фамилия клиента, сумма на счете, дата последнего
изменения.
Вывести на экран все фамилии, сумма на счету которых 0. Вывести на
экран общую сумму вложений всех клиентов банка. Файл заполнить заранее
(не программно).
Пример файла:
Иванов 120 12.09.2022
Петров 0 15.08.2022– 3 балла'''


import sys
import importlib
sys.path.append('subjects/script-languages')

import functions as f
from functions import print_full_width_line as line
f = importlib.reload(f)

def main():
    line()
    f.print_task_start(2)
    line()

    file_clients = open("subjects/script-languages/lr-3-12/task-2/bank_clients.txt", "r", encoding="utf-8")
    list_clients = []

    print("Дадаем кліентаў: ")
    for client in file_clients:
        new_client = list(client.split())
        new_client[1] = int(new_client[1])
        list_clients.append(new_client)
        print(new_client)

    line()

    total_sum = 0
    file_clients.seek(0)
    print("Прозвішчы кліентаў, сума на рахунку якіх роўна 0: ")
    for client in list_clients:
        if client[1] == 0:
            print(client[0])
        else:
            total_sum += client[1]

    line()

    print(f"Сумма ўсіх рахункаў: {total_sum} рублёў")

    line()

    f.print_task_finished(2)

    line()
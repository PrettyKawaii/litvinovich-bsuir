'''4. Создать вручную и заполнить несколькими строками текстовый
файл, в котором каждая строка будет содержать данные о фирме: название,
форма собственности, выручка, издержки.
Пример строки файла: firm_1 ООО 10000 5000.

Необходимо построчно прочитать файл, вычислить прибыль каждой
компании, а также среднюю прибыль. Если фирма получила убытки, в расчёт
средней прибыли её не включать.

Далее реализовать список. Он должен содержать словарь с фирмами и
их прибылями, а также словарь со средней прибылью. Если фирма получила
убытки, также добавить её в словарь (со значением убытков).

Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000},
{“average_profit”: 2000}].
Итоговый список сохранить в виде json-объекта в соответствующий
файл.
Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit":
2000}]
Подсказка: использовать менеджер контекста. – 1 балл (задача на
оценку 10)'''

# import sys
# import importlib
# sys.path.append('subjects/script-languages')

# import functions as f
# from functions import print_full_width_line as line
# f = importlib.reload(f)

# import json

# with open("subjects/script-languages/lr-3-12/task-4/info.json", 'w', encoding="utf-8") as json_file, open('subjects/script-languages/lr-3-12/task-4/firms.txt', 'r', encoding="utf-8") as firms_file:
#     print(list(firms_file.readlines()))
#     json_file.write(" ".join(firms_file.readlines()))


import json


def main():
    with open('firms.txt', 'w', encoding='utf-8') as f:
        
        f.write("firm_1 ООО 10000 5000\nfirm_2 ЗАО 8000 9000\nfirm_3 ИП 15000 7000\n")


    firms_profit = {}
    profits = []

    with open('firms.txt', 'r', encoding='utf-8') as file:
        for line in file:
            name, _, revenue, costs = line.strip().split()
            profit = int(revenue) - int(costs)
            firms_profit[name] = profit
            if profit > 0:
                profits.append(profit)


    result = [
        firms_profit,
        {"average_profit": sum(profits) / len(profits) if profits else 0}
    ]

    with open('firms_info.json', 'w', encoding='utf-8') as f:
        json.dump(result, f, ensure_ascii=False, indent=2)

    print("Рэзультат захаваны ў файл firms_info.json")





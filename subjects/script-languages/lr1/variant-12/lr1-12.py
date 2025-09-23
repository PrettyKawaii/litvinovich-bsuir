import math as m
import os
import shutil

def print_full_width_line(character):
    """
    Prints a line of the specified character spanning the full width of the terminal.
    """
    columns, _ = shutil.get_terminal_size()
    print(character * columns)

def clear_terminal():
    os.system('cls')

def print_unkown_choice():
    print("Неизвестный выбор. Повторите попытку.")

def print_task_finished(n):
    print(f"Задача №{n} завершена.")
''' 
1. Сделайте так, чтобы число секунд отображалось в
виде дни:часы:минуты:секунды. Ввод закончить, когда пользователь
ввел 0. '''
def refine_seconds ():
    isFinished = False
    seconds = -1

    while not isFinished:
        try:
            if seconds == 0:
                isFinished = True
                print_task_finished(1)
            else:
                seconds = int(input("Введите целое количество секунд (0 - выход): "))

                days = seconds // (24*3600)
                seconds_left = seconds % (24*3600) 

                hours = seconds_left // 3600
                seconds_left %= 3600

                minutes = seconds_left // 60
                seconds_left %= 60
                result = "Результат - " + f"{days:02d}:{hours:02d}:{minutes:02d}:{seconds_left:02d}"
                print(result)
        except (ValueError):
            print("Ошибка ввода! Потворите попытку.")

'''
2. На вход программе подается строка текста. Напишите программу,
которая переводит каждый ее символ в соответствующий ему код из
таблицы символов Unicode. Вывести на экран самое длинное слово.'''
def translate_to_unicode(line):
    return "-".join(str(ord(i)) for i in line)

def longest_word(line):
    punct_table = str.maketrans({char: " " for char in ['.', ',', '?', '!']})
    words = line.translate(punct_table).split()
    return max(words, key = len)
'''
3. На вход программе подается натуральное число n, а
затем n целых чисел. Напишите программу, которая создает из
указанных чисел список их кубов. Найти сумму и произведение
элементов списка. Вывести список в обратном порядке'''    
def task_three(n):
    numbers = [int(input(f"Введите число {i+1}: ")) for i in range(n)]
    cubes = [i**3 for i in numbers]
    sums = sum(numbers)
    product = 1
    for i in numbers:
        product *= i
    print("-------------\nИсходный список:", numbers)
    print("Обратный список:", numbers[::-1])
    print("Список кубов:", cubes)
    print(f"Сумма элементов: {sums}, произведение элементов:", product)
    print_task_finished(3)

'''
4. Найдите три ключа с самыми высокими значениями в
словаре my_dict = {'a':500, 'b':5874, 'c': 560,'d':400, 'e':5874, 'f': 20}
'''
def task_four():
    my_dict = {'a':500, 'b':5874, 'c': 560,'d':400, 'e':5874, 'f': 20}
    print("Словарь:", my_dict)
    stuff = sorted(list(my_dict.items()), key=lambda x: x[1], reverse=True)
    max_keys = [stuff[i][0] for i in range(3)]
    print("Три ключа с самыми высокими значениями: ", end='')
    print(*max_keys, sep=', ')
    
   
'''
5. Реализуйте программу «Ювелирный магазин», которая будет
включать в себя шесть пунктов меню. У вас есть словарь, где ключ –
название изделия. Значение – список, который содержит состав
изделия(золото, серебро,и т.п.), цену и кол-во (шт),которое есть в
магазине.
1. Просмотр описания: название – описание
2. Просмотр цены: название – цена.
3. Просмотр количества: название – количество.
4. Всю информацию.
5. Покупка
В пункте «Покупка» необходимо совершить покупку, с клавиатуры
вводите название изделия и его кол-во, n – выход из программы.
Посчитать цену выбранных товаров и сколько товаров осталось в
изначальном списке. На выходе должен быть чек из магазина.
6. До свидания – 2 балла'''

def store_menu():

    print(
"""1. Просмотр описания
2. Просмотр цены
3. Просмотр количества
4. Всю информацию.
5. Покупка
6. Выход""")
    return int(input("> "))
def task_five():
    to_exit = False
    content = "Состав"
    jew_items = {"Кольцо Prestige": ["Минималистичный дизайн подчеркивает 18 карат золота", "Золото 750 пробы", 600, 30], 
                 "Ожерелье Elegant": ["Семь бриллиантов в сочетании с серебром создают строгий стиль", "Серебро 925 пробы, 2.1 карат бриллианта", 1800, 3], 
                 "Серьги Classic": ["Красота кроется в простоте", "Серебро 830 пробы", 300, 40]}
    keys = list(jew_items.keys())
    values = list(jew_items.values())
    while not to_exit:
        ch = store_menu()
        clear_terminal()
        match ch:
            case 1:
                print("Описание товаров")
                print_full_width_line('-')
                for key in jew_items.keys():
                    print(f"{key:<20}: {jew_items[key][0]}\n{content:<20}: {jew_items[key][1]}\n")
            case 2:
                print("Стоимость товаров")
                print_full_width_line("-")
                for key in jew_items.keys():
                    print(f"{key:<20}:  ${jew_items[key][2]}\n")
            case 3:
                print("Количество товаров")
                print_full_width_line("-")
                for key in jew_items.keys():
                    print(f"{key:<20}:  {"Нет в наличии" if jew_items[key][3] == 0 else jew_items[key][3]}\n")
            case 4:
                print("Вся информация о товарах")
                print_full_width_line("-")
                for key in jew_items.keys():
                    print(f"{key:<20}: ", end='')
                    print(*list(jew_items[key]), sep=', ', end='\n\n')
            case 5:
                print("Что Вы хотите купить? (0 - назад)")
                i = 1
                for key in jew_items.keys():
                    print(f"{i} - {key:<20} - ${jew_items[key][2]}", end=' ')
                    print("(Нет в наличии)" if jew_items[key][3] == 0 else f"(осталось {jew_items[key][3]})")
                    i += 1
                to_buy = int(input("> "))                    
                if (to_buy < 0 or to_buy > len(list(jew_items.keys()))):
                    print_unkown_choice()
                elif to_buy == 0:
                    print("Назад.")
                elif (jew_items[list(jew_items.keys())[to_buy-1]][3] == 0):
                    print("Данного товара нет в наличии. Выберите другой товар.")

                else:
                    item = list(jew_items.keys())[to_buy-1]
                    price = jew_items[item][2]
                    total_qty = jew_items[item][3]
                    
                    
                    is_correct = False
                    while not is_correct:
                        qty = int(input("Введите количество: "))
                        if (qty < 1):
                            print("Количество не может быть меньше единицы. Повторите попытку")
                        elif (qty > total_qty):
                            print(f"В наличии только {total_qty}! Повторите попытку.")
                                                    
                        else:
                            jew_items[item][3] -= qty
                            is_correct = True


                    print(f"{item}: ${price} * {qty} = ${price*qty} (осталось: {total_qty - qty})")
                    
                    not_conf = True
                    while not_conf:
                        print("Вы уверены, что хотите совершить покупку? (Y/n)")
                        c = input("> ")
                        if (c == "Y" or c == "y"):
                            clear_terminal()
                            print("Покупка совершена успешно.")
                            print("Чек оплаты")
                            print("--------------------------")
                            print(f"{item}: ${price} * {qty}")
                            print(f"Оплачено: ${price*qty}")
                            print("--------------------------")
                            print("Спасибо за покупку!")


                            not_conf = False
                        elif (c == "N" or c == "n"):
                            clear_terminal()
                            print("Покупка отменена.")
                            not_conf = False
                        else:
                            print_unkown_choice()


            case 6:
                print("До свидания!")
                to_exit = True
            case _:
                print_unkown_choice()
        

'''6. Вы принимаете от пользователя последовательность чисел,
разделённых запятой. Составьте список и кортеж с этими числами. – 1
балл'''
def task_six():
    print("Введите последовательность чисел в формате a, b, c, ...")
    my_list = input("> ").split(", ")
    my_tuple = tuple(my_list)
    print("Список:", my_list)
    print("Кортеж:", my_tuple)

keep_going = True
print("СЯП: ЛР-1, Литвинович Александр, 477901")
print("Вариант 12.")
while keep_going:
    print("Выберите номер задания (1-6, 0 - выход)")
    choice = int(input("> "))
    clear_terminal()
    if choice == 1:
        refine_seconds()
    elif choice == 2:
        string = input("Введите строку: ")
        print("Строка в Юникоде:", translate_to_unicode(string))
        print("Самое длинное слово:", longest_word(string))
        print_task_finished(2)
    elif choice == 3:
        task_three(int(input("Введите количество натуральных чисел: ")))
    elif choice == 4:
        task_four()
        print_task_finished(4)
    elif choice == 5:
        task_five()
        print_task_finished(5)
    elif choice == 6:
        task_six()
        print_task_finished(6)
    elif choice == 0:
        print("Программа завершена.")
        keep_going = False        
    else:
        print_unkown_choice()
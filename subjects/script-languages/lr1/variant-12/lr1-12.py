import math as m
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
словаре my_dict = {'a':500, 'b':5874, 'c': 560,'d':400, 'e':5874, 'f': 20} – 2
балла
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


keep_going = True
print("СЯП: ЛР-1, Литвинович Александр, 477901")
print("Вариант 12.")
while keep_going:
    print("Выберите номер задания (1-6, 0 - выход)")
    choice = int(input("> "))
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
        print_task_finished(4)
    elif choice == 5:
        print_task_finished(5)
    elif choice == 6:
        print_task_finished(6)
    elif choice == 0:
        print("Программа завершена.")
        keep_going = False        
    else:
        print("Неизвестный выбор. Повторите попытку.")
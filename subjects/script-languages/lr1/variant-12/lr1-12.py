import math as m
def refine_seconds ():
    ''' 
    1) Сделайте так, чтобы число секунд отображалось в
    виде дни:часы:минуты:секунды. Ввод закончить, когда пользователь
    ввел 0. – 2 балла
    '''
    isFinished = False
    while not isFinished:
        try:
            if seconds == 0:
                isFinished = True
                print("Задача №1 завершена.")
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
таблицы символов Unicode. Вывести на экран самое длинное слово. – 1
балл'''
def translate_to_unicode(line):
    return "-".join(str(ord(i)) for i in line)

def longest_word(line):
    punct_table = str.maketrans({char: " " for char in ['.', ',', '?', '!']})
    words = line.translate(punct_table).split()
    return max(words, key = len)
    




keep_going = True
print("СЯП: ЛР-1, Литвинович Александр, 477901")
print("Вариант 12.")
while keep_going:
    choice = int(input("Выберите номер задания (1-6, 0 - выход): "))
    if choice == 1:
        refine_seconds()
    elif choice == 2:
        string = input("Введите строку: ")
        print("Строка в Юникоде:", translate_to_unicode(string))
        print("Самое длинное слово:", longest_word(string))
    elif choice == 3:
        fdf
    elif choice == 4:
        fdf
    elif choice == 5:
        fdf
    elif choice == 6:
        fdf
    elif choice == 0:
        print("Программа завершена.")
        keep_going = False        
    else:
        print("Неизвестный выбор. Повторите попытку.")
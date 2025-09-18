import math as m

''' 
1) Сделайте так, чтобы число секунд отображалось в
виде дни:часы:минуты:секунды. Ввод закончить, когда пользователь
ввел 0. – 2 балла
'''
isFinished = False
while not isFinished:
    try:
        seconds = int(input("Введите целое количество секунд (0 - выход): "))
        if seconds == 0:
            isFinished = True
            print("Программа завершена.")
        else:
            days = seconds // (24*3600)
            seconds_left = seconds % (24*3600) 

            hours = seconds_left // 3600
            seconds_left %= 3600

            minutes = seconds_left // 60
            seconds_left %= 60
            print("Результат - ", end='')
            #print(days, hours, minutes, seconds_left, sep=':')
            print(f"{days:02d}:{hours:02d}:{minutes:02d}:{seconds_left:02d}")

    except (ValueError):
        print("Ошибка ввода! Потворите попытку.")


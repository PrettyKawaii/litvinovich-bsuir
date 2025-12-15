# ========== ЗАДАНИЕ 1 ==========
def are_anagrams(word1, word2):
    """
    Проверяет, являются ли два слова анаграммами.
    """
    # Приводим к нижнему регистру, удаляем пробелы и сортируем буквы
    return sorted(word1.replace(" ", "").lower()) == sorted(word2.replace(" ", "").lower())

# ========== ЗАДАНИЕ 2 ==========
def process_data(data):
    """
    Обрабатывает данные разных типов согласно условию.
    """
    if isinstance(data, list):
        # Находим индекс последнего положительного элемента
        last_positive_index = -1
        for i in range(len(data)-1, -1, -1):
            if data[i] > 0:
                last_positive_index = i
                break
        
        # Сумма элементов после последнего положительного
        sum_after_last_positive = sum(data[last_positive_index+1:]) if last_positive_index != -1 else 0
        
        # Удаляем нулевые элементы
        data_without_zeros = [x for x in data if x != 0]
        
        return {
            "type": "list",
            "sum_after_last_positive": sum_after_last_positive,
            "list_without_zeros": data_without_zeros
        }
    
    elif isinstance(data, dict):
        if not data:
            return {"type": "dict", "min_element": None}
        
        # Находим элемент с минимальным значением
        min_key = min(data, key=data.get)
        return {
            "type": "dict",
            "min_element": (min_key, data[min_key])
        }
    
    elif isinstance(data, (int, float)):
        # Выводим число в обратном порядке
        if isinstance(data, float):
            # Для дробных чисел преобразуем в строку и разворачиваем
            str_num = str(data)
            reversed_str = str_num[::-1]
            reversed_num = float(reversed_str) if '.' in reversed_str else int(reversed_str)
        else:
            reversed_num = int(str(data)[::-1])
        
        return {
            "type": "number",
            "reversed": reversed_num
        }
    
    elif isinstance(data, str):
        # Подсчитываем количество слов (разделитель - пробел)
        word_count = len(data.split())
        return {
            "type": "string",
            "word_count": word_count
        }
    
    else:
        return {"type": "unknown", "message": "Неподдерживаемый тип данных"}

# ========== ЗАДАНИЕ 3 ==========
def process_matrix(matrix):
    """
    Проверяет, все ли строки матрицы содержат положительный элемент.
    Если да - меняет знаки всех элементов на противоположные.
    """
    if not matrix:
        return matrix
    
    # Проверяем каждую строку на наличие положительного элемента
    all_rows_have_positive = all(any(element > 0 for element in row) for row in matrix)
    
    # Если условие выполняется, меняем знаки
    if all_rows_have_positive:
        return [[-element for element in row] for row in matrix]
    
    return matrix

# ========== ЗАДАНИЕ 4 ==========
def demonstrate_try_except():
    """
    Демонстрация работы try/except/finally.
    """
    print("\n=== Демонстрация try/except/finally ===")
    
    # Пример 1: Деление на ноль
    try:
        result = 10 / 0
        print(f"Результат деления: {result}")
    except ZeroDivisionError as e:
        print(f"Ошибка деления на ноль: {e}")
    finally:
        print("Блок finally выполнен после деления на ноль")
    
    # Пример 2: Преобразование строки в число
    try:
        value = int("не число")
        print(f"Преобразованное значение: {value}")
    except ValueError as e:
        print(f"Ошибка преобразования: {e}")
    finally:
        print("Блок finally выполнен после преобразования")
    
    # Пример 3: Успешное выполнение
    try:
        numbers = [1, 2, 3]
        print(f"Третий элемент списка: {numbers[2]}")
    except IndexError as e:
        print(f"Ошибка индекса: {e}")
    finally:
        print("Блок finally выполнен после работы со списком")

# ========== ТЕСТИРОВАНИЕ ==========
def main():
    print("=" * 50)
    print("ТЕСТИРОВАНИЕ РЕШЕНИЙ")
    print("=" * 50)
    
    # Тестирование задания 1
    print("\n--- ЗАДАНИЕ 1: Проверка анаграмм ---")
    test_pairs = [
        ("binary", "brainy"),
        ("раздвоение", "дозревание"),
        ("listen", "silent"),
        ("hello", "world"),
        ("", ""),
    ]
    
    for word1, word2 in test_pairs:
        result = are_anagrams(word1, word2)
        print(f"'{word1}' и '{word2}': {'Анаграммы' if result else 'Не анаграммы'}")
    
    # Тестирование задания 2
    print("\n--- ЗАДАНИЕ 2: Обработка разных типов данных ---")
    
    # Список
    test_list = [1, -2, 0, 3, 0, 4, -5, 0]
    print(f"Список: {test_list}")
    list_result = process_data(test_list)
    print(f"Результат: {list_result}")
    
    # Словарь
    test_dict = {"a": 10, "b": 5, "c": 20, "d": 3}
    print(f"\nСловарь: {test_dict}")
    dict_result = process_data(test_dict)
    print(f"Результат: {dict_result}")
    
    # Число
    test_number = 12345
    print(f"\nЧисло: {test_number}")
    number_result = process_data(test_number)
    print(f"Результат: {number_result}")
    
    # Строка
    test_string = "Это тестовая строка с несколькими словами"
    print(f"\nСтрока: '{test_string}'")
    string_result = process_data(test_string)
    print(f"Результат: {string_result}")
    
    # Тестирование задания 3
    print("\n--- ЗАДАНИЕ 3: Обработка матрицы ---")
    
    matrix1 = [
        [1, -2, 3],
        [-4, 5, -6],
        [7, -8, 9]
    ]
    print(f"Исходная матрица 1: {matrix1}")
    result1 = process_matrix(matrix1)
    print(f"Результат: {result1}")
    
    matrix2 = [
        [-1, -2, -3],
        [-4, -5, -6],
        [-7, -8, -9]
    ]
    print(f"\nИсходная матрица 2: {matrix2}")
    result2 = process_matrix(matrix2)
    print(f"Результат: {result2}")
    
    # Тестирование задания 4
    demonstrate_try_except()

if __name__ == "__main__":
    main()
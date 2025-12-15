import numpy as np

# 1.1 Создать вектор размера 10, заполненный нулями
vector_zeros = np.zeros(10)
print("1.1 Вектор из нулей:", vector_zeros)

# 1.2 Создать вектор размера 10, заполненный числом 2.5
vector_full = np.full(10, 2.5)
print("1.2 Вектор из 2.5:", vector_full)

# 1.3 Создать вектор размера 10, заполненный нулями, но пятый элемент равен 1
vector_modified = np.zeros(10)
vector_modified[4] = 1  # Индексация с 0, поэтому пятый элемент имеет индекс 4
print("1.3 Вектор с единицей на 5-й позиции:", vector_modified)

# 1.4 Создать вектор со значениями от 10 до 49
vector_range = np.arange(10, 50)
print("1.4 Вектор от 10 до 49:", vector_range)

# 1.5 Найти индексы ненулевых элементов в [1,2,0,0,4,0]
arr = np.array([1, 2, 0, 0, 4, 0])
nonzero_indices = np.nonzero(arr)
print("1.5 Индексы ненулевых элементов:", nonzero_indices[0])

# 1.6 Создать 3x3 единичную матрицу
identity_matrix = np.eye(3)
print("1.6 Единичная матрица 3x3:")
print(identity_matrix)

# 1.7 Создать массив 10x10 со случайными значениями, найти минимум и максимум
random_array = np.random.random((10, 10))
min_val = np.min(random_array)
max_val = np.max(random_array)
print(f"1.7 Минимум: {min_val:.4f}, Максимум: {max_val:.4f}")

# 1.8 Создать случайный вектор размера 30 и найти среднее значение
random_vector = np.random.random(30)
mean_val = np.mean(random_vector)
print(f"1.8 Среднее значение: {mean_val:.4f}")

# 1.9 Создать 8x8 матрицу и заполнить её в шахматном порядке
chessboard = np.zeros((8, 8), dtype=int)
chessboard[1::2, ::2] = 1  # Нечетные строки, четные столбцы
chessboard[::2, 1::2] = 1  # Четные строки, нечетные столбцы
print("1.9 Шахматная доска 8x8:")
print(chessboard)

# 1.10 Перемножить матрицы 5x3 и 3x2
matrix_a = np.random.random((5, 3))
matrix_b = np.random.random((3, 2))
matrix_product = np.dot(matrix_a, matrix_b)
print("1.10 Результат умножения матриц 5x3 и 3x2 имеет форму:", matrix_product.shape)

# 1.11 Проверить, одинаковы ли 2 numpy массива
arr1 = np.array([1, 2, 3])
arr2 = np.array([1, 2, 3])
arr3 = np.array([1, 2, 4])
are_equal_1_2 = np.array_equal(arr1, arr2)
are_equal_1_3 = np.array_equal(arr1, arr3)
print(f"1.11 arr1 и arr2 одинаковы: {are_equal_1_2}")
print(f"1.11 arr1 и arr3 одинаковы: {are_equal_1_3}")

# 1.12 Заменить максимальный элемент на ноль
arr = np.array([1, 5, 3, 9, 2, 8])
max_index = np.argmax(arr)
arr[max_index] = 0
print("1.12 Массив после замены максимума на 0:", arr)

# 1.13 Найти наиболее частое значение в массиве
arr = np.array([1, 2, 3, 2, 2, 1, 4, 2, 3])
values, counts = np.unique(arr, return_counts=True)
most_frequent = values[np.argmax(counts)]
print(f"1.13 Наиболее частое значение: {most_frequent}")

# 1.14 Найти n наибольших значений в массиве
arr = np.array([4, 2, 3, 6, 7, 8, 9, 2, 10])
n = int(input("Введите n: "))
largest_n = np.partition(arr, -n)[-n:]
largest_n_sorted = np.sort(largest_n)[::-1]
print(f"1.14 {n} наибольших значений: {largest_n_sorted}")

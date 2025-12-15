import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

plt.style.use('seaborn-v0_8')# Настройка стиля графиков для лучшего отображения
sns.set_palette("husl")

def load_dataset():# Загрузка и подготовка данных
    """Загружаем основной датасет с недвижимостью"""
    try:
        # Читаем основной файл с данными
        price_df = pd.read_csv('price_prepared.csv')

        print("=== ДАННЫЕ УСПЕШНО ЗАГРУЖЕНЫ ===")
        print(f"Исходный размер данных: {price_df.shape}")
        print(f"Столбцы в данных: {price_df.columns.tolist()}")
        if price_df.shape[1] == 1:  # Проверяем, нужно ли разделить данные из одного столбца
            print("\n=== РАЗДЕЛЯЕМ ДАННЫЕ НА ОТДЕЛЬНЫЕ СТОЛБЦЫ ===")
            # Названия для новых столбцов
            new_columns = ['Square', 'LifeSquare', 'KitchenSquare', 'm_sq', 'Price']
            # Разделяем данные по точке с запятой
            price_df = price_df.iloc[:, 0].str.split(';', expand=True)
            price_df.columns = new_columns

            # Преобразуем все в числа
            for column in new_columns:
                price_df[column] = pd.to_numeric(price_df[column], errors='coerce')

            print(f"Данные после разделения: {price_df.shape}")
            print("Новые столбцы:", price_df.columns.tolist())

        return price_df

    except FileNotFoundError:
        print("Файл price_prepared.csv не найден. Положите его в папку со скриптом.")
        return None


# Создание выборки данных
def take_sample(df):
    """Берем случайную выборку из 1000 записей"""
    sample_size = min(1000, len(df))
    sample_data = df.sample(n=sample_size, random_state=42)

    print(f"\n=== СОЗДАЕМ ВЫБОРКУ ИЗ {sample_size} ЗАПИСЕЙ ===")
    print(f"Исходный размер: {df.shape}")
    print(f"Размер выборки: {sample_data.shape}")

    return sample_data


# Проверка на пропущенные значения
def check_missing_values(df):
    """Ищем пропущенные значения в данных"""
    missing_counts = df.isnull().sum()
    missing_info = pd.DataFrame({
        'Количество пропусков': missing_counts,
        'Процент пропусков': (missing_counts / len(df)) * 100
    })

    print("\n=== ПРОВЕРЯЕМ ПРОПУЩЕННЫЕ ЗНАЧЕНИЯ ===")
    if missing_counts.sum() > 0:
        print("Найдены пропуски в данных:")
        print(missing_info[missing_info['Количество пропусков'] > 0])

        # Рисуем карту пропусков
        plt.figure(figsize=(9, 5))
        sns.heatmap(df.isnull(), cbar=True, yticklabels=False,
                    cmap='magma', alpha=0.8)
        plt.title('Карта пропущенных значений в данных')
        plt.tight_layout()
        plt.show()
    else:
        print("Пропусков не обнаружено - отлично!")

    return missing_info


# Очистка и подготовка данных
def clean_data(df):
    """Чистим данные: заполняем пропуски и убираем выбросы"""
    print("\n=== НАЧИНАЕМ ОЧИСТКУ ДАННЫХ ===")
    cleaned_df = df.copy()

    # Заполняем пропущенные значения
    print("Заполняем пропуски:")
    for column in cleaned_df.columns:
        if cleaned_df[column].isnull().any():
            if pd.api.types.is_numeric_dtype(cleaned_df[column]):
                # Для чисел используем медиану
                fill_value = cleaned_df[column].median()
                cleaned_df[column].fillna(fill_value, inplace=True)
                print(f"  Столбец {column} (числовой): заполнили медианой {fill_value:.2f}")
            else:
                # Для текста используем самое частое значение
                fill_value = cleaned_df[column].mode()[0] if len(cleaned_df[column].mode()) > 0 else 'Неизвестно'
                cleaned_df[column].fillna(fill_value, inplace=True)
                print(f"  Столбец {column} (текстовый): заполнили значением '{fill_value}'")

    # Обрабатываем выбросы в числовых столбцах
    numeric_columns = cleaned_df.select_dtypes(include=[np.number]).columns
    print("\nОбрабатываем выбросы:")

    for column in numeric_columns:
        # Считаем квантили для определения выбросов
        Q1 = cleaned_df[column].quantile(0.25)
        Q3 = cleaned_df[column].quantile(0.75)
        IQR = Q3 - Q1

        if IQR > 0:
            lower_bound = Q1 - 1.5 * IQR
            upper_bound = Q3 + 1.5 * IQR

            # Считаем сколько выбросов
            low_outliers = (cleaned_df[column] < lower_bound).sum()
            high_outliers = (cleaned_df[column] > upper_bound).sum()
            total_outliers = low_outliers + high_outliers

            if total_outliers > 0:
                print(f"  Столбец {column}: найдено {total_outliers} выбросов")

                # Заменяем выбросы граничными значениями
                cleaned_df[column] = np.clip(cleaned_df[column], lower_bound, upper_bound)

    print(f"Пропусков после очистки: {cleaned_df.isnull().sum().sum()}")
    return cleaned_df


# Основной анализ данных
def analyze_data(df):
    """Проводим полный анализ данных"""
    print("\n" + "=" * 50)
    print("=== НАЧИНАЕМ ПОЛНЫЙ АНАЛИЗ ДАННЫХ ===")
    print("=" * 50)

    # Базовая статистика
    print("\n1. ОСНОВНАЯ СТАТИСТИКА:")
    # Округляем статистику до 2 знаков после запятой
    stats = df.describe()
    print(stats.round(2))

    # Анализ числовых данных
    numeric_columns = df.select_dtypes(include=[np.number]).columns

    if len(numeric_columns) > 0:
        print(f"\n2. АНАЛИЗ ЧИСЛОВЫХ ДАННЫХ ({len(numeric_columns)} столбцов):")

        # Создаем сетку для графиков
        columns_per_row = min(3, len(numeric_columns))
        rows_count = (len(numeric_columns) + columns_per_row - 1) // columns_per_row

        fig, axes = plt.subplots(rows_count, columns_per_row, figsize=(14, 4 * rows_count))

        # Преобразуем axes в плоский список для удобства
        if rows_count > 1:
            axes_flat = axes.flatten()
        else:
            axes_flat = [axes] if columns_per_row == 1 else axes

        # Рисуем гистограммы для каждого числового столбца
        column_index = 0
        for column in numeric_columns:
            if column_index < len(axes_flat):
                df[column].hist(bins=15, ax=axes_flat[column_index],
                                alpha=0.7, color='lightcoral', edgecolor='darkred')
                axes_flat[column_index].set_title(f'Распределение: {column}')
                axes_flat[column_index].set_xlabel(column)
                axes_flat[column_index].set_ylabel('Количество')
                column_index += 1

        # Скрываем пустые графики
        for i in range(column_index, len(axes_flat)):
            axes_flat[i].set_visible(False)

        plt.tight_layout()
        plt.show()

    # Анализ корреляций
    if len(numeric_columns) > 1:
        print("\n3. АНАЛИЗ ВЗАИМОСВЯЗЕЙ МЕЖДУ ДАННЫМИ:")

        plt.figure(figsize=(9, 7))
        correlation_data = df[numeric_columns].corr()
        # Скрываем повторяющиеся значения
        mask = np.triu(np.ones_like(correlation_data, dtype=bool))

        sns.heatmap(correlation_data, mask=mask, annot=True, cmap='YlOrRd',
                    center=0, fmt='.2f', square=True, cbar_kws={'shrink': 0.8})
        plt.title('Карта взаимосвязей между показателями')
        plt.tight_layout()
        plt.show()

        # Ищем сильные корреляции
        print("Сильные взаимосвязи (коэффициент > 0.5):")
        correlations = correlation_data.unstack().sort_values(key=abs, ascending=False)
        strong_correlations = correlations[(correlations != 1.0) & (abs(correlations) > 0.5)]

        if len(strong_correlations) > 0:
            for columns_pair, correlation_value in strong_correlations.items():
                # Округляем корреляцию до 2 знаков
                rounded_corr = round(correlation_value, 2)
                print(f"  {columns_pair[0]} <-> {columns_pair[1]}: {rounded_corr}")
        else:
            print("  Сильных взаимосвязей не обнаружено")

    # Анализ текстовых данных
    text_columns = df.select_dtypes(include=['object']).columns
    if len(text_columns) > 0:
        print(f"\n4. АНАЛИЗ ТЕКСТОВЫХ ДАННЫХ ({len(text_columns)} столбцов):")

        for column in text_columns:
            value_distribution = df[column].value_counts()
            print(f"\n  Столбец: {column}")
            print(f"    Уникальных значений: {df[column].nunique()}")
            print(f"    Самые частые значения:")

            count = 0
            for value, frequency in value_distribution.head().items():
                # Округляем процент до 2 знаков после запятой
                percentage = (frequency / len(df)) * 100
                rounded_percentage = round(percentage, 2)
                print(f"      '{value}': {frequency} раз ({rounded_percentage}%)")
                count += 1

# Сохранение результатов
def save_cleaned_data(df, filename='surname.csv'):
    """Сохраняем очищенные данные в файл"""
    df.to_csv(filename, index=False)
    print(f"\n" + "=" * 50)
    print("=== РЕЗУЛЬТАТЫ СОХРАНЕНЫ ===")
    print(f"Файл с результатами: {filename}")
    print(f"Размер данных: {df.shape}")
    print(f"Столбцы: {list(df.columns)}")
    print("=" * 50)


# Главная функция программы
def main():
    """Запускаем весь процесс анализа данных"""
    # Загружаем данные
    main_data = load_dataset()

    if main_data is not None:
        sample_data = take_sample(main_data)

        # Проверяем на пропуски
        check_missing_values(sample_data)

        # Очищаем данные
        cleaned_data = clean_data(sample_data)

        # Анализируем данные
        analyze_data(cleaned_data)

        # Сохраняем результаты
        save_cleaned_data(cleaned_data)


# Запускаем программу если файл выполняется напрямую
if __name__ == "__main__":
    main()


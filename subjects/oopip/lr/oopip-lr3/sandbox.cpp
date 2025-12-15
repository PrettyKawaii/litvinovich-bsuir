#include <iostream>
#include <vector>
#include <list>
#include <array>

int main()
{
    // Создание vector с целыми числами
    std::vector<int> numbers = {1, 2, 3, 4, 5};
    numbers.push_back(6); // Добавление элемента

    // Создание list со строками
    std::list<std::string> names = {"Анна", "Борис", "Виктор"};
    names.push_front("Алексей"); // Добавление в начало

    // Создание array с фиксированным размером
    std::array<double, 5> temperatures = {36.6, 37.0, 36.8, 37.2, 36.9};

    // Вывод элементов vector
    std::cout << "Vector: ";
    for (const auto &num : numbers)
    {
        std::cout << num << " ";
    }

    // Вывод элементов list
    std::cout << "\nList: ";
    for (const auto &name : names)
    {
        std::cout << name << " ";
    }

    // Вывод элементов array
    std::cout << "\nArray: ";
    for (const auto &temp : temperatures)
    {
        std::cout << temp << " ";
    }

    return 0;
}
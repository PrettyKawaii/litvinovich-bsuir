#include <iostream>
#include <vector>
#include <list>
#include <array>
#include <algorithm>
#include <fstream>
#include <iomanip>
#include <string>

using namespace std;

class Employee
{
private:
    string name;
    string position;
    double hoursWorked;
    string date;

public:
    Employee() : name(""), position(""), hoursWorked(0), date("") {}
    Employee(string n, string p, double h, string d) : name(n), position(p), hoursWorked(h), date(d) {}

    string getName() const { return name; }
    string getPosition() const { return position; }
    double getHours() const { return hoursWorked; }
    string getDate() const { return date; }

    void setName(string n) { name = n; }
    void setPosition(string p) { position = p; }
    void setHours(double h) { hoursWorked = h; }
    void setDate(string d) { date = d; }

    bool operator<(const Employee &other) const { return hoursWorked < other.hoursWorked; }
    bool operator==(const Employee &other) const { return name == other.name; }
    bool operator>(const Employee &other) const { return hoursWorked > other.hoursWorked; }
};

// Перегрузка оператора вывода вне класса
ostream &operator<<(ostream &os, const Employee &emp)
{
    os << left << setw(15) << emp.getName() << setw(15) << emp.getPosition()
       << setw(10) << emp.getHours() << setw(12) << emp.getDate();
    return os;
}

class TimeTracker
{
private:
    vector<Employee> vecEmployees;
    list<Employee> lstEmployees;
    array<Employee, 100> arrEmployees;
    size_t arrSize = 0;

public:
    void addEmployee(const Employee &emp)
    {
        vecEmployees.push_back(emp);
        lstEmployees.push_back(emp);
        if (arrSize < arrEmployees.size())
        {
            arrEmployees[arrSize++] = emp;
        }
        cout << "Сотрудник добавлен!\n";
    }

    void removeEmployee(const string &name)
    {
        // Vector
        auto it = remove_if(vecEmployees.begin(), vecEmployees.end(),
                            [&](const Employee &e)
                            { return e.getName() == name; });
        if (it != vecEmployees.end())
        {
            vecEmployees.erase(it, vecEmployees.end());
            cout << "Сотрудник удален из vector\n";
        }

        // List
        size_t listSizeBefore = lstEmployees.size();
        lstEmployees.remove_if([&](const Employee &e)
                               { return e.getName() == name; });
        if (lstEmployees.size() < listSizeBefore)
        {
            cout << "Сотрудник удален из list\n";
        }

        // Array
        bool found = false;
        for (size_t i = 0; i < arrSize; i++)
        {
            if (arrEmployees[i].getName() == name)
            {
                for (size_t j = i; j < arrSize - 1; j++)
                {
                    arrEmployees[j] = arrEmployees[j + 1];
                }
                arrSize--;
                found = true;
                cout << "Сотрудник удален из array\n";
                break;
            }
        }

        if (!found)
        {
            cout << "Сотрудник не найден!\n";
        }
    }

    void findEmployee(const string &name)
    {
        cout << "\nРезультаты поиска '" << name << "':\n";
        cout << setw(15) << "Имя" << setw(15) << "Должность"
             << setw(10) << "Часы" << setw(12) << "Дата" << "\n";

        bool found = false;
        for (const auto &emp : vecEmployees)
        {
            if (emp.getName().find(name) != string::npos)
            {
                cout << emp << "\n";
                found = true;
            }
        }

        if (!found)
        {
            cout << "Сотрудники не найдены\n";
        }
    }

    void sortByHours()
    {
        sort(vecEmployees.begin(), vecEmployees.end());
        lstEmployees.sort();

        for (size_t i = 0; i < arrSize - 1; i++)
        {
            for (size_t j = 0; j < arrSize - i - 1; j++)
            {
                if (arrEmployees[j].getHours() > arrEmployees[j + 1].getHours())
                {
                    swap(arrEmployees[j], arrEmployees[j + 1]);
                }
            }
        }
        cout << "Данные отсортированы по часам\n";
    }

    void displayAll()
    {
        if (vecEmployees.empty())
        {
            cout << "Нет данных для отображения\n";
            return;
        }

        cout << "\n=== VECTOR (" << vecEmployees.size() << " записей) ===\n";
        cout << setw(15) << "Имя" << setw(15) << "Должность"
             << setw(10) << "Часы" << setw(12) << "Дата" << "\n";
        for (const auto &emp : vecEmployees)
        {
            cout << emp << "\n";
        }

        cout << "\n=== LIST (" << lstEmployees.size() << " записей) ===\n";
        for (const auto &emp : lstEmployees)
        {
            cout << emp << "\n";
        }

        cout << "\n=== ARRAY (" << arrSize << " записей) ===\n";
        for (size_t i = 0; i < arrSize; i++)
        {
            cout << arrEmployees[i] << "\n";
        }
    }

    void saveToFile(const string &filename)
    {
        ofstream file(filename);
        if (file.is_open())
        {
            file << "Имя,Должность,Часы,Дата\n";
            for (const auto &emp : vecEmployees)
            {
                file << emp.getName() << "," << emp.getPosition() << ","
                     << emp.getHours() << "," << emp.getDate() << "\n";
            }
            file.close();
            cout << "Данные сохранены в " << filename << "\n";
        }
        else
        {
            cout << "Ошибка открытия файла!\n";
        }
    }

    void filterByPosition(const string &position)
    {
        cout << "\nСотрудники на должности '" << position << "':\n";
        cout << setw(15) << "Имя" << setw(15) << "Должность"
             << setw(10) << "Часы" << setw(12) << "Дата" << "\n";

        bool found = false;
        for (const auto &emp : vecEmployees)
        {
            if (emp.getPosition() == position)
            {
                cout << emp << "\n";
                found = true;
            }
        }

        if (!found)
        {
            cout << "Сотрудники не найдены\n";
        }
    }
};

void showMenu()
{
    cout << "\n=== Учет рабочего времени банковских сотрудников ===\n";
    cout << "1. Добавить сотрудника\n";
    cout << "2. Удалить сотрудника\n";
    cout << "3. Найти сотрудника\n";
    cout << "4. Сортировать по часам\n";
    cout << "5. Показать всех\n";
    cout << "6. Сохранить в файл\n";
    cout << "7. Фильтр по должности\n";
    cout << "8. Выход\n";
    cout << "Выбор: ";
}

Employee inputEmployee()
{
    string name, position, date;
    double hours;

    cout << "Имя: ";
    cin >> name;
    cout << "Должность: ";
    cin >> position;
    cout << "Отработано часов: ";
    cin >> hours;
    cout << "Дата (ДД.ММ.ГГГГ): ";
    cin >> date;

    return Employee(name, position, hours, date);
}

int main()
{
    TimeTracker tracker;
    int choice;

    // Тестовые данные
    tracker.addEmployee(Employee("Иванов", "Кассир", 160.5, "15.01.2024"));
    tracker.addEmployee(Employee("Петрова", "Менеджер", 175.0, "15.01.2024"));
    tracker.addEmployee(Employee("Сидоров", "Аналитик", 152.0, "15.01.2024"));

    do
    {
        showMenu();
        cin >> choice;

        switch (choice)
        {
        case 1:
        {
            Employee emp = inputEmployee();
            tracker.addEmployee(emp);
            break;
        }
        case 2:
        {
            string name;
            cout << "Имя для удаления: ";
            cin >> name;
            tracker.removeEmployee(name);
            break;
        }
        case 3:
        {
            string name;
            cout << "Имя для поиска: ";
            cin >> name;
            tracker.findEmployee(name);
            break;
        }
        case 4:
            tracker.sortByHours();
            break;
        case 5:
            tracker.displayAll();
            break;
        case 6:
            tracker.saveToFile("employees.csv");
            break;
        case 7:
        {
            string position;
            cout << "Должность для фильтра: ";
            cin >> position;
            tracker.filterByPosition(position);
            break;
        }
        case 8:
            cout << "Выход...\n";
            break;
        default:
            cout << "Неверный выбор!\n";
        }
    } while (choice != 8);

    return 0;
}
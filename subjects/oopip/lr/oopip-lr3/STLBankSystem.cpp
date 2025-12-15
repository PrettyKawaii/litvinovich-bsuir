#include "STLBankSystem.h"
#include <iostream>
#include <iomanip>
#include <fstream>
#include <sstream>
#include <limits>
#include <algorithm>

STLBankSystem::STLBankSystem()
{
    daysOfWeek = {"Понедельник", "Вторник", "Среда", "Четверг",
                  "Пятница", "Суббота", "Воскресенье"};
}

void STLBankSystem::addEmployee()
{
    std::cout << "\n=== Добавление сотрудника ===\n";

    auto employee = std::make_shared<BankEmployee>();
    employee->inputInfo();

    // Проверка на уникальность ID
    for (const auto &emp : employees)
    {
        if (emp->getEmployeeId() == employee->getEmployeeId())
        {
            std::cout << "Ошибка: сотрудник с таким ID уже существует!\n";
            return;
        }
    }

    employees.push_back(employee);
    std::cout << "Сотрудник успешно добавлен в vector!\n";
}

void STLBankSystem::displayEmployees() const
{
    if (employees.empty())
    {
        std::cout << "Нет сотрудников для отображения.\n";
        return;
    }

    std::cout << "\n=== Список сотрудников (vector) ===\n";
    std::cout << std::left
              << std::setw(5) << "ID"
              << std::setw(20) << "ФИО"
              << std::setw(15) << "Должность"
              << std::setw(10) << "Зарплата" << std::endl;
    std::cout << std::string(50, '-') << std::endl;

    for (const auto &emp : employees)
    {
        emp->displayInfo();
        std::cout << std::endl;
    }
}

void STLBankSystem::editEmployee()
{
    int id;
    std::cout << "Введите ID сотрудника для редактирования: ";
    std::cin >> id;

    auto it = std::find_if(employees.begin(), employees.end(),
                           [id](const std::shared_ptr<BankEmployee> &emp)
                           {
                               return emp->getEmployeeId() == id;
                           });

    if (it != employees.end())
    {
        std::cout << "Текущая информация:\n";
        (*it)->displayInfo();
        std::cout << "\nВведите новую информацию:\n";
        (*it)->inputInfo();
        std::cout << "Сотрудник успешно отредактирован!\n";
    }
    else
    {
        std::cout << "Сотрудник с ID " << id << " не найден.\n";
    }
}

void STLBankSystem::deleteEmployee()
{
    int id;
    std::cout << "Введите ID сотрудника для удаления: ";
    std::cin >> id;

    auto it = std::remove_if(employees.begin(), employees.end(),
                             [id](const std::shared_ptr<BankEmployee> &emp)
                             {
                                 return emp->getEmployeeId() == id;
                             });

    if (it != employees.end())
    {
        employees.erase(it, employees.end());
        std::cout << "Сотрудник с ID " << id << " удален из vector.\n";

        timeRecords.remove_if([id](const WorkTimeRecord &record)
                              { return record.getEmployeeId() == id; });
    }
    else
    {
        std::cout << "Сотрудник с ID " << id << " не найден.\n";
    }
}

void STLBankSystem::searchEmployeeById() const
{
    int id;
    std::cout << "Введите ID сотрудника для поиска: ";
    std::cin >> id;

    auto it = std::find_if(employees.begin(), employees.end(),
                           [id](const std::shared_ptr<BankEmployee> &emp)
                           {
                               return emp->getEmployeeId() == id;
                           });

    if (it != employees.end())
    {
        std::cout << "\n=== Найденный сотрудник ===\n";
        std::cout << std::left
                  << std::setw(5) << "ID"
                  << std::setw(20) << "ФИО"
                  << std::setw(15) << "Должность"
                  << std::setw(10) << "Зарплата" << std::endl;
        std::cout << std::string(50, '-') << std::endl;
        (*it)->displayInfo();
        std::cout << std::endl;
    }
    else
    {
        std::cout << "Сотрудник с ID " << id << " не найден.\n";
    }
}

void STLBankSystem::searchEmployeeByName() const
{
    std::string name;
    std::cout << "Введите имя для поиска: ";
    std::cin.ignore();
    std::getline(std::cin, name);

    std::cout << "\n=== Результаты поиска ===\n";
    std::cout << std::left
              << std::setw(5) << "ID"
              << std::setw(20) << "ФИО"
              << std::setw(15) << "Должность"
              << std::setw(10) << "Зарплата" << std::endl;
    std::cout << std::string(50, '-') << std::endl;

    bool found = false;
    for (const auto &emp : employees)
    {
        if (emp->getName().find(name) != std::string::npos)
        {
            emp->displayInfo();
            std::cout << std::endl;
            found = true;
        }
    }

    if (!found)
    {
        std::cout << "Сотрудники с именем '" << name << "' не найдены.\n";
    }
}

void STLBankSystem::sortEmployeesByName()
{
    std::sort(employees.begin(), employees.end(),
              [](const std::shared_ptr<BankEmployee> &a,
                 const std::shared_ptr<BankEmployee> &b)
              {
                  return a->getName() < b->getName();
              });
    std::cout << "Сотрудники отсортированы по имени.\n";
}

void STLBankSystem::sortEmployeesBySalary()
{
    std::sort(employees.begin(), employees.end(),
              [](const std::shared_ptr<BankEmployee> &a,
                 const std::shared_ptr<BankEmployee> &b)
              {
                  return a->getSalary() < b->getSalary();
              });
    std::cout << "Сотрудники отсортированы по зарплате.\n";
}

void STLBankSystem::addTimeRecord()
{
    WorkTimeRecord record;
    record.inputRecord();

    // Проверка существования сотрудника
    bool employeeExists = false;
    for (const auto &emp : employees)
    {
        if (emp->getEmployeeId() == record.getEmployeeId())
        {
            employeeExists = true;
            break;
        }
    }

    if (!employeeExists)
    {
        std::cout << "Ошибка: сотрудник с ID " << record.getEmployeeId() << " не существует!\n";
        return;
    }

    timeRecords.push_back(record);
    std::cout << "Запись рабочего времени добавлена в list!\n";
}

void STLBankSystem::displayTimeRecords() const
{
    if (timeRecords.empty())
    {
        std::cout << "Нет записей рабочего времени.\n";
        return;
    }

    std::cout << "\n=== Записи рабочего времени (list) ===\n";
    std::cout << std::left
              << std::setw(5) << "ID"
              << std::setw(12) << "Дата"
              << std::setw(8) << "Часы"
              << std::setw(25) << "Описание задачи" << std::endl;
    std::cout << std::string(50, '-') << std::endl;

    for (const auto &record : timeRecords)
    {
        record.displayRecord();
        std::cout << std::endl;
    }
}

void STLBankSystem::editTimeRecord()
{
    int empId;
    std::string date;
    std::cout << "Введите ID сотрудника записи для редактирования: ";
    std::cin >> empId;
    std::cout << "Введите дату записи (ДД.ММ.ГГГГ): ";
    std::cin.ignore();
    std::getline(std::cin, date);

    auto it = std::find_if(timeRecords.begin(), timeRecords.end(),
                           [empId, date](const WorkTimeRecord &record)
                           {
                               return record.getEmployeeId() == empId && record.getDate() == date;
                           });

    if (it != timeRecords.end())
    {
        std::cout << "Текущая запись:\n";
        it->displayRecord();
        std::cout << "\nВведите новую информацию:\n";
        it->inputRecord();
        std::cout << "Запись успешно отредактирована!\n";
    }
    else
    {
        std::cout << "Запись не найдена.\n";
    }
}

void STLBankSystem::deleteTimeRecord()
{
    int empId;
    std::string date;
    std::cout << "Введите ID сотрудника записи для удаления: ";
    std::cin >> empId;
    std::cout << "Введите дату записи (ДД.ММ.ГГГГ): ";
    std::cin.ignore();
    std::getline(std::cin, date);

    timeRecords.remove_if([empId, date](const WorkTimeRecord &record)
                          { return record.getEmployeeId() == empId && record.getDate() == date; });

    std::cout << "Записи удалены.\n";
}

void STLBankSystem::searchTimeRecordsByEmployee() const
{
    int empId;
    std::cout << "Введите ID сотрудника для поиска записей: ";
    std::cin >> empId;

    std::cout << "\n=== Записи сотрудника " << empId << " ===\n";
    std::cout << std::left
              << std::setw(5) << "ID"
              << std::setw(12) << "Дата"
              << std::setw(8) << "Часы"
              << std::setw(25) << "Описание задачи" << std::endl;
    std::cout << std::string(50, '-') << std::endl;

    bool found = false;
    for (const auto &record : timeRecords)
    {
        if (record.getEmployeeId() == empId)
        {
            record.displayRecord();
            std::cout << std::endl;
            found = true;
        }
    }

    if (!found)
    {
        std::cout << "Записи для сотрудника с ID " << empId << " не найдены.\n";
    }
}

void STLBankSystem::searchTimeRecordsByDate() const
{
    std::string date;
    std::cout << "Введите дату для поиска записей (ДД.ММ.ГГГГ): ";
    std::cin.ignore();
    std::getline(std::cin, date);

    std::cout << "\n=== Записи за " << date << " ===\n";
    std::cout << std::left
              << std::setw(5) << "ID"
              << std::setw(12) << "Дата"
              << std::setw(8) << "Часы"
              << std::setw(25) << "Описание задачи" << std::endl;
    std::cout << std::string(50, '-') << std::endl;

    bool found = false;
    for (const auto &record : timeRecords)
    {
        if (record.getDate() == date)
        {
            record.displayRecord();
            std::cout << std::endl;
            found = true;
        }
    }

    if (!found)
    {
        std::cout << "Записи за дату " << date << " не найдены.\n";
    }
}

void STLBankSystem::sortTimeRecordsByDate()
{
    timeRecords.sort([](const WorkTimeRecord &a, const WorkTimeRecord &b)
                     { return a.getDate() < b.getDate(); });
    std::cout << "Записи отсортированы по дате.\n";
}

void STLBankSystem::sortTimeRecordsByHours()
{
    timeRecords.sort([](const WorkTimeRecord &a, const WorkTimeRecord &b)
                     { return a.getHoursWorked() < b.getHoursWorked(); });
    std::cout << "Записи отсортированы по количеству часов.\n";
}

void STLBankSystem::displayDaysOfWeek() const
{
    std::cout << "\n=== Дни недели (array) ===\n";
    for (size_t i = 0; i < daysOfWeek.size(); ++i)
    {
        std::cout << i + 1 << ". " << daysOfWeek[i] << std::endl;
    }
}

void STLBankSystem::demonstrateArrayOperations() const
{
    std::cout << "\n=== Операции с array ===\n";
    std::cout << "Первый день: " << daysOfWeek.front() << std::endl;
    std::cout << "Последний день: " << daysOfWeek.back() << std::endl;
    std::cout << "Третий день: " << daysOfWeek[2] << std::endl;
    std::cout << "Размер массива: " << daysOfWeek.size() << std::endl;

    std::cout << "Все дни: ";
    for (const auto &day : daysOfWeek)
    {
        std::cout << day << " ";
    }
    std::cout << std::endl;
}

void STLBankSystem::saveToFiles() const
{
    std::ofstream empFile("employees.txt");
    if (empFile.is_open())
    {
        for (const auto &emp : employees)
        {
            empFile << *emp << std::endl;
        }
        empFile.close();
        std::cout << "Сотрудники сохранены в файл 'employees.txt'\n";
    }
    else
    {
        std::cout << "Ошибка сохранения сотрудников!\n";
    }

    std::ofstream timeFile("time_records.txt");
    if (timeFile.is_open())
    {
        for (const auto &record : timeRecords)
        {
            timeFile << record << std::endl;
        }
        timeFile.close();
        std::cout << "Записи времени сохранены в файл 'time_records.txt'\n";
    }
    else
    {
        std::cout << "Ошибка сохранения записей времени!\n";
    }
}

void STLBankSystem::loadFromFiles()
{
    employees.clear();
    timeRecords.clear();

    std::ifstream empFile("employees.txt");
    if (empFile.is_open())
    {
        std::string line;
        while (std::getline(empFile, line))
        {
            if (!line.empty())
            {
                auto employee = std::make_shared<BankEmployee>();
                std::istringstream iss(line);
                iss >> *employee;
                employees.push_back(employee);
            }
        }
        empFile.close();
        std::cout << "Сотрудники загружены из файла 'employees.txt'\n";
    }

    std::ifstream timeFile("time_records.txt");
    if (timeFile.is_open())
    {
        std::string line;
        while (std::getline(timeFile, line))
        {
            if (!line.empty())
            {
                WorkTimeRecord record;
                std::istringstream iss(line);
                iss >> record;
                timeRecords.push_back(record);
            }
        }
        timeFile.close();
        std::cout << "Записи времени загружены из файла 'time_records.txt'\n";
    }
}

void STLBankSystem::showMainMenu() const
{
    std::cout << "\n=== Система учета рабочего времени банка (STL) ===\n";
    std::cout << "1. Управление сотрудниками (vector)\n";
    std::cout << "2. Управление записями времени (list)\n";
    std::cout << "3. Дни недели (array)\n";
    std::cout << "4. Сохранить данные в файлы\n";
    std::cout << "5. Загрузить данные из файлов\n";
    std::cout << "0. Выход\n";
    std::cout << "Выберите опцию: ";
}

void STLBankSystem::showEmployeeMenu() const
{
    std::cout << "\n=== Управление сотрудниками (vector) ===\n";
    std::cout << "1. Добавить сотрудника\n";
    std::cout << "2. Показать всех сотрудников\n";
    std::cout << "3. Редактировать сотрудника\n";
    std::cout << "4. Удалить сотрудника\n";
    std::cout << "5. Поиск по ID\n";
    std::cout << "6. Поиск по имени\n";
    std::cout << "7. Сортировать по имени\n";
    std::cout << "8. Сортировать по зарплате\n";
    std::cout << "0. Назад\n";
    std::cout << "Выберите опцию: ";
}

void STLBankSystem::showTimeRecordMenu() const
{
    std::cout << "\n=== Управление записями времени (list) ===\n";
    std::cout << "1. Добавить запись\n";
    std::cout << "2. Показать все записи\n";
    std::cout << "3. Редактировать запись\n";
    std::cout << "4. Удалить запись\n";
    std::cout << "5. Поиск по сотруднику\n";
    std::cout << "6. Поиск по дате\n";
    std::cout << "7. Сортировать по дате\n";
    std::cout << "8. Сортировать по часам\n";
    std::cout << "0. Назад\n";
    std::cout << "Выберите опцию: ";
}

void STLBankSystem::run()
{
    int mainChoice, subChoice;

    do
    {
        showMainMenu();
        std::cin >> mainChoice;

        switch (mainChoice)
        {
        case 1:
            do
            {
                showEmployeeMenu();
                std::cin >> subChoice;
                switch (subChoice)
                {
                case 1:
                    addEmployee();
                    break;
                case 2:
                    displayEmployees();
                    break;
                case 3:
                    editEmployee();
                    break;
                case 4:
                    deleteEmployee();
                    break;
                case 5:
                    searchEmployeeById();
                    break;
                case 6:
                    searchEmployeeByName();
                    break;
                case 7:
                    sortEmployeesByName();
                    break;
                case 8:
                    sortEmployeesBySalary();
                    break;
                case 0:
                    break;
                default:
                    std::cout << "Неверный выбор!\n";
                }
            } while (subChoice != 0);
            break;

        case 2:
            do
            {
                showTimeRecordMenu();
                std::cin >> subChoice;
                switch (subChoice)
                {
                case 1:
                    addTimeRecord();
                    break;
                case 2:
                    displayTimeRecords();
                    break;
                case 3:
                    editTimeRecord();
                    break;
                case 4:
                    deleteTimeRecord();
                    break;
                case 5:
                    searchTimeRecordsByEmployee();
                    break;
                case 6:
                    searchTimeRecordsByDate();
                    break;
                case 7:
                    sortTimeRecordsByDate();
                    break;
                case 8:
                    sortTimeRecordsByHours();
                    break;
                case 0:
                    break;
                default:
                    std::cout << "Неверный выбор!\n";
                }
            } while (subChoice != 0);
            break;

        case 3:
            displayDaysOfWeek();
            demonstrateArrayOperations();
            break;

        case 4:
            saveToFiles();
            break;

        case 5:
            loadFromFiles();
            break;

        case 0:
            std::cout << "Выход из программы.\n";
            break;

        default:
            std::cout << "Неверный выбор!\n";
        }

    } while (mainChoice != 0);
}
#include "BankEmployee.h"
#include <limits>

BankEmployee::BankEmployee()
    : name(""), position(""), employeeId(0), salary(0.0) {}

BankEmployee::BankEmployee(const std::string &name, const std::string &position,
                           int employeeId, double salary)
    : name(name), position(position), employeeId(employeeId), salary(salary) {}

BankEmployee::~BankEmployee() {}

std::string BankEmployee::getName() const { return name; }
std::string BankEmployee::getPosition() const { return position; }
int BankEmployee::getEmployeeId() const { return employeeId; }
double BankEmployee::getSalary() const { return salary; }

void BankEmployee::setName(const std::string &name) { this->name = name; }
void BankEmployee::setPosition(const std::string &position) { this->position = position; }
void BankEmployee::setEmployeeId(int id) { this->employeeId = id; }
void BankEmployee::setSalary(double salary) { this->salary = salary; }

void BankEmployee::displayInfo() const
{
    std::cout << std::left
              << std::setw(5) << employeeId
              << std::setw(20) << name
              << std::setw(15) << position
              << std::setw(10) << std::fixed << std::setprecision(2) << salary;
}

void BankEmployee::inputInfo()
{
    std::cout << "Введите ID сотрудника: ";
    std::cin >> employeeId;
    std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');

    std::cout << "Введите ФИО сотрудника: ";
    std::getline(std::cin, name);

    std::cout << "Введите должность: ";
    std::getline(std::cin, position);

    std::cout << "Введите зарплату: ";
    std::cin >> salary;
}

std::ostream &operator<<(std::ostream &os, const BankEmployee &emp)
{
    os << emp.employeeId << ";" << emp.name << ";" << emp.position << ";" << emp.salary;
    return os;
}

std::istream &operator>>(std::istream &is, BankEmployee &emp)
{
    std::string line;
    if (std::getline(is, line))
    {
        size_t pos1 = line.find(';');
        size_t pos2 = line.find(';', pos1 + 1);
        size_t pos3 = line.find(';', pos2 + 1);

        if (pos1 != std::string::npos && pos2 != std::string::npos && pos3 != std::string::npos)
        {
            emp.employeeId = std::stoi(line.substr(0, pos1));
            emp.name = line.substr(pos1 + 1, pos2 - pos1 - 1);
            emp.position = line.substr(pos2 + 1, pos3 - pos2 - 1);
            emp.salary = std::stod(line.substr(pos3 + 1));
        }
    }
    return is;
}
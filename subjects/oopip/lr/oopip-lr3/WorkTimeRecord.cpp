#include "WorkTimeRecord.h"
#include <limits>

WorkTimeRecord::WorkTimeRecord()
    : employeeId(0), date(""), hoursWorked(0.0), taskDescription("") {}

WorkTimeRecord::WorkTimeRecord(int empId, const std::string &date,
                               double hours, const std::string &task)
    : employeeId(empId), date(date), hoursWorked(hours), taskDescription(task) {}

int WorkTimeRecord::getEmployeeId() const { return employeeId; }
std::string WorkTimeRecord::getDate() const { return date; }
double WorkTimeRecord::getHoursWorked() const { return hoursWorked; }
std::string WorkTimeRecord::getTaskDescription() const { return taskDescription; }

void WorkTimeRecord::setEmployeeId(int id) { employeeId = id; }
void WorkTimeRecord::setDate(const std::string &date) { this->date = date; }
void WorkTimeRecord::setHoursWorked(double hours) { hoursWorked = hours; }
void WorkTimeRecord::setTaskDescription(const std::string &task) { taskDescription = task; }

void WorkTimeRecord::displayRecord() const
{
    std::cout << std::left
              << std::setw(5) << employeeId
              << std::setw(12) << date
              << std::setw(8) << std::fixed << std::setprecision(2) << hoursWorked
              << std::setw(25) << taskDescription;
}

void WorkTimeRecord::inputRecord()
{
    std::cout << "Введите ID сотрудника: ";
    std::cin >> employeeId;
    std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');

    std::cout << "Введите дату (ДД.ММ.ГГГГ): ";
    std::getline(std::cin, date);

    std::cout << "Введите отработанные часы: ";
    std::cin >> hoursWorked;
    std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');

    std::cout << "Введите описание задачи: ";
    std::getline(std::cin, taskDescription);
}

std::ostream &operator<<(std::ostream &os, const WorkTimeRecord &record)
{
    os << record.employeeId << ";" << record.date << ";" << record.hoursWorked
       << ";" << record.taskDescription;
    return os;
}

std::istream &operator>>(std::istream &is, WorkTimeRecord &record)
{
    std::string line;
    if (std::getline(is, line))
    {
        size_t pos1 = line.find(';');
        size_t pos2 = line.find(';', pos1 + 1);
        size_t pos3 = line.find(';', pos2 + 1);

        if (pos1 != std::string::npos && pos2 != std::string::npos && pos3 != std::string::npos)
        {
            record.employeeId = std::stoi(line.substr(0, pos1));
            record.date = line.substr(pos1 + 1, pos2 - pos1 - 1);
            record.hoursWorked = std::stod(line.substr(pos2 + 1, pos3 - pos2 - 1));
            record.taskDescription = line.substr(pos3 + 1);
        }
    }
    return is;
}
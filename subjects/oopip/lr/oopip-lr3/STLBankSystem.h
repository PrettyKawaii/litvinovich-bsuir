#ifndef STLBANKSYSTEM_H
#define STLBANKSYSTEM_H

#include "BankEmployee.h"
#include "WorkTimeRecord.h"
#include <vector>
#include <list>
#include <array>
#include <algorithm>
#include <memory>
#include <fstream>

class STLBankSystem
{
private:
    std::vector<std::shared_ptr<BankEmployee>> employees;
    std::list<WorkTimeRecord> timeRecords;
    std::array<std::string, 7> daysOfWeek;

public:
    STLBankSystem();

    void addEmployee();
    void displayEmployees() const;
    void editEmployee();
    void deleteEmployee();
    void searchEmployeeById() const;
    void searchEmployeeByName() const;
    void sortEmployeesByName();
    void sortEmployeesBySalary();

    void addTimeRecord();
    void displayTimeRecords() const;
    void editTimeRecord();
    void deleteTimeRecord();
    void searchTimeRecordsByEmployee() const;
    void searchTimeRecordsByDate() const;
    void sortTimeRecordsByDate();
    void sortTimeRecordsByHours();

    void displayDaysOfWeek() const;
    void demonstrateArrayOperations() const;

    void saveToFiles() const;
    void loadFromFiles();

    void run();

private:
    void showMainMenu() const;
    void showEmployeeMenu() const;
    void showTimeRecordMenu() const;
};

#endif
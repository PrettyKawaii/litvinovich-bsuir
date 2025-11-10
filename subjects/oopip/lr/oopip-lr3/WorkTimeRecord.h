#ifndef WORKTIMERECORD_H
#define WORKTIMERECORD_H

#include <iostream>
#include <string>
#include <iomanip>

class WorkTimeRecord
{
private:
    int employeeId;
    std::string date;
    double hoursWorked;
    std::string taskDescription;

public:
    WorkTimeRecord();
    WorkTimeRecord(int empId, const std::string &date, double hours, const std::string &task);

    int getEmployeeId() const;
    std::string getDate() const;
    double getHoursWorked() const;
    std::string getTaskDescription() const;

    void setEmployeeId(int id);
    void setDate(const std::string &date);
    void setHoursWorked(double hours);
    void setTaskDescription(const std::string &task);

    void displayRecord() const;
    void inputRecord();

    friend std::ostream &operator<<(std::ostream &os, const WorkTimeRecord &record);
    friend std::istream &operator>>(std::istream &is, WorkTimeRecord &record);
};

#endif
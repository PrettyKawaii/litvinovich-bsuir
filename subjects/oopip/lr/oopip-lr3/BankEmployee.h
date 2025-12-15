#ifndef BANKEMPLOYEE_H
#define BANKEMPLOYEE_H

#include <iostream>
#include <string>
#include <iomanip>

class BankEmployee
{
protected:
    std::string name;
    std::string position;
    int employeeId;
    double salary;

public:
    BankEmployee();
    BankEmployee(const std::string &name, const std::string &position,
                 int employeeId, double salary);
    virtual ~BankEmployee();

    std::string getName() const;
    std::string getPosition() const;
    int getEmployeeId() const;
    double getSalary() const;

    void setName(const std::string &name);
    void setPosition(const std::string &position);
    void setEmployeeId(int id);
    void setSalary(double salary);

    virtual void displayInfo() const;
    virtual void inputInfo();

    friend std::ostream &operator<<(std::ostream &os, const BankEmployee &emp);
    friend std::istream &operator>>(std::istream &is, BankEmployee &emp);
};

#endif
#include <iostream>
#include <iomanip>
#include <vector>
#include <string>
#include <algorithm>
#include <limits>
#include <stdexcept>

using namespace std;

// Простая реализация pretty-вывода (аналог библиотеки pretty)
class Pretty
{
public:
    static void printHeader(const string &title)
    {
        cout << "\n"
             << string(60, '=') << endl;
        cout << center(title, 60) << endl;
        cout << string(60, '=') << endl;
    }

    static void printSubHeader(const string &title)
    {
        cout << "\n"
             << string(40, '-') << endl;
        cout << center(title, 40) << endl;
        cout << string(40, '-') << endl;
    }

    static string center(const string &text, int width)
    {
        if (text.length() >= width)
            return text;
        int padding = (width - text.length()) / 2;
        return string(padding, ' ') + text + string(width - text.length() - padding, ' ');
    }

    static void printMenu(const vector<string> &options)
    {
        cout << "\n"
             << string(40, '=') << endl;
        for (size_t i = 0; i < options.size(); ++i)
        {
            cout << " " << i + 1 << ". " << left << setw(35) << options[i] << endl;
        }
        cout << string(40, '=') << endl;
        cout << "Выберите опцию: ";
    }

    static void printSuccess(const string &message)
    {
        cout << "Успех. " << message << endl;
    }

    static void printError(const string &message)
    {
        cout << "Ошибка. " << message << endl;
    }

    static void printInfo(const string &message)
    {
        cout << "Информация. " << message << endl;
    }
};

class Employee
{
protected:
    string name;
    string position;
    int experience;

public:
    Employee(string n, string p, int e) : name(n), position(p), experience(e) {}
    virtual ~Employee() {}
    virtual void display() const
    {
        cout << left << setw(20) << name << setw(15) << position << setw(10) << experience;
    }
    string getName() const { return name; }
    string getPosition() const { return position; }
    int getExperience() const { return experience; }
    virtual string getSpecialization() const = 0;
};

class Electrician : public Employee
{
public:
    Electrician(string n, int e) : Employee(n, "Электрик", e) {}
    string getSpecialization() const override { return "электрика"; }
};

class Plumber : public Employee
{
public:
    Plumber(string n, int e) : Employee(n, "Сантехник", e) {}
    string getSpecialization() const override { return "сантехника"; }
};

class Janitor : public Employee
{
public:
    Janitor(string n, int e) : Employee(n, "Дворник", e) {}
    string getSpecialization() const override { return "уборка"; }
};

class Territory
{
private:
    string address;
    string type;
    vector<string> requiredWorks;

public:
    Territory(string a, string t, vector<string> works) : address(a), type(t), requiredWorks(works) {}

    void display() const
    {
        cout << left << setw(25) << address << setw(15) << type;
        cout << "[";
        for (size_t i = 0; i < requiredWorks.size(); ++i)
        {
            cout << requiredWorks[i];
            if (i != requiredWorks.size() - 1)
                cout << ", ";
        }
        cout << "]";
    }

    string getAddress() const { return address; }
    vector<string> getRequiredWorks() const { return requiredWorks; }
};

class Brigade
{
private:
    vector<Employee *> members;
    Territory *territory;
    string dispatchTime;

public:
    Brigade(Territory *t, string time) : territory(t), dispatchTime(time) {}

    void addMember(Employee *emp)
    {
        members.push_back(emp);
    }

    bool isEmpty() const
    {
        return members.empty();
    }

    void display() const
    {
        Pretty::printHeader("БРИГАДА: " + territory->getAddress());
        cout << "Время выезда: " << dispatchTime << endl;
        cout << "Количество сотрудников: " << members.size() << endl;
        cout << string(60, '-') << endl;
        cout << left << setw(20) << "ФИО" << setw(15) << "Должность" << setw(10) << "Стаж" << setw(15) << "Специализация" << endl;
        cout << string(60, '-') << endl;

        for (const auto &member : members)
        {
            member->display();
            cout << setw(15) << member->getSpecialization() << endl;
        }
    }
};

class HousingService
{
private:
    vector<Employee *> employees;
    vector<Territory *> territories;
    vector<Brigade *> brigades;

public:
    ~HousingService()
    {
        for (auto emp : employees)
            delete emp;
        for (auto ter : territories)
            delete ter;
        for (auto brig : brigades)
            delete brig;
    }

    void addEmployee(Employee *emp)
    {
        employees.push_back(emp);
    }

    void addTerritory(Territory *ter)
    {
        territories.push_back(ter);
    }

    void displayAllEmployees()
    {
        Pretty::printHeader("СПИСОК СОТРУДНИКОВ");
        cout << left << setw(5) << "ID" << setw(20) << "ФИО" << setw(15) << "Должность" << setw(10) << "Стаж" << setw(15) << "Специализация" << endl;
        cout << string(65, '-') << endl;

        for (size_t i = 0; i < employees.size(); ++i)
        {
            cout << setw(5) << i + 1;
            employees[i]->display();
            cout << setw(15) << employees[i]->getSpecialization() << endl;
        }
    }

    void displayAllTerritories()
    {
        Pretty::printHeader("СПИСОК ТЕРРИТОРИЙ");
        cout << setw(5) << "ID" << setw(25) << "Адрес" << setw(15) << "Тип" << "Необходимые работы" << endl;
        cout << string(70, '-') << endl;

        for (size_t i = 0; i < territories.size(); ++i)
        {
            cout << setw(5) << i + 1;
            territories[i]->display();
            cout << endl;
        }
    }

    void createBrigade()
    {
        try
        {
            if (territories.empty() || employees.empty())
            {
                throw runtime_error("Недостаточно данных для создания бригады!");
            }

            displayAllTerritories();
            cout << "\nВыберите ID территории: ";
            int terId;
            cin >> terId;

            if (cin.fail() || terId < 1 || terId > (int)territories.size())
            {
                cin.clear();
                cin.ignore(numeric_limits<streamsize>::max(), '\n');
                throw runtime_error("Неверный ID территории!");
            }

            cin.ignore();
            cout << "Введите время выезда: ";
            string time;
            getline(cin, time);

            if (time.empty())
            {
                throw runtime_error("Время выезда не может быть пустым!");
            }

            Brigade *brigade = new Brigade(territories[terId - 1], time);

            Pretty::printSubHeader("ВЫБОР СОТРУДНИКОВ ДЛЯ БРИГАДЫ");
            displayAllEmployees();
            cout << "\nВыберите сотрудников для бригады (введите 0 для завершения):" << endl;

            while (true)
            {
                int empId;
                cout << "ID сотрудника: ";
                cin >> empId;

                if (cin.fail())
                {
                    cin.clear();
                    cin.ignore(numeric_limits<streamsize>::max(), '\n');
                    Pretty::printError("Неверный ввод!");
                    continue;
                }

                if (empId == 0)
                    break;

                if (empId < 1 || empId > (int)employees.size())
                {
                    Pretty::printError("Неверный ID сотрудника!");
                    continue;
                }

                brigade->addMember(employees[empId - 1]);
                Pretty::printSuccess("Сотрудник добавлен в бригаду!");
            }

            if (brigade->isEmpty())
            {
                delete brigade;
                throw runtime_error("Бригада не может быть пустой!");
            }

            brigades.push_back(brigade);
            Pretty::printSuccess("Бригада успешно создана!");
        }
        catch (const exception &e)
        {
            Pretty::printError(e.what());
        }
    }

    void displayBrigades()
    {
        if (brigades.empty())
        {
            Pretty::printInfo("Бригады не созданы!");
            return;
        }

        Pretty::printHeader("ОТЧЕТ ПО БРИГАДАМ ЖИЛИЩНОЙ СЛУЖБЫ");

        for (size_t i = 0; i < brigades.size(); ++i)
        {
            cout << "\n  Бригада #" << i + 1 << endl;
            brigades[i]->display();
            cout << endl;
        }
    }

    void sortEmployeesByExperience()
    {
        sort(employees.begin(), employees.end(),
             [](Employee *a, Employee *b)
             { return a->getExperience() > b->getExperience(); });
        Pretty::printSuccess("Сотрудники отсортированы по стажу!");
    }

    void searchEmployeeByName()
    {
        cin.ignore();
        cout << "Введите имя для поиска: ";
        string searchName;
        getline(cin, searchName);

        bool found = false;
        for (const auto &emp : employees)
        {
            if (emp->getName().find(searchName) != string::npos)
            {
                if (!found)
                {
                    Pretty::printSubHeader("НАЙДЕННЫЕ СОТРУДНИКИ");
                    found = true;
                }
                emp->display();
                cout << setw(15) << emp->getSpecialization() << endl;
            }
        }

        if (!found)
        {
            Pretty::printInfo("Сотрудники не найдены!");
        }
    }
};

void showMainMenu()
{
    vector<string> menuOptions = {
        "Добавить сотрудника",
        "Добавить территорию",
        "Показать всех сотрудников",
        "Показать все территории",
        "Создать бригаду",
        "Показать все бригады",
        "Отсортировать сотрудников по стажу",
        "Поиск сотрудника по имени",
        "Выход из программы"};
    Pretty::printMenu(menuOptions);
}

int main()
{
    try
    {

        HousingService service;

        // Добавляем тестовые данные
        service.addEmployee(new Electrician("Иванов И.И.", 5));
        service.addEmployee(new Plumber("Петров П.П.", 3));
        service.addEmployee(new Janitor("Сидоров С.С.", 2));
        service.addEmployee(new Electrician("Смирнов А.В.", 7));
        service.addEmployee(new Plumber("Козлов Д.М.", 4));

        service.addTerritory(new Territory("ул. Ленина 25", "Жилая", {"электрика", "уборка"}));
        service.addTerritory(new Territory("Центральный парк", "Общественная", {"уборка", "сантехника"}));
        service.addTerritory(new Territory("пр. Мира 10", "Жилая", {"сантехника", "электрика"}));

        Pretty::printHeader("СИСТЕМА УПРАВЛЕНИЯ ЖИЛИЩНОЙ СЛУЖБОЙ");
        Pretty::printInfo("Добро пожаловать! Загружено тестовых данных: ");
        Pretty::printInfo("- Сотрудников: 5");
        Pretty::printInfo("- Территорий: 3");

        while (true)
        {
            showMainMenu();
            int choice;
            cin >> choice;

            if (cin.fail())
            {
                cin.clear();
                cin.ignore(numeric_limits<streamsize>::max(), '\n');
                Pretty::printError("Неверный ввод! Введите число от 1 до 9.");
                continue;
            }

            cin.ignore();

            switch (choice)
            {
            case 1:
            {
                Pretty::printSubHeader("ДОБАВЛЕНИЕ НОВОГО СОТРУДНИКА");
                cout << "Тип сотрудника (1-Электрик, 2-Сантехник, 3-Дворник): ";
                int type;
                cin >> type;
                cin.ignore();

                cout << "ФИО: ";
                string name;
                getline(cin, name);

                if (name.empty())
                {
                    Pretty::printError("ФИО не может быть пустым!");
                    break;
                }

                cout << "Стаж: ";
                int exp;
                cin >> exp;

                if (cin.good() && exp >= 0)
                {
                    Employee *emp = nullptr;
                    switch (type)
                    {
                    case 1:
                        emp = new Electrician(name, exp);
                        break;
                    case 2:
                        emp = new Plumber(name, exp);
                        break;
                    case 3:
                        emp = new Janitor(name, exp);
                        break;
                    default:
                        Pretty::printError("Неверный тип!");
                    }
                    if (emp)
                    {
                        service.addEmployee(emp);
                        Pretty::printSuccess("Сотрудник успешно добавлен!");
                    }
                }
                else
                {
                    cin.clear();
                    cin.ignore(numeric_limits<streamsize>::max(), '\n');
                    Pretty::printError("Неверный стаж!");
                }
                break;
            }
            case 2:
            {
                Pretty::printSubHeader("ДОБАВЛЕНИЕ НОВОЙ ТЕРРИТОРИИ");
                cout << "Адрес: ";
                string address;
                getline(cin, address);

                if (address.empty())
                {
                    Pretty::printError("Адрес не может быть пустым!");
                    break;
                }

                cout << "Тип: ";
                string type;
                getline(cin, type);

                cout << "Необходимые работы (через запятую): ";
                string worksStr;
                getline(cin, worksStr);

                vector<string> works;
                size_t pos = 0;
                while ((pos = worksStr.find(',')) != string::npos)
                {
                    works.push_back(worksStr.substr(0, pos));
                    worksStr.erase(0, pos + 1);
                }
                works.push_back(worksStr);

                service.addTerritory(new Territory(address, type, works));
                Pretty::printSuccess("Территория успешно добавлена!");
                break;
            }
            case 3:
                service.displayAllEmployees();
                break;
            case 4:
                service.displayAllTerritories();
                break;
            case 5:
                service.createBrigade();
                break;
            case 6:
                service.displayBrigades();
                break;
            case 7:
                service.sortEmployeesByExperience();
                break;
            case 8:
                service.searchEmployeeByName();
                break;
            case 9:
                Pretty::printSuccess("Выход из программы... До свидания!");
                return 0;
            default:
                Pretty::printError("Неверная опция! Выберите от 1 до 9.");
            }
        }
    }
    catch (const exception &e)
    {
        Pretty::printError("Критическая ошибка: " + string(e.what()));
        return 1;
    }

    return 0;
}
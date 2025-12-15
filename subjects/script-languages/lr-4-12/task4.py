class BankAccount:
    bank_name = "Беларусбанк"
    private_var = 100000


    def __init__(self, owner, balance=0):
        self.owner = owner
        self.__balance = balance
    
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Унесена {amount} руб. Новы баланс: {self.__balance} руб.")
        else:
            print("Сума павінна быць дадатнай")
    
    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Знята {amount} руб. Новы баланс: {self.__balance} руб.")
        else:
            print("Недастаткова сродкаў")
    
    def get_balance(self):
        return self.__balance
    
    @classmethod
    def change_bank_name(cls, new_name):
        cls.bank_name = new_name
        print(f"Назва банка зменена на: {new_name}")
    
    @staticmethod
    def validate_account_number(number):
        return len(str(number)) == 20 and str(number).isdigit()
    
    def transfer(self, other_account, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            other_account.__balance += amount
            print(f"Пераведзена {amount} руб. на рахунак {other_account.owner}")
        else:
            print("Недастаткова сродкаў для перакладу")

def main():

    

    print(f"Банк: {BankAccount.bank_name}")
    
    account1 = BankAccount("Іван Іваноў", 1000)
    account2 = BankAccount("Пётр Пятроў", 500)

    print("Прыватная пераменная: ", account1.private_var)
    
    account1.deposit(300)
    account1.withdraw(200)
    account2.deposit(100)
    
    print(f"Баланс рахунка {account1.owner}: {account1.get_balance()} руб.")
    
    account1.transfer(account2, 150)
    print(f"Баланс рахунка {account2.owner}: {account2.get_balance()} руб.")
    
    BankAccount.change_bank_name("Белаграпрамбанк")
    
    account_number = "12345678901234567890"
    print(f"Нумар рахунка {account_number} карэктны: {BankAccount.validate_account_number(account_number)}")

if __name__ == "__main__":
    main()
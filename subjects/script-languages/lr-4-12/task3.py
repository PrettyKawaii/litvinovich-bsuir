class Stationery:
    def __init__(self, title):
        self.title = title
    
    def draw(self):
        print("Запуск адмалёўкі")

class Pen(Stationery):
    def draw(self):
        print(f"Ручка {self.title} піша сінім чарнілам")

class Pencil(Stationery):
    def draw(self):
        print(f"Аловак {self.title} рысуе шэрыя лініі")

class Handle(Stationery):
    def draw(self):
        print(f"Маркер {self.title} зафарбоўвае яркім колерам")

def main():
    pen = Pen("Parker")
    pencil = Pencil("Koh-i-Noor")
    handle = Handle("Edding")
    
    pen.draw()
    pencil.draw()
    handle.draw()

if __name__ == "__main__":
    main()
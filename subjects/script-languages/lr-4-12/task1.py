'''Создать класс String (строка). Разработать в классе методы для работы со
строками (не менее 5).'''
import sys
import importlib
sys.path.append('subjects/script-languages')

import functions as f
from functions import print_full_width_line as line
f = importlib.reload(f)

class String:
    def __init__ (self, text=""):
        self.text = str(text)
        self.length = len(self.text)
        self.language = "unkown"
    def reverse(self):
        return self.text[::-1]
    def count_words(self):
        return len(f.get_words(self.text))
    def get_list_words(self):
        return f.get_words(self.text)
    
    def get_stats(self):
    
        vowels = sum(1 for char in self.text.lower() if char in 'aeiouyаеёіуюяи')
        consonants = sum(1 for char in self.text.lower() if char.isalpha() and char not in 'aeiouyаеёіуюяи')
        digits = sum(1 for char in self.text if char.isdigit())
        return {"vowels": vowels, "consonants": consonants, "digits": digits}

    def most_common_char(self):
        """Самы часта сустракаемы сімвал"""
        from collections import Counter
        if not self.text:
            return None
        return Counter(self.text.replace(" ", "")).most_common(1)[0]

line()
f.print_task_start(1)
line()

def string_menu():
    # f.clear_terminal()
    print()
    line()
    print()
    print('''Меню класа String
1. Стварыць новы радок
2. Праглядзець бягучы радок
3. Змяніць радок
4. Выканаць аперацыі
5. Выдаліць радок
0. Выйсці''')
    return int(input("Выберыце опцыю: "))

def operations_menu(string_obj):
    # f.clear_terminal()
    print()
    line()
    print()
    print(f'''Аперацыі з радком: "{string_obj.text}"
1. Перавернуць радок
2. Падлічыць колькасць слоў
3. Спіс слоў
4. Статыстыка
5. Самы часты сімвал
6. Вярнуцца ў галоўнае меню''')
    return int(input("Выберыце опцыю: "))

def main():
    # f.press_key()
    current_string = None
    
    while True:
        choice = string_menu()
        
        if choice == 1:
            text = input("Увядзіце радок: ")
            current_string = String(text)
            print(f"Створаны новы радок: {current_string.text}")
            
        elif choice == 2:
            if current_string:
                print(f"Бягучы радок: {current_string.text}")
                print(f"Даўжыня: {current_string.length} сімвалаў")
            else:
                print("Радок яшчэ не створаны")
                
        elif choice == 3:
            if current_string:
                new_text = input("Увядзіце новы радок: ")
                current_string.text = new_text
                current_string.length = len(new_text)
                print(f"Радок абноўлены: {current_string}")
            else:
                print("Спачатку стварыце радок")
                
        elif choice == 4:
            if current_string:
                while True:
                    op_choice = operations_menu(current_string)
                    
                    if op_choice == 1:
                        reversed_text = current_string.reverse()
                        print(f"Перавернуты радок: {reversed_text}")
                        
                    elif op_choice == 2:
                        word_count = current_string.count_words()
                        print(f"Колькасць слоў: {word_count}")
                        
                    elif op_choice == 3:
                        words = current_string.get_list_words()
                        print(f"Спіс слоў: {words}")
                        
                    elif op_choice == 4:
                        stats = current_string.get_stats()
                        print(f"Статыстыка:")
                        print(f"Галосныя: {stats['vowels']}")
                        print(f"Зычныя: {stats['consonants']}")
                        print(f"Лічбы: {stats['digits']}")
                        
                    elif op_choice == 5:
                        common_char = current_string.most_common_char()
                        if common_char:
                            char, count = common_char
                            print(f"Самы часты сімвал: '{char}' ({count} разоў)")
                        else:
                            print("Радок пусты")
                            
                    elif op_choice == 6:
                        break
                    else:
                        print("Невядомая опцыя")
            else:
                print("Спачатку стварыце радок")
                
        elif choice == 5:
            if current_string:
                confirm = input(f"Вы ўпэўнены, што хочаце выдаліць радок '{current_string.text}'? (y/n): ")
                if confirm.lower() == 'y':
                    current_string = None
                    print("Радок выдалены")
            else:
                print("Няма радка для выдалення")
                
        elif choice == 0:
            print("Да пабачэння")
            break
            
        else:
            print("Невядомая опцыя")


main()
line()
f.print_task_end(1)
line()
f.press_key()
f.clear_terminal()
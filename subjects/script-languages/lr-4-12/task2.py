import string

class Alphabet:
    def __init__(self, lang, letters):
        self.lang = lang
        self.letters = list(letters)
    
    def print(self):
        print(f"Літары алфавіта {self.lang}: {''.join(self.letters)}")
    
    def letters_num(self):
        return len(self.letters)

class EngAlphabet(Alphabet):
    __letters_num = 26
    
    def __init__(self):
        super().__init__('En', string.ascii_uppercase)
    
    def is_en_letter(self, letter):
        return letter.upper() in self.letters
    
    def letters_num(self):
        return self.__letters_num
    
    @staticmethod
    def example():
        return "The quick brown fox jumps over the lazy dog"

def main():
    alphabet = Alphabet("Беларускі", "АБВГД")
    alphabet.print()
    print(f"Колькасць літар: {alphabet.letters_num()}")
    
    eng = EngAlphabet()
    eng.print()
    print(f"Колькасць літар: {eng.letters_num()}")
    print(f"'A' - англійская літара: {eng.is_en_letter('A')}")
    print(f"'Ў' - англійская літара: {eng.is_en_letter('Ў')}")
    print(f"Прыклад тэксту: {EngAlphabet.example()}")

def get_words(line):
    punct_table = str.maketrans({char: " " for char in ['.', ',', '?', '!']})
    words = line.translate(punct_table).split()
    return words



import random

class RandomWord:
    def __init__(self, filename):
        self.filename = filename


    def read_text(self):
        try:
            with open(self.filename, 'r', encoding='utf-8') as f:
                text = [line.strip() for line in f.readlines()]
                text = list(filter(lambda x: len(x) > 3, text))

            random_word = text[random.randint(0, len(text)-1)]

            text.remove(random_word)

            with open(self.filename, 'w', encoding='utf-8') as f:
                f.write("\n".join(text))

            return random_word
        except:
            print('В файле нет текста или файл не найден')














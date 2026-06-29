


import random

class RandomWord:
    def __init__(self, filename):
        self.filename = filename


    def read_text(self):
        with open(self.filename, 'r', encoding='utf-8') as f:
            text = [line.strip() for line in f.readlines()]
            text = list(filter(lambda x: len(x) > 3, text))

        random_word = text[random.randint(0, len(text)-1)]

        return random_word















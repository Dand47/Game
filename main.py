from random_slovo import RandomWord
from start_end import Start
from visual import visual




class Game(Start, RandomWord):


    def __init__(self):
        self.filename = 'text.txt'
        self.wins = 0
        self.lose = 0
        self.hp = 5
        self.main_words = 'Минато'
        self.user_words = []


    def setup_game(self):
        self.hp = 5

        try:
            self.main_words = self.read_text()
            self.user_words = ['*'] * len(self.main_words)
        except:
            print('возникла ошибка в setup_game')


    @staticmethod
    def get_input():
        return input("Введите букву ").lower().strip()


    def main_game(self, words):
        for i in range(len(self.main_words)):
             if self.main_words[i].lower() == words:
                 self.user_words[i] = self.main_words[i]

        print(f"Правильно: {self.user_words}")


    def lose_hp(self):
        self.hp -= 1
        print(f'Неправильно: текущее здоровье {self.hp}')
        visual(self.hp)


    def check_input(self, user_input):

        if not user_input.isalpha():
            print('Нужно вводить букву!')
            return

        elif user_input in self.user_words:
            print(f"Вы уже вводили эту букву!")
            return


        elif len(user_input) > 1:
            print('Нужно ввести 1 букву!')
            return

        elif user_input in self.main_words.lower():
            self.main_game(user_input)
            return

        else:
            self.lose_hp()


    def check_win(self):
        return "".join(self.user_words) == self.main_words


    def check_lose(self):
        return self.hp <= 0


    def game_start(self):
        self.setup_game()

        while True:
            user_input = self.get_input()
            self.check_input(user_input)

            if self.check_win():
                self.wins += 1
                print(f"Победа!: побед {self.wins}")
                break

            if self.check_lose():
                self.lose += 1
                print(f"Поражение: поражений {self.lose}")
                break



if __name__ == '__main__':
    game = Game()
    game.hello()

    while True:

        if game.game_start_or_end() != 'y':
            break
        game.game_start()
        if game.end() != 'y':
            break

































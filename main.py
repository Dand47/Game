from random_word import RandomWord
from start_end import Start
from visual import visual




class Game:

    def __init__(self):
        self.start = Start()
        self.random_word = RandomWord(filename='text.txt')


        self.wins = 0
        self.lose = 0
        self.hp = 5
        self.secret_words = 'минато'
        self.user_input = []


    def setup_game(self):
        try:
            self.hp = 5
            self.secret_words = self.random_word.read_text()
            self.user_input = ['*'] * len(self.secret_words)
            return True
        except (TypeError, ValueError, IndexError, FileNotFoundError):
            print('Ошибка в setup_game')
            return False


    @staticmethod
    def get_input():
        return input("Введите букву ").lower().strip()


    def main_game(self, words):
        for i in range(len(self.secret_words)):
             if self.secret_words[i].lower() == words:
                 self.user_input[i] = self.secret_words[i]

        print(f"Правильно: {self.user_input}")


    def lose_hp(self):
        self.hp -= 1
        print(f'Неправильно: текущее здоровье {self.hp}')
        visual(self.hp)


    def check_input(self, user_input):

        if not user_input.isalpha():
            print('Нужно вводить букву!')
            return

        elif len(user_input) > 1:
            print('Нужно ввести 1 букву!')
            return

        elif user_input in self.user_input:
            print(f"Вы уже вводили эту букву!")
            return


        elif user_input in self.secret_words.lower():
            self.main_game(user_input)
            return

        else:
            self.lose_hp()


    def check_win(self):
        return "".join(self.user_input).lower() == self.secret_words.lower()


    def check_lose(self):
        return self.hp <= 0


    def game_start(self):
        if self.setup_game():
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
    game.start.hello()

    while True:
        if game.start.game_start_end() != 'y':
             break
        game.game_start()





class Start:
    def hello(self):
        print(f"Добро пожаловать в висилицу")
        print("""
      ________
     |       |
     |       O
     |      /|\\
     |      / \\
     |
_____|_____
        """)


    def game_start_or_end(self):
        return input("Желаете начать новую игру или выйти из приложения? y/n ").lower().strip()

    def end(self):
        return input("Конец игры хотите продолжить игру? y/n ").lower().strip()





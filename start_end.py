



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


    def game_start_end(self):
        return input("Конец игры, желаете начать новую игру или выйти из приложения? y/n ").lower().strip()




import random
from decouple import config


class CasinoGame:
    def __init__(self):
        self.money = int(config('MY_MONEY'))

    def start_game(self):
        while True:
            print(f"У тебя: ${self.money}")
            bet = int(input("Сделай ставку на число от 1 до 10: "))

            winning_number = random.randint(1, 10)
            if bet == winning_number:
                self.money += 1
                print(f"Ты выйграл ${bet}")
            else:
                self.money -= bet * 100
                print(f"Ты програл ${bet * 100}")

            play_again = input("Ты хочешь сыграть ещё? (y/n): ")
            if play_again.lower() != 'y':
                break

        print(f"У тебя сейчас: ${self.money}")
        if self.money > int(config('MY_MONEY')):
            print("Ты в плюсе")
        elif self.money < int(config('MY_MONEY')):
            print("Ты в минусе")
        else:
            print("[ДАННЫЕ УДАЛЕНЫ] этого казино [ДАННЫЕ УДАЛЕНЫ], ты чё бредешь [ДАННЫЕ УДАЛЕНЫ]")

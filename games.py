import random
import itertools

class Player:

    def __init__(self, money):
        self.start_money = money
        self.current_money = money

    def flip_coin(self):
        sides = ["Heads", "Tails"]
        side = choose_menu(sides, "Choose Side")
        bet = self.bet(self.current_money)
        case = random.choice(sides)
        win = 2*bet if case == side else 0
        print(f"\nYour bet: {side} - {bet}")
        print(f"{case} is showing")
        self.game_result(win - bet)

    def cho_han(self):
        var = choose_menu(["Even", "Odd"], "Choose Even or Odd")
        bet = self.bet(self.current_money)
        dice = random.choices(range(1, 7), k=2)
        case = "Even" if sum(dice) % 2 == 0 else "Odd"
        win = 2*bet if case == var else 0
        print(f"\nYour bet: {var} - {bet}")
        print(f"{dice[0]} and {dice[1]} are showing. Sum is {case}")
        self.game_result(win - bet)

    def cards(self):
        bet = self.bet(self.current_money)
        suit = list(range(2, 11)) + ["Jack", "Queen", "King", "Ace"]
        deck = set(itertools.product(suit, ("♠", "♥", "♦", "♣")))
        values = {name: score for score, name in enumerate(suit)}
        cs = random.sample(deck, 2)
        if values[cs[0][0]] > values[cs[1][0]]:
            win = 2*bet
        elif values[cs[0][0]] < values[cs[1][0]]:
            win = 0
        else:
            win = bet
        print(f"\nYour bet: {bet}")
        print(f'You have "{cs[0][0]} of {cs[0][1]}" vs "{cs[1][0]} of {cs[1][1]}"')
        self.game_result(win - bet)

    def roulette(self):
        choices = []
        bets = []
        even_black = [i for i in list(range(1, 11)) + list(range(19, 29)) if i % 2 == 0]
        odd_black = [i for i in list(range(11, 19)) + list(range(29, 37)) if i % 2 == 1]
        black = even_black + odd_black
        red = [i for i in range(1, 37) if i not in black]
        while self.current_money > sum(bets):
            if len(choices) > 0:
                choice = choose_menu(["Add a bet", "Play"], "Choose action")
                if choice == "Play":
                    break
            bet_type = choose_menu(["Number", "Even or Odd", "Color"], "Choose bet type")
            if bet_type == "Number":
                choices.append(get_positive("Choose Number between 1 and 36 ", 36))
            elif bet_type == "Even or Odd":
                choices.append(choose_menu(["Even", "Odd"], "Choose Even or Odd"))
            elif bet_type == "Color":
                print("Black: " + ", ".join(map(str, black)))
                print("Red: " + ", ".join(map(str, red)))
                choices.append(choose_menu(["Black", "Red"], "Choose Color"))
            bets.append(self.bet(self.current_money - sum(bets)))
        ntype = lambda x: "Even" if x % 2 == 0 else "Odd"
        color = lambda x: "Black" if x in black else "Red"
        wheel = [(i, ntype(i), color(i)) for i in range(1, 37)] + [("0","",""),("00","","")]
        num = random.choice(wheel)
        coef = (36, 2, 2)
        win = 0
        print("\nYour bets:")
        for choice, bet in zip(choices, bets):
            print(f"{choice} - {bet}")
            for i in range(3):
                if choice == num[i]:
                    win += bet*coef[i]
        print(f"The ball is in slot: {num[0]} {num[1]} {num[2]}")
        self.game_result(win - sum(bets))

    @staticmethod
    def bet(money):
        print(f"You have {money} coins")
        return get_positive("What is your bet? ", money)

    def game_result(self, diff):
        if diff > 0:
            print(f"You won {diff} coins")
        elif diff < 0:
            print(f"You lost {-diff} coins")
        else:
            print("You broke even")
        self.current_money += diff
        print(f"You have {self.current_money} coins")

    def exit(self):
        diff = self.current_money - self.start_money
        if diff > 0:
            print(f"It was a lucky day. You won {diff} coins")
        elif diff < 0:
            print(f"It was an unlucky day. You lost {-diff} coins")
        else:
            print("You broke even")
        print(f"You leave Greedy Goblin Casino having {self.current_money} coins")

def casino():
    print("Welcome to Greedy Goblin Casino!")
    player = Player(get_positive("How many coins do you have? "))
    casino_list = ["Flip Coin", "Cho-Han", "Cards", "Roulette", "Exit Casino"]
    choice = None
    while True:
        choice = choose_menu(casino_list, "Choose a game")
        if choice == "Flip Coin":
            player.flip_coin()
        elif choice == "Cho-Han":
            player.cho_han()
        elif choice == "Cards":
            player.cards()
        elif choice == "Roulette":
            player.roulette()
        if choice == "Exit Casino" or player.current_money == 0:
            player.exit()
            break

def get_positive(text, max=float('inf')):
    while True:
        try:
            user_input = int(input(text))
            if user_input <= 0:
                raise Error
            elif user_input > max:
                print(f"Input integer not exceeding {max}")
            else:
                return user_input
        except:
            print("Input positive integer")

def choose_menu(lst, title):
    print(f"\n{title}")
    for item in enumerate(lst):
        print(f"{item[0]} - {item[1]}")
    while True:
        choice = input("Number of your choice: ")
        if choice in map(str, range(len(lst))):
            return lst[int(choice)]

casino()

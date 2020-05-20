import random
import itertools

def choose_from_list(lst, title, menu=True):
    print(f'\n{title}')
    chosen = None
    if menu:
        for i in enumerate(lst):
            print(f'{i[0]} - {i[1]}')
        while not chosen in [str(i) for i in range(len(lst))]:
            chosen = input('Number of your choice: ')
        chosen = lst[int(chosen)]
    else:
        while not chosen in lst:
            chosen = input('Your choice: ').title()
    return chosen

def make_bet(money):
    while True:
        bet = input(f'Make your bet more than 0 and not more than {money}: ')
        try:
            if 0 < int(bet) <= money:
                return int(bet)
        except:
            pass

def flip_coin(side, bet):
    case = random.choice(['Heads', 'Tails'])
    result = ('won', 1) if case == side else ('lost', -1)
    print(f'{case} is showing')
    print(f'You {result[0]} {bet}')
    return bet*result[1]

def cho_han(side, bet):
    dice = random.choices(range(1, 7), k=2)
    case = 'Even' if sum(dice) % 2 == 0 else 'Odd'
    result = ('won', 1) if case == side else ('lost', -1)
    print(f'{dice[0]} and {dice[1]} are showing. Sum is {case}')
    print(f'You {result[0]} {bet}')
    return bet*result[1]

def cards(bet):
    suit = list(range(2, 11)) + ['Jack', 'Queen', 'King', 'Ace']
    deck = set(itertools.product(suit, ('♠', '♥', '♦', '♣')))
    values = {name: score for score, name in enumerate(suit)}
    cards = random.sample(deck, 2)
    if values[cards[0][0]] > values[cards[1][0]]:
        result = (f'You won {bet}', 1)
    elif values[cards[0][0]] < values[cards[1][0]]:
        result = (f'You lost {bet}', -1)
    else:
        result = ('It is tie', 0)
    print(f'You have "{cards[0][0]} of {cards[0][1]}" vs "{cards[1][0]} of {cards[1][1]}"')
    print(result[0])
    return bet*result[1]

def roulette(choice, bet):
    type = lambda i: 'Even' if i % 2 == 0 else 'Odd'
    wheel = [(str(i), type(i)) for i in range(1, 37)] + [('0', ''), ('00', '')]
    num = random.choice(wheel)
    if num[0] == choice:
        result = ('won', 35)
    elif num[1] == choice:
        result = ('won', 1)
    else:
        result = ('lost', -1)
    print(f'{num[0]} is showing')
    print(f'You {result[0]} {abs(result[1]*bet)}')
    return bet*result[1]

def games():
    money = 100
    choice = None
    menu = ['Flip Coin', 'Cho-Han', 'Cards', 'Roulette', 'Exit' ]
    while choice != 'Exit':
        print(f'You have {money} money')
        choice = choose_from_list(menu, 'Games of Chance')
        bet = make_bet(money)
        if choice == 'Flip Coin':
            money += flip_coin(choose_from_list(['Heads', 'Tails'], 'Choose side'), bet)
        elif choice == 'Cho-Han':
            money += cho_han(choose_from_list(['Even', 'Odd'], 'Choose Even/Odd'), bet)
        elif choice == 'Cards':
            money += cards(bet)
        elif choice == 'Roulette':
            roulette_list = [str(i) for i in range(1, 37)] + ['Even', 'Odd']
            roulette_text = 'Choose number from 1 to 36 or "Even" or "Odd"'
            money += roulette(choose_from_list(roulette_list, roulette_text, menu=False), bet)
        if money == 0:
            print('You lost all your money')
            break

games()

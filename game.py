import random


suits = ('Черви', 'Бубы', 'Крести', 'Пики')
names = ('Двойка', 'Тройка', 'Четвёрка', 'Пятёрка', 'Шестёрка', 'Семёрка', 'Восьмёрка', 'Девятка', 'Десятка', 'Валет',
         'Дама', 'Король', 'Туз')
values = {'Двойка': 2, 'Тройка': 3, 'Четвёрка': 4, 'Пятёрка': 5, 'Шестёрка': 6, 'Семёрка': 7, 'Восьмёрка': 8,
          'Девятка': 9, 'Десятка': 10, 'Валет': 10, 'Дама': 10, 'Король': 10, 'Туз': 11}

playing = True

class Card():

    def __init__(self, suit, name):
        self.suit = suit
        self.name = name

    def __str__(self):
        return f"{self.name} {self.suit}"

class Desk():

    def __init__(self):
        self.deck = []
        for suit in suits:
            for name in names:
                self.deck.append(Card(suit, name))

    def __str__(self):
        str_deck = ''
        count = 1
        for card in self.deck:
            str_deck += str(count) + ' ' + str(card) + '\n'
            count += 1
        return str_deck

    def shuffle(self):
        random.shuffle(self.deck)

    def give_card(self):
        card = self.deck.pop()
        return card

class Hand():

    def __init__(self):
        self.hand = []
        self.value = 0
        self.aces = 0
        self.aces_dict = []

    def __str__(self):
        str_hand = ''
        count = 1
        for card in self.hand:
            str_hand += str(count) + ' ' + str(card) + '\n'
            count += 1
        return str_hand

    def take_one_card(self, deck):
        card = deck.give_card()
        self.hand.append(card)
        self.value += values[card.name]
        return self

    def add_aces(self):
        for card in self.hand:
            if card.name == 'Туз' and card not in self.aces_dict:
                self.aces_dict.append(card)
                self.aces += 1
        while self.value > 21 and self.aces > 0:
            self.aces -= 1
            self.value -= 10
        if self.value > 21:
            self.value = 99
class Chips():

    def __init__(self, balance=1000, bet=0):
        self.balance = balance
        self.bet = bet

    def __str__(self):
        return f'Текущий баланс: {self.balance}\n' \
               f'Текущая ставка: {self.bet}'

    def pay_money(self):
        while True:
            try:
                self.balance = int(input('Сколько денег вы хотите внести для игры: '))
                if self.balance < 0:
                    print('Вы ввели отрицательное значение!')
                    continue
            except:
                print('Вы ввели не число!')
                continue
            else:
                print(f'Ваш баланс: {self.balance}')
                break

    def make_bet(self):
        while True:
            try:
                self.bet = int(input('Какая у вас ставка:'))
            except ValueError:
                print('Похоже вы ввели не целое числовое значение, попробуйте ещё раз')
                continue
            if self.bet > self.balance:
                print(f'У вас нет столько денег!, у вас только {self.balance}')
                continue
            elif self.bet <= 0:
                print(f'Вы ввели невозможное значение!\nВаш баланс: {self.balance}')
                continue
            else:
                self.balance -= self.bet
                print('Ставка сделана!')
                print(self)
                break



if __name__ == "__main__":
    game = Desk()
    game.shuffle()
    print(game)
    print(game.give_card())
    hand = Hand()
    hand.take_one_card(game)
    hand.take_one_card(game)
    hand.take_one_card(game)
    print(hand.value)
    hand.add_aces()
    print(hand.value)
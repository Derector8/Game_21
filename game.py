import random
import logging_hw
from logging_hw import logger_1


#dictConfig(config_dict.LOGGING)
#logger_1 = logging.getLogger('my_logging_hw')


suits = ('Черви', 'Бубы', 'Крести', 'Пики')
names = ('Двойка', 'Тройка', 'Четвёрка', 'Пятёрка', 'Шестёрка', 'Семёрка', 'Восьмёрка', 'Девятка', 'Десятка', 'Валет',
         'Дама', 'Король', 'Туз')
values = {'Двойка': 2, 'Тройка': 3, 'Четвёрка': 4, 'Пятёрка': 5, 'Шестёрка': 6, 'Семёрка': 7, 'Восьмёрка': 8,
          'Девятка': 9, 'Десятка': 10, 'Валет': 10, 'Дама': 10, 'Король': 10, 'Туз': 11}

playing = True


class Card():

    def __init__(self, suit, name):
        logger_1.info("Initializing Card class")
        self.suit = suit
        self.name = name
        logger_1.info("Card class initializing completed")

    def __str__(self):
        return f"{self.name} {self.suit}"


class Desk():

    def __init__(self):
        logger_1.info("Desk class initializing")
        self.deck = []
        for suit in suits:
            for name in names:
                self.deck.append(Card(suit, name))
        logger_1.info("Desk class initializing completed")

    def __str__(self):
        str_deck = ''
        count = 1
        for card in self.deck:
            str_deck += str(count) + ' ' + str(card) + '\n'
            count += 1
        return str_deck

    def shuffle(self):
        random.shuffle(self.deck)
        logger_1.info("Cards are shuffled")

    def give_card(self):
        logger_1.info("Asked to give a card")
        card = self.deck.pop()
        logger_1.info("Card is given")
        return card


class Hand():

    def __init__(self):
        logger_1.info("Hand class initializing")
        self.hand = []
        self.value = 0
        self.aces = 0
        self.aces_dict = []
        logger_1.info("Hand class initializing completed")

    def __str__(self):
        str_hand = ''
        count = 1
        for card in self.hand:
            str_hand += str(count) + ' ' + str(card) + '\n'
            count += 1
        return str_hand

    def take_one_card(self, deck):
        logger_1.info("User asked to take one additional card")
        card = deck.give_card()
        self.hand.append(card)
        self.value += values[card.name]
        logger_1.info("Card is taken")
        return self

    def add_aces(self):
        logger_1.debug("Checking for Aces cost: 1 or 11")
        for card in self.hand:
            if card.name == 'Туз' and card not in self.aces_dict:
                self.aces_dict.append(card)
                self.aces += 1
        while self.value > 21 and self.aces > 0:
            self.aces -= 1
            self.value -= 10
        if self.value > 21:
            self.value = 99
        logger_1.debug("Checking for Aces cost completed")


class Chips():

    def __init__(self, balance=1000, bet=0):
        logger_1.info("Chips class initializing")
        self.balance = balance
        self.bet = bet
        logger_1.info("Chips class initializing completed")

    def __str__(self):
        return f'Текущий баланс: {self.balance}\n' \
               f'Текущая ставка: {self.bet}'

    def pay_money(self):
        logger_1.info("Adding money started")
        while True:
            logger_1.debug("New cycle started")
            try:
                self.balance = int(input('Сколько денег вы хотите внести для игры: '))
                if self.balance < 0:
                    print('Вы ввели отрицательное значение!')
                    continue
            except:
                print('Вы ввели не число!')
                logger_1.warning("User tried to use non-digit value while adding money")
                continue
            else:
                print(f'Ваш баланс: {self.balance}')
                break
        logger_1.info("Adding money ended")

    def make_bet(self):
        logger_1.info("Making bet started")
        while True:
            try:
                self.bet = int(input('Какая у вас ставка:'))
            except ValueError:
                logger_1.warning("User tried to use non-digit value while adding money")
                print('Похоже вы ввели не целое числовое значение, попробуйте ещё раз')
                continue
            if self.bet > self.balance:
                logger_1.warning("User tried to make too big bet")
                print(f'У вас нет столько денег!, у вас только {self.balance}')
                continue
            elif self.bet <= 0:
                logger_1.warning("User tried to make unreachable bet")
                print(f'Вы ввели невозможное значение!\nВаш баланс: {self.balance}')
                continue
            else:
                self.balance -= self.bet
                print('Ставка сделана!')
                print(self)
                logger_1.info("Making bet completed")
                break
        logger_1.info("Ended making bet cycle")


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

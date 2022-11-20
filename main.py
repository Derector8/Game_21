# Это Игра в 21, где нужно набрать 21 или больше дилера, но не более 21, чтобы выиграть ставку
import game
import sys


def initiation():
    chips = game.Chips()
    chips.pay_money()
    return chips


def start_game(chips):
    desk = game.Desk()
    desk.shuffle()
    dealer_hand = game.Hand()
    hand = game.Hand()
    chips.make_bet()
    hand.take_one_card(desk)
    dealer_hand.take_one_card(desk)
    hand.take_one_card(desk)
    dealer_hand.take_one_card(desk)
    print('Рука дилера: \n', dealer_hand.hand[1], '\t')
    print('Ваша рука: \n', hand)
    return desk, hand, chips, dealer_hand


def one_more_game(chips):
    while True:
        if chips.balance == 0:
            print('У вас закончились деньги, всего доброго!')
            return False
        answer = input('Хотите сыграть ещё?\n'
                       ' Д/Н:\t')
        if answer == 'Д':
            return True
        elif answer == 'Н':
            print('Всего доброго!')
            return False
        else:
            print('Непонятный ответ!')
            continue


def take_or_stop(hand, desk):
    while True:
        hand.add_aces()
        answer = input(f'Вы хотите взять ещё?\n'
                       f'В данный момент сумма {hand.value}\n'
                       f'Д/Н:\t')
        if hand.value == 99:
            print('Вы проиграли!')
            return hand, desk
        elif hand.value > 21:
            hand.add_aces()
            if hand.value > 21:
                print('Вы проиграли, у вас перебор!')
                return hand, desk
            continue
        elif hand.value == 21:
            print('21!!!!!')
            return hand, desk
        elif answer == 'Д':
            hand.take_one_card(desk)
            print(hand)
            hand.add_aces()
            if hand.value > 21:
                print('Вы проиграли, у вас перебор!')
                return hand, desk
            continue
        elif answer == 'Н':
            print('Закончили брать')
            return hand, desk
        else:
            print('Непонятный ответ!')
            continue


def dealer(hand, dealer_hand, desk):
    dealer_hand.add_aces()
    while dealer_hand.value < hand.value <= 21:
        dealer_hand.take_one_card(desk)
        dealer_hand.add_aces()
        print(f'Рука Дилера:\n{dealer_hand}\n'
              f'Его очки: {dealer_hand.value}')
    else:
        print(f'Карты дилера: {dealer_hand}')
    return dealer_hand


def end(hand, dealer_hand, chips):
    if hand.value > 21 or hand.value < dealer_hand.value < 21:
        print(f'Вы проиграли {chips.bet}\n'
              f'Теперь у вас {chips.balance} Р')
    elif dealer_hand.value <= hand.value or dealer_hand.value == 99:
        chips.balance += chips.bet * 2
        print(f'ПОБЕДА!!!\n'
              f'Теперь у вас {chips.balance} Р')
    else:
        print(f'Что вообще случилось?\n'
              f'Ваш: {hand.value}\n'
              f'Дилера: {dealer_hand.value}')
    return one_more_game(chips)


if __name__ == '__main__':
    print('Добро пожаловать в 21!')
    while True:
        answer = input('Вы желаете сыграть в игру? Д/Н: ')
        if answer == 'Д':
            print('Отлично, теперь пополните ваш баланс!')
            break
        elif answer == 'Н':
            print('Очень жаль, всего доброго!')
            sys.exit()
        else:
            print('Непонятный ответ!')
            continue

    chips = initiation()

    while game.playing == True:
        desk, hand, chips, dealer_hand = start_game(chips)
        hand, desk = take_or_stop(hand, desk)
        dealer_hand = dealer(hand, dealer_hand, desk)
        game.playing = end(hand, dealer_hand, chips)

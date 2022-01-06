import time
import itertools
import numpy as np


def wait(t):
    time.sleep(t)

def pick_a_card(cards, remove = True, manual = False):
    
    if manual:
        return input('name a card to pick:')
    else:
        suit_pick = list(cards.keys())[np.random.randint(0, 100) % len(cards)]
        card_pick = cards[suit_pick][np.random.randint(0, 100) % len(cards[suit_pick])]
        if remove:
            del cards[suit_pick][cards[suit_pick].index(card_pick)]
            if len(cards[suit_pick]) == 0:
                del cards[suit_pick]
        return suit_pick + '_' + card_pick

def pick_a_card_hard(cards, number_of_points, remove=True, manual=False):
    if manual:
        return input('name a card to pick:')
    else:
        suit_pick = list(cards.keys())[np.random.randint(0, 100) % len(cards)]
        card_pick = cards[suit_pick][np.random.randint(0, 100) % len(cards[suit_pick])]
        keys = list(cards.keys())
        values = list(cards.values())
        for i in range(len(keys)):
            for l in range(len(values[i])):
                if values[i][l] == str(number_of_points):
                    suit_pick = keys[i]
                    card_pick = cards[suit_pick][l]
                    break
            else:
                continue
            break

        if remove:
            del cards[suit_pick][cards[suit_pick].index(card_pick)]
            if len(cards[suit_pick]) == 0:
                del cards[suit_pick]
        return suit_pick + '_' + card_pick

# blackjack
def calc_points(cards, base_val = 21):
    card_values = {'A' : 11, 'J' : 10, 'Q' : 10, 'K' : 10, '2' : 2, '3' : 3, '4' : 4, '5' : 5, '6' : 6, '7' : 7, '8' : 8, '9' : 9, '10' : 10}
    points = 0
    for i in range(len(cards)):
        points += card_values[cards[i].split('_')[-1]]
    return points


def card_inc(card_box, n, cnt, shuffle_point, ndeck):
    if cnt + n >= shuffle_point:
        card_box = {
            'heart' : (['A', 'J', 'Q', 'K'] + ['%d'%i for i in range(2, 11)]) * ndeck, 
            'diamond' : (['A', 'J', 'Q', 'K'] + ['%d'%i for i in range(2, 11)]) * ndeck, 
            'club' : (['A', 'J', 'Q', 'K'] + ['%d'%i for i in range(2, 11)]) * ndeck, 
            'spade' : (['A', 'J', 'Q', 'K'] + ['%d'%i for i in range(2, 11)]) * ndeck
        }
        shuffle_point = np.random.randint((ndeck * 52) // 4, (ndeck * 52 * 3) // 4)
        cnt = n
    else:
        cnt += n
    return card_box, cnt, shuffle_point


class Player:
    pl_cnt = 0
    
    def __init__(self, name=''):
        self.money = 500
        Player.pl_cnt += 1
        self.name = name if name.replace(' ', '') != '' else 'Player-%d'%Player.pl_cnt
    
    def new_session(self, card_box):
        self.bj_state = False
        self.cards = [pick_a_card(card_box, True), pick_a_card(card_box, True)]
        self.points = calc_points(self.cards)
        
    def set_bet(self, lowest_bet, type_of_player):
        if type_of_player =="p":
            self.bet = int(input('fund : %d,   enter the initial bet : '%self.money))
            while True:
                if self.bet < lowest_bet:
                    self.bet = int(input('invalid !!   lowest required bed is : %d, enter the bet again : '%lowest_bet))
                    continue
                if self.bet > self.money:
                    self.bet = int(input('invalid !!   fund : %d, enter the bet again : '%self.money))
                else:
                    self.money -= self.bet
                    break
        else:
            self.bet = self.money
            self.money -= self.bet

    def set_bet_player(self, number):
        self.bet = number
        self.money -= self.bet
        print(self.bet)

    def show_state(self):
        print('your cards : ', self.cards, '\t\t total points : ', self.points)

    def get_stats(self):
        return self.cards

    def check_blackjack(self, base_point):
        if self.points == base_point:
            self.bj_state = True
            print('!!!!!!!! BLACKJACK !!!!!!!!!!')
        return self.bj_state

    def check_A(self):
        numbers = 0
        for i in range(len(self.cards)):
            if self.cards[i].split('_')[-1] == 'A':
                numbers+=1
        return numbers

    
    def hit(self, card_box):
        self.cards += [pick_a_card(card_box, True)]
        self.points = calc_points(self.cards)
        self.show_state()

    def last_card(self):
        return self.cards[len(self.cards)-1]

    def last_card1(self):
        return self.cards[len(self.cards)-2]

    def hit_hard(self, card_box, number_of_points):
        self.cards += [pick_a_card_hard(card_box, number_of_points, True)]
        self.points = calc_points(self.cards)
        self.show_state()
    
    def update_money(self, win_flag):
        if win_flag == 'w':
            if self.bj_state:
                self.money += (1.5 + 1) * self.bet
            else:
                self.money += self.bet * 2
        elif win_flag == 'd':
            self.money += self.bet
        if self.money <= 0:
            self.money = 0


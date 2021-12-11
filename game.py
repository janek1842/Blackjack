from numpy import random

import blackjack
from utils import *

twentyone = 21
lowest_bet = 5
t = 1
yes = ['y', 'yes']
no = ['n', 'no']
numer_of_decks = 3

t0 = time.time()

while True:
    try:
        init_players = int(input('Enter total players : '))
        break
    except ValueError:
        print("Oops!  That was no valid number.  Try again...")
db = blackjack.DataBase
type =[]
players = []
while len(type) != init_players:
    type.append(input('enter type of player ( p - player, e - AI type easy, m - AI type medium, h - AI type hard): '))
    if type[len(type)-1] == "p":
        players.append(Player(input('enter %d player name: '% (len(type)-1 + 1))))
    elif type[len(type)-1] == "e":
        players.append(Player('AI easy'))
    elif type[len(type)-1] == "m":
        players.append(Player('AI medium'))
    elif type[len(type)-1] == "h":
        players.append(Player('AI hard'))
    else:
        print('Try again ')
        type.pop()
type = np.asarray(type)
players = np.asarray(players)

def getPlayerResult(i):
    if(win_state[i]=='w'):
        return True
    elif(win_state[i]=='d'):
        return None
    else:
        return False

def getAmount(i,amount):
    if getPlayerResult(i):
        return amount
    elif not getPlayerResult(i):
        return (-1*amount)
    else:
        return 0

def getCardDictFromList(cardOriginList):
    cardList = []

    for card in cardOriginList:
        if('10' in card):
            cardList.append("10")
        else:
            cardList.append(card[-1:])

    cardDict = {}

    for card in cardList:
        cardDict[card] = cardList.count(card)

    return cardDict

card_box = {
    'heart': (['A', 'J', 'Q', 'K'] + ['%d' % i for i in range(2, 11)]) * numer_of_decks,
    'diamond': (['A', 'J', 'Q', 'K'] + ['%d' % i for i in range(2, 11)]) * numer_of_decks,
    'club': (['A', 'J', 'Q', 'K'] + ['%d' % i for i in range(2, 11)]) * numer_of_decks,
    'spade': (['A', 'J', 'Q', 'K'] + ['%d' % i for i in range(2, 11)]) * numer_of_decks
}
card_cnt = 0
shuffle_point = np.random.randint((numer_of_decks * 52) // 2, numer_of_decks * 52)
number_of_players = len(players)
bjs = [False for i in range(number_of_players)]
left_over = [None for i in range(number_of_players)]
win_state = ['l' for i in range(number_of_players)]

for i in range(number_of_players):
        print(' ****************** PLAYER %d - %s ****************' % (i+1, players[i].name))
        # setting initial bet0
        players[i].set_bet(lowest_bet, type[i])
        wait(t)

for i in range(number_of_players):
    if type[i] == "p":
        print(' ****************** PLAYER - %s ****************' % players[i].name)
        # start session
        print('player is picking two cards...')
        card_box, card_cnt, shuffle_point = card_inc(card_box, 2, card_cnt, shuffle_point, numer_of_decks)
        players[i].new_session(card_box)
        # print(card_box)
        players[i].show_state()
        bjs[i] = players[i].check_blackjack(twentyone)
        wait(t)

        print(' ****************** PLAYER - %s ****************' % players[i].name)
        players[i].show_state()
        left_over[i] = players[i].points
        if bjs[i]:
            left_over[i] = players[i].points
        else:
            while True:
                # stop betting ?
                hit_stand = input('do you want to hit ? (y / n)')
                wait(t)
                if hit_stand.lower() in yes:
                    print('player is picking a new card...')
                    card_box, card_cnt, shuffle_point = card_inc(card_box, 1, card_cnt, shuffle_point, numer_of_decks)
                    players[i].hit(card_box)
                    if players[i].points >= twentyone:
                        left_over[i] = players[i].points
                        bjs[i] = players[i].check_blackjack(twentyone)
                        break
                elif hit_stand.lower() in no:
                    left_over[i] = players[i].points
                    bjs[i] = players[i].check_blackjack(twentyone)
                    break
                else:
                    print('invalid input !!  valid is "y" or "n"')
    elif type[i] == "e":
        print(' ****************** PLAYER - %s ****************' % players[i].name)
        print('player is picking two cards...')
        card_box, card_cnt, shuffle_point = card_inc(card_box, 2, card_cnt, shuffle_point, numer_of_decks)
        players[i].new_session(card_box)
        players[i].show_state()
        bjs[i] = players[i].check_blackjack(twentyone)
        wait(t)

        print(' ****************** PLAYER - %s ****************' % players[i].name)
        players[i].show_state()
        left_over[i] = players[i].points
        if bjs[i]:
            left_over[i] = players[i].points
        else:
            while players[i].points<20:
                # stop betting ?
                print('do you want to hit ? (y / n)')
                if random.randint(0,1) == True:
                    hit_stand = "y"
                    print('y')
                    print('player is picking a new card...')
                    card_box, card_cnt, shuffle_point = card_inc(card_box, 1, card_cnt, shuffle_point, numer_of_decks)
                    players[i].hit(card_box)
                    if players[i].points >= twentyone:
                        left_over[i] = players[i].points
                        bjs[i] = players[i].check_blackjack(twentyone)
                        break
                else:
                    print('n')
                    left_over[i] = players[i].points
                    bjs[i] = players[i].check_blackjack(twentyone)
                    break

    elif type[i] == "m":
        print(' ****************** PLAYER - %s ****************' % players[i].name)
        # start session
        print('player is picking two cards...')
        card_box, card_cnt, shuffle_point = card_inc(card_box, 2, card_cnt, shuffle_point, numer_of_decks)
        players[i].new_session(card_box)
        # print(card_box)
        players[i].show_state()
        bjs[i] = players[i].check_blackjack(twentyone)
        wait(t)

        print(' ****************** PLAYER - %s ****************' % players[i].name)
        players[i].show_state()
        left_over[i] = players[i].points
        if bjs[i]:
            left_over[i] = players[i].points
        else:
            while True:
                # stop betting ?
                print('do you want to hit ? (y / n)')
                if players[i].points < 18:
                    hit_stand = "y"
                    print('y')
                    print('player is picking a new card...')
                    card_box, card_cnt, shuffle_point = card_inc(card_box, 1, card_cnt, shuffle_point, numer_of_decks)
                    players[i].hit(card_box)
                    if players[i].points >= twentyone:
                        left_over[i] = players[i].points
                        bjs[i] = players[i].check_blackjack(twentyone)
                        break
                else:
                    print('n')
                    bjs[i] = players[i].check_blackjack(twentyone)
                    left_over[i] = players[i].points
                    break

    else:
        print(' ****************** PLAYER - %s ****************' % players[i].name)
        # start session
        print('player is picking two cards...')
        card_box, card_cnt, shuffle_point = card_inc(card_box, 2, card_cnt, shuffle_point, numer_of_decks)
        players[i].new_session(card_box)
        # print(card_box)
        players[i].show_state()
        bjs[i] = players[i].check_blackjack(twentyone)
        wait(t)

        print(' ****************** PLAYER - %s ****************' % players[i].name)
        players[i].show_state()
        left_over[i] = players[i].points
        if bjs[i]:
            left_over[i] = players[i].points
        else:
            while True:
                print('do you want to hit ? (y / n)')
                if players[i].check_A() == 0:
                    if players[i].points<17:
                        hit_stand = "y"
                        print('y')
                        print('player is picking a new card...')
                        card_box, card_cnt, shuffle_point = card_inc(card_box, 1, card_cnt, shuffle_point, numer_of_decks)
                        players[i].hit(card_box)
                        if players[i].points >= twentyone:
                            left_over[i] = players[i].points
                            bjs[i] = players[i].check_blackjack(twentyone)
                            break
                    else:
                        print('n')
                        bjs[i] = players[i].check_blackjack(twentyone)
                        left_over[i] = players[i].points
                        break
                elif players[i].check_A() == 1:
                    if players[i].points < 18:
                        hit_stand = "y"
                        print('y')
                        print('player is picking a new card...')
                        card_box, card_cnt, shuffle_point = card_inc(card_box, 1, card_cnt, shuffle_point,
                                                                     numer_of_decks)
                        players[i].hit(card_box)
                        if players[i].points >= twentyone:
                            left_over[i] = players[i].points
                            bjs[i] = players[i].check_blackjack(twentyone)
                            break
                    else:
                        print('n')
                        bjs[i] = players[i].check_blackjack(twentyone)
                        left_over[i] = players[i].points
                        break
                elif players[i].check_A()== 2:
                    print('n')
                    bjs[i] = players[i].check_blackjack(twentyone)
                    left_over[i] = players[i].points
                    break

bjs = np.array(bjs)
win_state = np.array(win_state)
left_over = np.array(left_over)
print(left_over)
for l in range(number_of_players):
    print(left_over[l])
    if left_over[l] > 21:
        left_over[l] = 0

print(left_over)
for k in range(number_of_players):
    if (max(left_over) == left_over[k]) and left_over[k]>0:
        win_state[k] = 'w'
    else:
        win_state[k] = 'l'

print(win_state)
for i in range(number_of_players):
        players[i].update_money(win_state[i])
        if win_state[i] == 'w':
            wstate, gstate = 'wins', 'gains'
        else:
            wstate, gstate = 'loses', 'loses'
        print('"%s" %s, %s bet of %d, current fund: %d' % (
        players[i].name, wstate, gstate, players[i].bet if not bjs[i] else 1.5 * players[i].bet, players[i].money))
        # players[i].show_state()

        # W TYM MIEJSCU JEST ZRZUCANIE STATYSTYK DO BAZY DANYCH PO ZAKOŃCZONEJ ROZGRYWCE !
        # user
        if(type[i] == "p"):
            total_time = time.time() - t0
            db.updatePlayerStat(db,players[i].name,getPlayerResult(i),round(total_time,2),getAmount(i,players[i].bet if not bjs[i] else 1.5 * players[i].bet))
            db.updateCardStats(db,players[i].name,getCardDictFromList(players[i].get_stats()))
        # AI easy
        if (type[i] == "e"):
            total_time = time.time() - t0
            db.updatePlayerStat(db, 'AI- easy', getPlayerResult(i), round(total_time, 2),getAmount(i, players[i].bet if not bjs[i] else 1.5 * players[i].bet))
            db.updateCardStats(db, 'AI- easy', getCardDictFromList(players[i].get_stats()))
        # AI medium
        if (type[i] == "m"):
            total_time = time.time() - t0
            db.updatePlayerStat(db, 'AI- medium', getPlayerResult(i), round(total_time, 2),getAmount(i, players[i].bet if not bjs[i] else 1.5 * players[i].bet))
            db.updateCardStats(db, 'AI- medium' , getCardDictFromList(players[i].get_stats()))
        # AI hard
        if (type[i] == "h"):
            total_time = time.time() - t0
            db.updatePlayerStat(db, 'AI- hard', getPlayerResult(i), round(total_time, 2),getAmount(i, players[i].bet if not bjs[i] else 1.5 * players[i].bet))
            db.updateCardStats(db, 'AI- hard' , getCardDictFromList(players[i].get_stats()))
        # W TYM MIEJSCU SIE TO KONCZY !

total_time = time.time() - t0
print ('Game time: ' + str(total_time))
print('###################################################################################')
print('################################## GAME OVER ######################################')
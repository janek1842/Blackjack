import np as np

from utils import *
import numpy

twentyone = 21
lowest_bet = 5
yes = ['y', 'yes']
no = ['n', 'no']
numer_of_decks = 4

init_players = int(input('enter total players : '))
players = np.array([Player(input('enter name - %d : ' % (i + 1))) for i in range(init_players)])

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
        print(' ****************** PLAYER - %s ****************' % players[i].name)
        # setting initial bet
        players[i].set_bet(lowest_bet)
        wait(.5)

for i in range(number_of_players):
        print(' ****************** PLAYER - %s ****************' % players[i].name)
        # start session
        print('player is picking two cards...')
        card_box, card_cnt, shuffle_point = card_inc(card_box, 2, card_cnt, shuffle_point, numer_of_decks)
        players[i].new_session(card_box)
        # print(card_box)
        players[i].show_state()
        bjs[i] = players[i].check_blackjack(twentyone)
        wait()

        print(' ****************** PLAYER - %s ****************' % players[i].name)
        players[i].show_state()
        if bjs[i]:
            left_over[i] = players[i].points
        else:
            while True:
                # stop betting ?
                hit_stand = input('do you want to hit ? (y / n)')
                if hit_stand.lower() in yes:
                    print('player is picking a new card...')
                    card_box, card_cnt, shuffle_point = card_inc(card_box, 1, card_cnt, shuffle_point, numer_of_decks)
                    players[i].hit(card_box)
                    if players[i].points >= twentyone:
                        left_over[i] = players[i].points
                        break
                elif hit_stand.lower() in no:
                    left_over[i] = players[i].points
                    break
                else:
                    print('invalid input !!  valid is "y" or "n"')

bjs = np.array(bjs)
win_state = np.array(win_state)
left_over = np.array(left_over)
id = left_over.argmax()
for l in range(number_of_players):
    if left_over[l] > 21:
        left_over[l] = 0
id = left_over.argmax()
for k in range(number_of_players):
    if k == id:
            win_state[k] = 'w'
    elif left_over[k] == left_over[id]:
            win_state[k] = 'd'

for i in range(number_of_players):
        players[i].update_money(win_state[i])
        if win_state[i] == 'w':
            wstate, gstate = 'wins', 'gains'
        elif win_state[i] == 'd':
            wstate, gstate = 'draws', 'gets back'
        else:
            wstate, gstate = 'loses', 'loses'
        print('"%s" %s, %s bet of %d, current fund: %d' % (
        players[i].name, wstate, gstate, players[i].bet if not bjs[i] else 1.5 * players[i].bet, players[i].money))

print('###################################################################################')
print('################################## GAME OVER ######################################')
from utils import *

base_point = 21
deal_lbase = 17
lowest_bet = 5
yes = ['y', 'yes']
no = ['n', 'no']
ndeck = 6

init_players = 1
players = np.array([Player(input('enter your name: ')) for i in range(init_players)])

# game begins
card_box = {
    'heart': (['A', 'J', 'Q', 'K'] + ['%d' % i for i in range(2, 11)]) * ndeck,
    'diamond': (['A', 'J', 'Q', 'K'] + ['%d' % i for i in range(2, 11)]) * ndeck,
    'club': (['A', 'J', 'Q', 'K'] + ['%d' % i for i in range(2, 11)]) * ndeck,
    'spade': (['A', 'J', 'Q', 'K'] + ['%d' % i for i in range(2, 11)]) * ndeck
}
card_cnt = 0
shuffle_point = np.random.randint((ndeck * 52) // 2, ndeck * 52)
total_players = len(players)
bjs = [False for i in range(total_players)]
left_over = [None for i in range(total_players)]
win_state = ['l' for i in range(total_players)]

for i in range(total_players):
        print(' ****************** PLAYER - %s ****************' % players[i].name)
        # setting initial bet
        players[i].set_bet(lowest_bet)
        wait(.5)

for i in range(total_players):
        print(' ****************** PLAYER - %s ****************' % players[i].name)
        print('player is picking two cards...')
        card_box, card_cnt, shuffle_point = card_inc(card_box, 2, card_cnt, shuffle_point, ndeck)
        players[i].new_session(card_box)
        # print(card_box)
        players[i].show_state()
        bjs[i] = players[i].check_blackjack(base_point)
        wait()

for i in range(total_players):
        print(' ****************** PLAYER - %s ****************' % players[i].name)
        players[i].show_state()
        if bjs[i]:
            left_over[i] = players[i].points
        else:
            while True:
                # stop betting ?
                hit_stand = input('do you want to hit ? (y / n)')
                if hit_stand.lower() in yes:
                    wait(.5)
                    # new card
                    print('player is picking a new card...')
                    card_box, card_cnt, shuffle_point = card_inc(card_box, 1, card_cnt, shuffle_point, ndeck)
                    players[i].hit(card_box)
                    if players[i].points >= base_point:
                        left_over[i] = players[i].points
                        break
                elif hit_stand.lower() in no:
                    left_over[i] = players[i].points
                    break
                else:
                    print('invalid input !!  valid is "y" or "n"')
        # print(card_box)

bjs = np.array(bjs)
win_state = np.array(win_state)
left_over = np.array(left_over)

print('computer is picking two cards...')
card_box, card_cnt, shuffle_point = card_inc(card_box, 2, card_cnt, shuffle_point, ndeck)
computer_cards = [pick_a_card(card_box, True), pick_a_card(card_box, True)]
computer_point = calc_points([computer_cards[0]])

computer_point = calc_points(computer_cards)
print('dealer cards : ', computer_cards, '\t\t total points : ', computer_point)
wait()

# dealer has blackjack
if computer_point == base_point:
        win_state[bjs] = 'd'
else:
        # straight win for blackjacks
        win_state[bjs] = 'w'

        # dealer will pick
        while True:

            if computer_point >= deal_lbase:
                break
            else:
                print('dealer is picking a new card...')
                computer_cards += [pick_a_card(card_box, True)]
                computer_point = calc_points(computer_cards)
                print('dealer cards : ', computer_cards, '\t\t total points : ', computer_point)
                wait()

        if computer_point > base_point:
            if left_over <= base_point:
                wstate, gstate = 'wins', 'gains'
                print('"%s" %s, %s bet of %d, current fund: %d' % (
                    players[i].name, wstate, gstate, players[i].bet if not bjs[i] else 1.5 * players[i].bet,
                    players[i].money))
                print('computer loses, loses bet of 500, current found: 0')
            else:
                wstate, gstate = 'loses', 'loses'
                print('"%s" %s, %s bet of %d, current fund: %d' % (
                    players[i].name, wstate, gstate, players[i].bet if not bjs[i] else 1.5 * players[i].bet,
                    players[i].money))
                print('computer loses, loses bet of 500, current found: 0')
        else:
            if left_over <= base_point:
                if left_over > computer_point:
                    wstate, gstate = 'wins', 'gains'
                    print('"%s" %s, %s bet of %d, current fund: %d' % (
                        players[i].name, wstate, gstate, players[i].bet if not bjs[i] else 1.5 * players[i].bet,
                        players[i].money))
                    print('computer loses, loses bet of 500, current found: 0')
                elif left_over == computer_point:
                    wstate, gstate = 'draws', 'gets back'
                    print('"%s" %s, %s bet of %d, current fund: %d' % (
                        players[i].name, wstate, gstate, players[i].bet if not bjs[i] else 1.5 * players[i].bet,
                        players[i].money))
                    print('computer draws, get back bet of 500, current found: 500')
                else:
                    wstate, gstate = 'loses', 'loses'
                    print('"%s" %s, %s bet of %d, current fund: %d' % (
                        players[i].name, wstate, gstate, players[i].bet if not bjs[i] else 1.5 * players[i].bet,
                        players[i].money))
                    print('computer wins, gains bet of 500, current found: 1000')

            else:
                wstate, gstate = 'loses', 'loses'
                print('"%s" %s, %s bet of %d, current fund: %d' % (
                    players[i].name, wstate, gstate, players[i].bet if not bjs[i] else 1.5 * players[i].bet,
                    players[i].money))
                print('computer wins, gains bet of 500, current found: 1000')

print('###################################################################################')
print('################################## GAME OVER ######################################')
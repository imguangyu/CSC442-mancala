#!/usr/bin/python

import sys

import numpy as np
from mancala import Mancala
from strategy import Random_player, Human_player

PITS = 6
STONES = 4

def terminal_test(state):
    """
        return None if not terminal, otherwise return the winner, 0 for draw
    """
    sum_1 = state[0,1:].sum()
    sum_2 = state[1,:-1].sum()

    store_1 = state[0,0]
    store_2 = state[1,-1]

    if sum_1 * sum_2 == 0:
        if store_1 + sum_1 > store_2 + sum_2:
            return 1
        elif store_1 + sum_1 < store_2 + sum_2:
            return 2
        else:
            return 0
    
    return None

def main():

    m = Mancala(PITS,STONES)

    player_1_str = sys.argv[1]
    player_2_str = sys.argv[2]

    if player_1_str == 'human':
        player_1 = Human_player(PITS)
    elif player_1_str == 'random':
        player_1 = Random_player(PITS)
    
    if player_2_str == 'human':
        player_2 = Human_player(PITS)
    elif player_2_str == 'random':
        player_2 = Random_player(PITS)

    player = 1

    players = [0]
    players.append(player_1)
    players.append(player_2)

    result = None
    while True:
        print("Player %d's turn:\n" % player)
        action = players[player].get_action(m.state, player)
        print(action)
        player = m.sow(action,player)
        m.print()

        result = terminal_test(m.state)
        if result:
            if result == 0:
                print("Draw.")
            else:
                print("Player %d wins!" % result)

            m.print_done()
            break

        # input()


if __name__ == '__main__':
    main()
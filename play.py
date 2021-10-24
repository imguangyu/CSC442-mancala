#!/usr/bin/python

import sys

import numpy as np
from mancala import Mancala
from strategy import MinMax_player, Random_player, Human_player, AlphaBeta_player

PITS = 6
STONES = 4
DEPTH_1 = 3
DEPTH_2 = 7

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

def main(player_1_str = None, player_2_str = None):

    m = Mancala(PITS,STONES)

    if player_1_str is None and player_2_str is None:
        player_1_str = sys.argv[1]
        player_2_str = sys.argv[2]

    if player_1_str == 'human':
        player_1 = Human_player(PITS)
    elif player_1_str == 'random':
        player_1 = Random_player(PITS)
    elif player_1_str == 'minmax':
        player_1 = MinMax_player(PITS, 1, DEPTH_1)
    elif player_1_str == 'alphabeta':
        player_1 = AlphaBeta_player(PITS, 1, DEPTH_1)
    
    if player_2_str == 'human':
        player_2 = Human_player(PITS)
    elif player_2_str == 'random':
        player_2 = Random_player(PITS)
    elif player_2_str == 'minmax':
        player_2 = MinMax_player(PITS, 2, DEPTH_2)
    elif player_2_str == 'alphabeta':
        player_2 = AlphaBeta_player(PITS, 2, DEPTH_2)

    player = 1

    players = [0]
    players.append(player_1)
    players.append(player_2)

    result = None
    while True:
        print("Player %d's turn:\n" % player)
        action = players[player].get_action(m.state.copy(), player)
        print(action)
        state, player = m.sow(action,player)
        m.state = state
        m.print()

        result = terminal_test(m.state)
        if not result==None:
            if result == 0:
                print("Draw.")
            else:
                print("Player %d wins!" % result)

            m.print_done()

            return result

        # input()


if __name__ == '__main__':
    main()
#!/usr/bin/python

import sys

import numpy as np
from mancala import Mancala
from strategy import MinMax_player, Random_player, Human_player, AlphaBeta_player
import time

PITS = 6
STONES = 4
DEPTH_1 = 3
DEPTH_2 = 3

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

def main(player_1_str = None, player_2_str = None, depth_1 = None, depth_2 = None):

    m = Mancala(PITS,STONES)

    if player_1_str is None and player_2_str is None:
        player_1_str = sys.argv[1]
        player_2_str = sys.argv[2]

    if depth_1 is None:
        depth_1 = DEPTH_1
    if depth_2 is None:
        depth_2 = DEPTH_2

    if player_1_str == 'human':
        player_1 = Human_player(PITS)
    elif player_1_str == 'random':
        player_1 = Random_player(PITS)
    elif player_1_str == 'minimax':
        player_1 = MinMax_player(PITS, 1, depth_1)
    elif player_1_str == 'alphabeta':
        player_1 = AlphaBeta_player(PITS, 1, depth_1)
    
    if player_2_str == 'human':
        player_2 = Human_player(PITS)
    elif player_2_str == 'random':
        player_2 = Random_player(PITS)
    elif player_2_str == 'minimax':
        player_2 = MinMax_player(PITS, 2, depth_2)
    elif player_2_str == 'alphabeta':
        player_2 = AlphaBeta_player(PITS, 2, depth_2)

    player = 1

    players = [0]
    timers = [0]
    players.append(player_1)
    players.append(player_2)

    timers.append(0.)
    timers.append(0.)

    result = None
    m.print()
    while True:
        print("Player %d's turn:\n" % player)
        start_time = time.time()
        action = players[player].get_action(m.state.copy(), player)
        end_time = time.time()

        timers[player] += end_time - start_time

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

            return result, timers

        # input()


def evluation(evaluation_num = 100, file_name = 'experiments_2.txt'):
    with open(file_name, 'wt') as f:
        # print("Random vs. MiniMax(3)",file = f)
        # print("-" * 50,file = f)
        # result = np.zeros(3,int)
        # for i in range(evaluation_num):
        #     res, timers = main("random","minimax",depth_2= 3)
        #     result[res] += 1
        # print("Draw: {:d}, Player 1 wins: {:d}, Player 2 wins: {:d}".format(*result.tolist()), file = f)
        # print("Player 1 times: {:f}, Player 2 times: {:f}".format(timers[1], timers[2]), file = f)
        # print("=" * 50,file=f)

        # print("Random vs. AlphaBeta(3)",file = f)
        # print("-" * 50,file = f)
        # result = np.zeros(3,int)
        # for i in range(evaluation_num):
        #     res, timers = main("random","alphabeta",depth_2= 3)
        #     result[res] += 1
        # print("Draw: {:d}, Player 1 wins: {:d}, Player 2 wins: {:d}".format(*result.tolist()), file = f)
        # print("Player 1 times: {:f}, Player 2 times: {:f}".format(timers[1], timers[2]), file = f)
        # print("=" * 50,file=f)

        # print("Random vs. Random",file = f)
        # print("-" * 50,file = f)
        # result = np.zeros(3,int)
        # for i in range(evaluation_num):
        #     res, timers = main("random","random")
        #     result[res] += 1
        # print("Draw: {:d}, Player 1 wins: {:d}, Player 2 wins: {:d}".format(*result.tolist()), file = f)
        # print("Player 1 times: {:f}, Player 2 times: {:f}".format(timers[1], timers[2]), file = f)
        # print("=" * 50,file=f)

        # print("MiniMax(3) vs. MiniMax(5)",file = f)
        # print("-" * 50,file = f)
        # result = np.zeros(3,int)
        # for i in range(evaluation_num):
        #     res, timers = main("minimax","minimax",3,5)
        #     result[res] += 1
        # print("Draw: {:d}, Player 1 wins: {:d}, Player 2 wins: {:d}".format(*result.tolist()), file = f)
        # print("Player 1 times: {:f}, Player 2 times: {:f}".format(timers[1], timers[2]), file = f)
        # print("=" * 50,file=f)

        # print("AlphaBeta(3) vs. AlphaBeta(10)",file = f)
        # print("-" * 50,file = f)
        # result = np.zeros(3,int)
        # for i in range(evaluation_num):
        #     res, timers = main("alphabeta","alphabeta",3,10)
        #     result[res] += 1
        # print("Draw: {:d}, Player 1 wins: {:d}, Player 2 wins: {:d}".format(*result.tolist()), file = f)
        # print("Player 1 times: {:f}, Player 2 times: {:f}".format(timers[1], timers[2]), file = f)
        # print("=" * 50,file=f)

        print("MiniMax(5) vs. AlphaBeta(5)",file = f)
        print("-" * 50,file = f)
        result = np.zeros(3,int)
        for i in range(evaluation_num):
            res, timers = main("minimax","alphabeta",5,5)
            result[res] += 1
        print("Draw: {:d}, Player 1 wins: {:d}, Player 2 wins: {:d}".format(*result.tolist()), file = f)
        print("Player 1 times: {:f}, Player 2 times: {:f}".format(timers[1], timers[2]), file = f)
        print("=" * 50,file=f)

        

if __name__ == '__main__':

    # evluation()
    main()
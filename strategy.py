import numpy as np
from mancala import Mancala
import pdb

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

class Random_player():

    def __init__(self, pits) -> None:
        self.pits = pits

    def get_action(self, state, player):
        if player == 1:
            idx = np.array(np.where(state[player-1,1:] != 0))
            idx += 1
        else:
            idx = np.array(np.where(state[player-1,:-1] != 0))
            idx += 1

        return np.random.choice(idx[0])

class Human_player():

    def __init__(self, pits) -> None:
        self.pits = pits

    def get_action(self, state, player):
        
        return int(input())

class MinMax_player():

    def __init__(self, pits, player, depth) -> None:
        self.pits = pits
        self.player = player
        self.brain = Mancala(pits)
        self.depth = depth

    def _get_valid_actions(self, state, player):
        if player == 1:
            idx = np.array(np.where(state[player-1,1:] != 0))
            idx += 1
        else:
            idx = np.array(np.where(state[player-1,:-1] != 0))
            idx += 1

        return idx[0]

    def get_action(self, state, player):

        actions = self._get_valid_actions(state.copy(), self.player)

        best = -np.inf
        best_action = []

        origin_state = state.copy()
        origin_player = player

        for action in actions:
            # print("Working on action %d" % action)
            state = origin_state.copy()
            player = origin_player
            state, player = self.brain.sow(action, player, state.copy())
            value = self.minmax(state.copy(), player, self.depth)

            if value > best:
                best = value
                best_action = [action]
            elif value == best:
                best = value
                best_action.append(action)

        return np.random.choice(best_action)

    def h(self, state, player):

        store_1 = state[0,0]
        store_2 = state[1,-1]

        stores = [store_1, store_2]

        return stores[player-1]



    def minmax(self, state, player, depth):

        result = terminal_test(state.copy())

        if not (result is None):
            # print(result)
            if result == player:
                return np.iinfo(np.int32).max
            if result == 3-player:
                return np.iinfo(np.int32).min

            return result

        if depth == 0:
            return self.h(state.copy(),player)

        self.brain.state = state.copy()

        if player == self.player: # Max

            best = np.iinfo(np.int32).min
            actions = self._get_valid_actions(state.copy(), player)
            origin_state = state.copy()
            origin_player = player
            for action in actions:
                state = origin_state.copy()
                player = origin_player
                state, player = self.brain.sow(action, player, state.copy())
                # self.brain.print(state)
                # pdb.set_trace()
                value = self.minmax(state.copy(), player, depth - 1)

                if value >= best:
                    best = value

            return best

        else: # Min
            best = np.iinfo(np.int32).max
            actions = self._get_valid_actions(state.copy(),player)
            origin_state = state.copy()
            origin_player = player
            for action in actions:
                player = origin_player
                state = origin_state.copy()
                state, player = self.brain.sow(action, player, state.copy())
                # self.brain.print(state)
                # pdb.set_trace()
                value = self.minmax(state.copy(), player, depth - 1)
                
                if value <= best:
                    best = value

            return best
class AlphaBeta_player():

    def __init__(self, pits, player, depth) -> None:
        self.pits = pits
        self.player = player
        self.brain = Mancala(pits)
        self.depth = depth

    def _get_valid_actions(self, state, player):
        if player == 1:
            idx = np.array(np.where(state[player-1,1:] != 0))
            idx += 1
        else:
            idx = np.array(np.where(state[player-1,:-1] != 0))
            idx += 1

        return idx[0]

    def get_action(self, state, player):

        actions = self._get_valid_actions(state.copy(), self.player)

        best = -np.inf
        best_action = []

        origin_state = state.copy()
        origin_player = player

        for action in actions:
            # print("Working on action %d" % action)
            state = origin_state.copy()
            player = origin_player
            state, player = self.brain.sow(action, player, state.copy())
            value = self.alphabeta(state.copy(), player, self.depth, -np.inf, np.inf )

            if value > best:
                best = value
                best_action = [action]
            elif value == best:
                best = value
                best_action.append(action)

        return np.random.choice(best_action)

    def h(self, state, player):

        store_1 = state[0,0]
        store_2 = state[1,-1]

        stores = [store_1, store_2]

        return stores[player-1]



    def alphabeta(self, state, player, depth, alpha, beta):

        result = terminal_test(state.copy())

        if not (result is None):
            # print(result)
            if result == player:
                return np.iinfo(np.int32).max
            if result == 3-player:
                return np.iinfo(np.int32).min

            return result

        if depth == 0:
            return self.h(state.copy(),player)

        self.brain.state = state.copy()

        if player == self.player: # Max

            best = np.iinfo(np.int32).min
            actions = self._get_valid_actions(state.copy(), player)
            origin_state = state.copy()
            origin_player = player
            for action in actions:
                state = origin_state.copy()
                player = origin_player
                state, player = self.brain.sow(action, player, state.copy())
                # self.brain.print(state)
                # pdb.set_trace()
                value = self.alphabeta(state.copy(), player, depth - 1, alpha, beta)
                alpha = max(alpha, value)
                if value >= best:
                    best = value
                
                if beta <= alpha:
                    break

            return best

        else: # Min
            best = np.iinfo(np.int32).max
            actions = self._get_valid_actions(state.copy(),player)
            origin_state = state.copy()
            origin_player = player
            for action in actions:
                player = origin_player
                state = origin_state.copy()
                state, player = self.brain.sow(action, player, state.copy())
                # self.brain.print(state)
                # pdb.set_trace()
                value = self.alphabeta(state.copy(), player, depth - 1, alpha, beta)
                beta = min(beta, value)

                if value <= best:
                    best = value
                
                if beta <= alpha:
                    break

            return best


if __name__ == '__main__':

    # a = Random_player(6)

    # a = Human_player(6)

    # print(a.get_action(None))
    # print(np.where(np.array([0,1,2,0,3]) == 0))

    # m = Mancala()
    # a = MinMax_player(6,1)
    # print(a._get_valid_actions(m.state,1))

    a = np.array([1])
    def plus(a):
        a += 1
        return a

    # import copy
    b = a
    plus(b)

    print(a)


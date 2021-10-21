import numpy as np

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


if __name__ == '__main__':

    # a = Random_player(6)

    # a = Human_player(6)

    # print(a.get_action(None))
    print(np.where(np.array([0,1,2,0,3]) == 0))
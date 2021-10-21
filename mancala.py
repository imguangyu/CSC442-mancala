import numpy as np

class Mancala:

    def __init__(self,pits=6,stones=4):

        self.pits = pits
        self.stones = stones

        self.state = np.ones((2,pits+1),int) * stones
        # Store
        self.state[0,0] = 0
        self.state[1,pits] = 0

    def get_next(self,index,player):
        """
            index: (2,) current index of state, (0,0) for store_1, (1,p) for store_2
            player: 1 or 2, indicating which player is moving 
        """
        row = index[0]
        column = index[1]
        if player == 1:
            if row == 0:
                if column == 0:
                    return (1, 0)
                else:
                    return (row, column - 1)
            else: # row ==1
                if column == self.pits - 1:
                    return (0, self.pits)
                else:
                    return (row, column + 1)
        else: # player 2
            if row == 0:
                if column == 1:
                    return (1, 0)
                else:
                    return (row, column - 1)
            else: # row ==1
                if column == self.pits:
                    return (0, self.pits)
                else:
                    return (row, column + 1)

    def _is_store(self,position):
        return True if position == (0,0) or position == (1,self.pits) else False

    def _get_store(self,player):
        return (0,0) if player == 1 else (1,self.pits)

    def _get_opp_index(self,pos,player):
        row = 1 - pos[0]
        if player == 1:
            col = pos[1] - 1 
        else:
            col = pos[1] + 1

        return (row,col)
            

    def sow(self, position, player):
        if not (1 <= position <= self.pits):
            print("Invalid move. Try again.")
            return player

        if player == 2:
            position -= 1

        current = (player-1, position)
        remaining = self.state[current]
        if remaining == 0:
            print("Invalid move. Try again.")
            return player

        self.state[current] = 0
        while remaining>0:
            current = self.get_next(current,player)
            self.state[current] += 1 
            remaining -= 1
        # Can take a free turn?
        if self._is_store(current):
            return player
        # Can capture?
        if self.state[current] == 1 and current[0] == player-1:
            self.state[self._get_store(player)] += self.state[self._get_opp_index(current,player)]+1
            self.state[self._get_opp_index(current,player)] = 0
            self.state[current] = 0
        
        return 3-player

    def print(self):
        # First row
        temp = "{:>5d} - "
        for i in range(self.pits):
            temp += "|{:>5d}|"
        print(temp.format(*list(self.state[0])))
        print("-" * (self.pits * 10))
        temp = " "*8
        for i in range(self.pits):
            temp += "|{:>5d}|"
        temp += " -{:>5d}"
        print('\033[95m'+temp.format(*list(self.state[1]))+'\033[0m')

    def print_done(self):

        sum_1 = self.state[0,1:].sum()
        sum_2 = self.state[1,:-1].sum()

        self.state[0, 0] += sum_1
        self.state[1, -1] += sum_2

        state = np.zeros_like(self.state)
        state[0, 0] = self.state[0, 0] 
        state[1, -1] = self.state[1, -1]

        temp = "{:>5d} - "
        for i in range(self.pits):
            temp += "|{:>5d}|"
        print(temp.format(*list(state[0])))
        print("-" * (self.pits * 10))
        temp = " "*8
        for i in range(self.pits):
            temp += "|{:>5d}|"
        temp += " -{:>5d}"
        print('\033[95m'+temp.format(*list(state[1]))+'\033[0m')

if __name__ =='__main__':
    m = Mancala()

    # m.print()
    player = 1
    while True:
        action = int(input("Player %d's turn:\n" % player))
        player = m.sow(action,player)
        m.print()
    # print(m.get_next([1,6],2))


        

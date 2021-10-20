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
            index: (2,) current index of state, (0,0) for store_1, (1,p) or store_2
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

    def sow(self, position, player):
        current = (player-1, position)
        remaining = self.state[current]
        self.state[current] = 0
        while remaining>0:
            current = self.get_next(current,player)
            self.state[current] += 1 
            remaining -= 1


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
        print(temp.format(*list(self.state[1])))

if __name__ =='__main__':
    m = Mancala()

    # m.print()
    m.sow(1,1)
    m.sow(2,2)
    m.print()
    # print(m.get_next([1,6],2))


        

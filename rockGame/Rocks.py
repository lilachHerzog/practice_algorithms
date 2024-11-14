class Rocks:
    """
    A class used to play a game where each player (out of 2) chooses a pile of rocks from one end of a row of rocks.
    The goal of the game is to reach the maximum number of stones.
    """
    def __init__(self, arr):
        self.rocks = {'p1': 0, 'p2': 0}
        self.arr = arr  
    
    def takePile(self, player ,side):
       """adds rocks from the chosen pile to the chosen player """
        self.rocks[player] += self.arr[side] # add selected rocks to the player's pile
        print(player, " takes ", self.arr.pop(side))
        return 
            
    def findBestEdge(self, player):
        """ finds the edge (start or end) that will result in the biggest sum of rocks"""
        if len(self.arr) == 1: 
            return self.takePile(player, 0)
        if arr[0] - max(arr[1], arr[-1]) > arr[-1] - max(arr[-2], arr[0]): # the more the other player gets the less i have
            self.takePile(player, 0)
        else:
            self.takePile(player, -1)
        playerIndex = (list(self.rocks).index(player) + 1) % 2 # find the index of the player
        player = list(self.rocks)[playerIndex % 2] # get the next player by index (only 2 players, so % 2)
        return self.findBestEdge(player)

    def canWin(self):
        """ The goal of the function is to determine whther the first player can win"""
        self.findBestEdge('p1')
        return self.rocks['p1'] > self.rocks['p2']

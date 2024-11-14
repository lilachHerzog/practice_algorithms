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
        playerIndex = list(self.rocks).index(player) # find the index of the player
        player = list(self.rocks)[(playerIndex + 1) % 2] # get the next player by index (only 2 players, so % 2)
        return self.findBestEdge(player)

    def canWin(self):
        """ The goal of the function is to determine whther the first player can win"""
        return self.rocks['p1'] > self.rocks['p2']


if __name__ == "__main__":
    arrays = [[2, 5, 3, 2],
              [1, 8, 3, 6, 4, 2],
              [5, 9, 1, 4, 6, 8, 3],
              [7, 4, 2, 5, 8, 1], 
              [3, 8, 4, 1, 7, 5, 2],
              [6, 1, 3, 5, 2],
              [4, 2, 9, 3, 5, 6]] 
    for arr in arrays:
        print('\n', arr)
        rocksAlg = Rocks(arr.copy())
        rocksAlg.findBestEdge("p1")
        if rocksAlg.canWin():
            print ("YES! the first player won with", rocksAlg.rocks['p1'], " while the second player got only ", rocksAlg.rocks['p2'])  
        else:
            print ("noooo! the first player lost with", rocksAlg.rocks['p1'], " while the second player got ", rocksAlg.rocks['p2'])           

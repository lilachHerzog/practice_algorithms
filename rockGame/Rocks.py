class Rocks:
    """
    A class used to play a game where each player (out of 2) chooses a pile of rocks from one end of a row of rocks.
    
    ...
    
    Attributes
    ----------
    rocks: dict
    saves the number of rocks (values) each player (keys) has.
    arr: array 
    represents a row of piles of rocks, each elemnt represents the number of rocks in the pile.
    
    Methods
    -------
    takePile(player ,side):
        adds rocks from the chosen pile to the chosen player
    findBestEdge(player):
        finds the edge (start or end) that will result in the biggest sum of rocks
    """
    def __init__(self, arr):
        self.rocks = {"myRocks": 0, "otherRocks": 0}
        self.arr = arr  
    
    def takePile(self, player ,side):
        """ adds rocks from the chosen pile to the chosen player
        Parameters
        ----------
        player: string
            the player who's playing in this turn
        side: int
            the side the pile is taken from (indexes at start or end of the array)
        """
        self.rocks[player] += self.arr[side] # add selected rocks to the player's pile
        print(player, " takes ", self.arr.pop(side))
        return 
    
    
    def findBestEdge(self, player):
        """
        finds the edge (start or end) that will result in the biggest sum of rocks
        
        Parameters
        ----------
        player: string
            the player who's playing in this turn                
        """
        if len(self.arr) == 1: 
            return self.takePile(player, 0)
        if arr[0] - max(arr[1], arr[-1]) > arr[-1] - max(arr[-2], arr[0]): # the more the other player gets the less i have
            self.takePile(player, 0)
        else:
            self.takePile(player, -1)
        playerIndex = (list(self.rocks).index(player) + 1) % 2 # find the index of the player
        player = list(self.rocks)[playerIndex % 2] # get the next player by index (only 2 players, so % 2)
        return self.findBestEdge(player)

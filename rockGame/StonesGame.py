"""
this code was originally written by someone else https://algoritmim.co.il/interview-practice/dynaimic-programming-game-of-stones/
there were some problems with the code so i fixed some of it so that now it mostly works, but there are still some arrays that don't
"""
class StonesGame:
    """
    A class used to play a game where each player (out of 2) chooses a pile of rocks from one end of a row of rocks.
    
    ...
    
    Attributes
    ----------
    scoresMemo: dict
        saves for each player the location of the pile so as to not calculate twice.
    moves: dict 
        saves the moves of the players in each round ({round: {player: pile chosen}}).
    
    Methods
    -------
    maxScorePlayer(arr, start, end, player, sumTotal, score, time=0):
        adds rocks from the chosen pile to the chosen player.
    findBestEdge(player):
        finds the edge (start or end) that will result in the biggest sum of rocks.
    """
    def __init__(self):
        self.scoresMemo = {'p1': {}, 'p2' : {}}
        self.moves = {x: ['p'+ str(x%2+1),''] for x in range(1, len(arr)+1)}
        
 
    def maxScorePlayer(self, arr, start, end, player, sumTotal, turn):
        """
        finds (recurrsively) the maximum score a player can achieve.

        Parameters
        ----------
        arr: array
            represents a row of piles of rocks, each elemnt represents the number of rocks in the pile.
        start, end: int
            the part of the array we want to go over (from start to end)
        player: string
            the player who's playing in this turn  
        sumTotal: int
            the maximum sum of rocks possible to achieve
        turn:
            the number of the round of the game
            
        """        
        turn+=1
        # sumTotal -= score
        if start>end:
            return 0

        if (start, end) in self.scoresMemo[player].keys():
            print("should {} takes {}?".format(player, sumTotal - self.scoresMemo[player][start, end]))
            return self.scoresMemo[player][start, end]
 
        if player == 'p1':
            player = 'p2'
            p2TakeLeft = self.maxScorePlayer(arr, start+1, end, player, sumTotal - arr[start], turn)
            p2TakeRight = self.maxScorePlayer(arr, start, end-1, player, sumTotal - arr[end], turn)
            if sumTotal - p2TakeLeft > sumTotal - p2TakeRight:
                result = sumTotal - p2TakeLeft
                if self.moves[turn][0] == player:
                    self.moves[turn][1] = "takes {}".format(arr[start])
                else:
                    print("turn", turn, player, "didnt take", arr[start], " suppesed to be ", self.moves[turn][0])
            else:
                if self.moves[turn][0] == player:
                    self.moves[turn][1] = "takes {}".format(arr[end])
                else:
                    print("turn", turn, player, "didnt take", arr[end], " suppesed to be ", self.moves[turn][0])
                result = sumTotal - p2TakeRight
        else:
            player = 'p1'
            p1TakeLeft = self.maxScorePlayer(arr, start+1, end, player, sumTotal - arr[start], turn)
            p1TakeRight = self.maxScorePlayer(arr, start, end-1, player, sumTotal - arr[end], turn)
            if sumTotal - p1TakeLeft > sumTotal - p1TakeRight:
                result = sumTotal - p1TakeLeft
                if self.moves[turn][0] == player:
                    self.moves[turn][1] = "takes {}".format(arr[start])
                else:
                    print("turn", turn, player, "didnt take", arr[start], " suppesed to be ", self.moves[turn][0])
            else:
                result = sumTotal - p1TakeLeft
                if self.moves[turn][0] == player:
                    self.moves[turn][1] = "takes {}".format(arr[end])
                else:
                    print("turn", turn, player, "didnt take", arr[end], " suppesed to be ", self.moves[turn][0])
        self.scoresMemo[player][start, end] = result
        self.scoresMemo[player]["sum"] = result

        return self.scoresMemo[player][start, end]



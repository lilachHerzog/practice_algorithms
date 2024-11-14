import Rocks
import StonesGame

if __name__ == "__main__":
    arrays = [[2, 5, 3, 2],
              [1, 8, 3, 6, 4, 2],
              [5, 9, 1, 4, 6, 8, 3], # works backwards 
              [7, 4, 2, 5, 8, 1],  # didn't work.  worked(except for 1 misshap) if "end" and "start" were replaced in the insertion
              [3, 8, 4, 1, 7, 5, 2], # backwards +  didn't work: the leftmost elemnet (3) replaced the "1" in the middle
              [6, 1, 3, 5, 2], # didn't work: the leftmost elemnet (6) replaced all other numbers. worked if "end" and "start" were replaced in the insertion
              [4, 2, 9, 3, 5, 6]] # didn't work
    for arr in arrays:
        print('\n', arr, '\nalgo A: ', end = "")
        rocksAlg = Rocks(arr.copy())
        rocksAlg.findBestEdge("p1")
        rocks = sorted(rocksAlg.rocks.items(), key=lambda x: x[1], reverse=True)
        print ("**** the win goes to ", rocks[0][0], " with ", rocks[0][1], ", while ", rocks[1][0], " got only ", rocks[1][1])

        print("algo B: ", end="")
        otherAlg = StonesGame()
        otherAlg.maxScorePlayer(arr, 0, len(arr)-1, 'p2', sum(arr), 0)
        turns = [" ".join(item) for item in dict(sorted(otherAlg.moves.items())).values()]
        
        sliced = [x.split(" ") for x in turns] 
        print("; ".join(turns), end="; ")
        sums = sorted({"p1": sum([int(x[-1]) for x in sliced if x[0]=='p1']),
                "p2": sum([int(x[-1]) for x in sliced if x[0]=='p2'])}.items())
        print ("**** the win goes to ", sums[0][0], " with ", sums[0][1], ", while ", sums[1][0], " got only ", sums[1][1])

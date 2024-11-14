"""
@param arr: an array of positive integers 
            each number describing the maximum jump size (to the next elements)
@return bool: true if it's possible to get to the last element of the array
"""
def jumpGame(arr):
    if len(arr) == 1:
        return True
    for idx, x in enumerate(reversed(arr[:len(arr) - 1])):
        dist = len(arr) - idx - 1
        if x >= dist:
            if jumpGame(arr[:idx + 1]):  
                newPlace =  idx + dist
                print ("arr[{}]={} => arr[{}]={} (jump {} steps)".format(idx, x, newPlace, arr[newPlace], dist))
                return True
            
    return False

if __name__ == '__main__':
  A = [1,2,0,3]
  B = [2,1,0,1]
  C = [3,0,0]
  print('\t',A)
  jumpGame( A)
  print('\n\t', B)
  jumpGame(B)
  print('\n\t', C)
  jumpGame(C)

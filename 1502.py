class Solution:
  def canMakeArithmeticProgression(self, arr:list) -> bool:
    arr.sort() 
    if len(arr) > 1: 
      difference = arr[1] - arr[0] 
    else: 
      return False 
      
    for i in range(len(arr)-1): 
      if arr[i+1] - arr[i] != difference: 
        return False 
      
    return True 
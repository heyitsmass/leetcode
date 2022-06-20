class Solution:
  def countOdds(self, low: int, high: int) -> int:
    range = (high-low) + 1

    if not range % 2: 
      return int(range/2)  
    else: 
      if low % 2 or high % 2: 
        return int(range/2) + 1 
      
      return int(range/2) 
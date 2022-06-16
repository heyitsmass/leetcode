class Solution:
  def isPerfectSquare(self, num: int) -> bool:
 
    if num > 1: 
      n = (num.bit_count() + num.bit_length()) + 3
      b = num / n 
      c = 0 
      for i in range(n): 
        c = num/b 
        b = (b + c) / 2
      num = c 

    return num % 1 == 0

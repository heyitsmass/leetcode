class Solution:
  def mySqrt(self, x: int) -> int:
    if x > 1: 
      n = (x.bit_count() + x.bit_length()) + 3
      b = x / n 
      c = 0 
      for i in range(n): 
        c = x/b 
        b = (b + c) / 2
      return int(c)
    return x
class Solution:
  def countBits(self, n: int) -> list:
    ret = [] 
    for i in range(n+1): 
      ret.append(sum(int(one) for one in bin(i)[2::])) 
    return ret 

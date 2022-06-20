class Solution:
  def digitSum(self, s: str, k: int) -> str:
    if len(s) <= k: return s 

    new = "" 

    i = 0
    while i < len(s): 

      new += str(sum([int(num) for num in str(s[i:i+k])])) 

      i+=k

    return self.digitSum(new, k) 
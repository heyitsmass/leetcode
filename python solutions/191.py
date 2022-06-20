class Solution:
  def hammingWeight(self, n: int) -> int:
    import re
    return len(list(filter(None, re.split(r'(?:0*\D?)', str(bin(n)))))) 
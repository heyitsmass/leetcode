class Solution:
    def addDigits(self, num: int) -> int:
      if num <= 9: return num 

      n = sum([int(n) for n in str(num)])

      return self.addDigits(n)
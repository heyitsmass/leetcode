class Solution:
    def intToRoman(self, num: int) -> str:
      
      romans = { 
        1 : 'I',
        4 : 'IV',
        5 : 'V', 
        9 : 'IX', 
        10 : 'X',
        40 : 'XL',
        50 : 'L',
        90 : 'XC',
        100 : 'C',
        400 : 'CD',
        500 : 'D', 
        900 : 'CM',
        1000 : 'M', 
      }

      nums = romans.keys() 
      conv = ''

      if num in list(romans.keys()): 
        return romans[num] 
      elif num < 1 or num > 3999: 
        raise Exception 

      while num > 0: 
        max, num = self.get_highest(num, nums)
        conv += romans[max] 

      return conv 

    def get_highest(self, num:int, nums:list): 
      for a in nums: 
        if num-a < 0: 
          break 
        difference = num-a 

      return num-difference, difference 


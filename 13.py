class Solution:
    def romanToInt(self, s: str) -> int:

        roman = { 
          'I': 1,
          'V': 5,
          'X': 10, 
          'L': 50, 
          'C': 100, 
          'D': 500, 
          'M': 1000,
          'IV': 4,
          'IX': 9,
          'XL': 40,
          'XC': 90,
          'CD': 400,
          'CM': 900
        }

        i = conv = 0 
        while i < len(s): 
          curr = s[i] 
          if i+1 < len(s): 
            next = s[i+1] 
            val = roman.get(curr+next) 
            if val: 
              conv += val 
              i+=1 
            else: 
              conv += roman.get(curr) 
          else: 
            conv += roman.get(curr) 
          i+=1 

        return conv 

print(Solution().romanToInt("MCMXCIV"))

        
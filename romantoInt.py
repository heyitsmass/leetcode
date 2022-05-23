class Solution:
    def romanToInt(self, s: str) -> int:
        if len(s) < 1 or len(s) > 15:
          raise Exception 

        conv = 0 

        legal = ('I', 'V', 'X', 'L', 'C', 'D', 'M', 'IV', 'IX', 'XL', 'XC', 'CD', 'CM') 

        roman = { 
          'I': 1,
          'V': 5,
          'X': 10, 
          'L': 50, 
          'C': 100, 
          'D': 500, 
          'M': 1000
        }
        
        i = 0

        while i < len(s): 
          curr = s[i]
          if i+1 < len(s): 
            next = s[i+1] 
            if curr + next in legal: 
              conv += roman[next] - roman[curr] 
              i+=1 
            elif curr in legal:
              conv += roman[curr]
            else: 
              raise Exception
          else: 
            if curr in legal:
              conv += roman[curr] 
            else: 
              raise Exception 
          i+=1 

        if conv < 1 or conv > 3999: 
          raise Exception 

        return conv 








Solution().romanToInt('LXIII') 
        
        
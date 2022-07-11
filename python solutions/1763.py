class Solution:
    def longestNiceSubstring(self, s: str) -> str:
      substrings = self._substrings(s) 
      if len(substrings) > 0: 
        return max(substrings, key=len)
      else: 
        return "" 

    def _substrings(self, s): 
      ret = list() 
      n = len(s)
      for i in range(0, n): 
        tmp = "" 
        for j in range(i, n):
          tmp+=s[j]
          if len(tmp) > 1 and self._isNice(tmp): 
            ret.append(tmp) 
      return ret 
    
    def _isNice(self, s:str): 
      for letter in s: 
        if letter.isupper(): 
          if letter.lower() not in s: 
            return False 
        else: 
          if letter.upper() not in s: 
            return False 
      return True 

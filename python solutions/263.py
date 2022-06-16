class Solution:
    def isUgly(self, n: int) -> bool:

      mods = [2, 3, 5]

      ret = [] 

      i = 0 
      while n >= 1: 

        if n == 1: 
          return True 
        
        tmp = n / mods[i] 

        if tmp.is_integer():
          n = tmp 
        else: 
          if i + 1 < len(mods): 
            ret.append(mods[i]) 
            i+=1 
            continue
          return False  

      if len(ret) > 1: 
        return True 
      return False   
 

cases = [ 
  6, 1, 14, 2147483648, -2147483648
]

for case in cases: 
  print(Solution().isUgly(case))
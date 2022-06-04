class Solution:
    def myAtoi(self, s: str) -> int:
      _max = pow(2, 31) - 1
      _min = (_max + 1) * -1
      ret = '' 
      sign = 1 
      flag = False 
      for char in s: 
        if char in [' ', '+', '-'] and not ret and not flag:
          if char == '-': 
            sign = -1 
            flag = True 
          elif char == '+': 
            flag = True  
          continue 
        elif char.isdigit(): 
          ret += char 
        else: 
          break  
      
      if ret: 
        ret = int(ret) * sign 
        if ret < _min:
          return _min
        elif ret > _max:
          return _max
        else: 
          return ret

      return 0 

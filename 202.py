class Solution:
  def isHappy(self, n:int) -> bool: 
    i = 0

    while i <= 1000: 
      if n == 1: 
        break  
      
      converted = str(n) 

      tmp = [] 

      for char in converted: 
        num = int(char) 
        tmp.append(num**2) 

      new = 0

      for num in tmp: 
        new += num 

      n = new
      i+=1 

    return True if i < 1000 else False 
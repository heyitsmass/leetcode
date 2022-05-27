class Solution:
  def findRepeatedDnaSequences(self, s: str) -> list:
    nucleotides = ['A', 'C', 'G', 'T'] 

    if len(s) > pow(10, 5): raise Exception 
    
    for char in s: 
      if char not in nucleotides: 
        raise Exception  

    tmp = dict() 

    for i in range(len(s)-9): 
      curr = s[i:i+10] 
      
      if curr not in tmp.keys(): 
        tmp[curr] = 1
      else: 
        tmp[curr] += 1 

    return [key for key in tmp if tmp[key] > 1]

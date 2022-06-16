from math import factorial
import random
class Solution:
  def isScramble(self, s1: str, s2: str) -> bool:
    length = len(s1)
    if length <= 1 and s1 == s2: 
      return True 
    else: 

      tmp = list()
      
      num_entries = self.numScrambles(s1) 


      while len(tmp) <= num_entries: 
        ret = self.getScramble(s1) 
        if ret == s2: 
          return True 

        if ret not in tmp: 
          tmp.append(ret)  

      
      return s2 in tmp 

  def getScramble(self, s1: str) -> str: 
    if len(s1) <= 1: 
      return s1 

    index = random.randrange(1, len(s1)) 

    x = s1[0:index] 
    y = s1[index:len(s1)] 

    if not random.randrange(0, 100) % 2: 
      tmp = x 
      x = y 
      y = tmp 
    
    return self.getScramble(x) + self.getScramble(y) 

  def numScrambles(self, string): 
    check = dict() 

    for char in string: 
      if char in check.keys(): 
        check[char] += 1 
      else: 
        check[char] = 1 

    div = 1

    for key in check: 
      div *= factorial(check[key]) 
    
    return int(factorial(len(string)) / div)



def repetitive_test(): 
  cases = [
    #("great", "rgeat", True),
    #("abcde", "caebd", False), 
    #("a", "b", False), 
    #("aa", "aa", True),
    #("aaa", "aaa", True),
    #("aaaa", "aaaa", True),
    #("abcdefg", "efghijc", False),
    #("abcdefghij", "efghijcadb", False),
    ("abcdbdacbdac", "bdacabcdbdac", True),
    #("great", "gtrae", True),
    ("abcdefghijklmnopq", "efghijklmnopqcadb", False)
  ]

  for case in cases: 
    print(Solution().isScramble(case[0], case[1])) 


repetitive_test()
import random 

global curr 
class Solution:
  def isScramble(self, s1: str, s2: str, curr: int) -> bool:
    length = len(s1)
    if length <= 1 and s1 == s2: 
      return True 
    else: 

      for i in range(pow(length* length-1,2)+(length* length-1)):

        tmp = self.getScramble(s1)

        if tmp == s2: 
          return True 
      
      return False 


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




def test(k, cases, curr): 
  for i in range(20): 
    print(f"************* ({k}: {i} ) *************")
    for case in cases: 
      s1 = case[0]
      s2 = case[1]
      ret = Solution().isScramble(s1, s2, curr)
      print(f"{s1=}, {s2=} :", ret)

      if ret != case[2]:
        return False 
  return True 


def repetitive_test(k: int): 
  cases = [
    ("great", "rgeat", True),
    ("abcde", "caebd", False), 
    ("a", "b", False), 
    ("aa", "aa", True),
    ("aaa", "aaa", True),
    ("aaaa", "aaaa", True),
    ("abcdefg", "efghijc", False),
    ("abcdefghij", "efghijcadb", False),
    ("abcdbdacbdac", "bdacabcdbdac", True),
    ("great", "gtrae", True),
    ("abcdefghijklmnopq", "efghijklmnopqcadb", False)
  ]

  cases = [ 
    ("abcdefghijklmnopq", "efghijklmnopqcadb", False)
  ]
  curr = 1
  print(f"************* ( TEST {k} ) *************")
  return test(k, cases, curr)




i = 0
for i in range(20): 

  if not repetitive_test(i):
    raise Exception 
  
  print(f"************* ( PASSED ) *************")




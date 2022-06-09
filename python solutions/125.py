import re 

class Solution:
  def isPalindrome(self, s: str) -> bool:
    
    tmp = re.split(r'([a-zA-Z0-9])', re.sub(r'[^a-zA-Z0-9]', '', s).lower())

    tmp = list(filter(None, tmp)) 

    print(tmp, tmp[::-1]) 

    return tmp == tmp[::-1]


import re 

class Solution:
  def isPalindrome(self, s: str) -> bool:
    
    tmp = re.sub(r'[^a-zA-Z0-9]', '', s).lower()

    return tmp == tmp[::-1]



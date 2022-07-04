class Solution:
  def firstUniqChar(self, s: str) -> int:
    _dict = {} 
    for char in s: 
      if char in _dict.keys(): 
        _dict[char] += 1 
      else: 
        _dict[char] = 1 

    letter = min(_dict, key=_dict.get)
    
    return s.index(letter) if _dict[letter] == 1 else -1 
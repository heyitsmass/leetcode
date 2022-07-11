class Solution:
  def findLucky(self, arr: list) -> int:
    _dict={} 
    for num in arr:
      if num in _dict.keys(): 
        _dict[num] += 1 
      else: 
        _dict[num] = 1 
    
    largest = 0
    for key in _dict: 
      if _dict[key] >= largest and _dict[key] == key: 
        largest = key 
    
    return largest if largest else -1 
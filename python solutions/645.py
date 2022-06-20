class Solution:
  def findErrorNums(self, nums):
    map = dict() 
    ret = list()  

    for i, num in enumerate(nums): 
      if i+1 not in map.keys(): 
        map[i+1] = 0 


      if num in map.keys(): 
        map[num] += 1 
        if map[num] > 1: 
          ret.insert(0, num)  
      else: 
        map[num] = 1 
    
    for key in map: 
      if not map[key]: 
        ret.append(key) 

    return ret 


  
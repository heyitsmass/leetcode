class Solution:
  def majorityElement(self, nums:list) -> list:

    table = {} 
    ret = [] 
    lim = len(nums)/3

    for num in nums: 
      
      if num in table.keys(): 
        table[num] += 1 
      else: 
        table[num] = 1 

      if table[num] > lim and num not in ret: 
        ret.append(num)  
    
    return ret  


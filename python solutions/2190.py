class Solution:
  def mostFrequent(self, nums: list[int], key: int) -> int:
    targets = {} 

    target = None 

    for i in range(len(nums)-1): 
      curr = nums[i] 
      next = nums[i+1] 

      if curr == key: 
        if next not in targets.keys(): 
          targets[next] = 1 
          if not target: 
            target = (next, targets[next])  
        else: 
          targets[next] += 1 
          if target and targets[next] > target[1]: 
            target = (next, targets[next]) 
      
    return target[0] 


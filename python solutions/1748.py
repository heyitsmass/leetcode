class Solution:
  def sumOfUnique(self, nums: list) -> int:
    
    i = 0
    _sum = 0
    while i < len(nums): 
      num = nums[i] 
      if num not in nums[i+1:len(nums)]: 
        _sum += num
      else: 
        nums = list(filter(lambda x: x != num, nums) ) 
        continue
      i+=1 

    return _sum 
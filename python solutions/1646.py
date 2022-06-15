class Solution:
    def getMaximumGenerated(self, n: int) -> int:
      nums = [] 

      for i in range(n+1):
        if not i: 
          nums.append(0) 

        if i == 1: 
          nums.append(1) 
        
        if 2 <= 2*i <= n: 
          nums.append(nums[i]) 
          
        if 2 <= 2*i+1 <= n: 
          nums.append(nums[i] + nums[i+1]) 

      return max(nums)

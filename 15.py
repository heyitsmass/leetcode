class Solution:
  def threeSum(self, nums: list([int])) -> list(list([int])):

    ret = list() 

    for i in range(len(nums) - 2): 
      j = i + 1
      k = len(nums) - 1 

      while j < k: 
        sum = nums[i] + nums[j] + nums[k] 
      
        if not sum: 
          arr = [nums[i], nums[j], nums[k]] 
          if arr not in ret: 
            ret.append(arr)

          j += 1
          k -= 1
        elif sum < 0: 
          j += 1 
        else: 
          k -= 1

    return ret 
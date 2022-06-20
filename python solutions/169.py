class Solution:
  def majorityElement(self, nums:list) -> int:
    map = {} 
    for num in nums: 
      if num in map.keys(): 
        map[num] += 1
      else: 
        map[num] = 1

    return max(map, key=map.get)

  """ Optimal Solution
  def majorityElement(self, nums:list) -> int: 
    nums.sort() 
    return nums[len(nums)//2]
  
  """


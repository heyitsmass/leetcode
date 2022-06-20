class Solution:
    def containsDuplicate(self, nums:list) -> bool:
        map = {}
        for num in nums: 
          if num in map.keys(): 
            return True 
          else: 
            map[num] = 1 
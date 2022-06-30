class Solution:
  def intersection(self, nums1: list, nums2: list) -> list:

    larger = list(set(nums1)) 
    smaller = list(set(nums2))  

    if len(nums1) < len(nums2): 
      larger, smaller = smaller, larger 

    intersection = [] 

    for num in smaller: 
      if num in larger: 
        intersection.append(num) 

    return intersection 

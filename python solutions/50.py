class Solution:

  def myPow(self, x:float, n:int) -> float: 
    return pow(x, n) 
    





cases = [ 
  #(2.0, 10), 
  #(2.1, 15), 
  #(4.3, 7), 
  (2, -3),
  (2, -2), 
  #(0.44258, 0)
]

for case in cases: 
  print(Solution().myPow(case[0], case[1]))  
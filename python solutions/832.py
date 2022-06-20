class Solution:
  def flipAndInvertImage(self, image:list):
    flipped = [i[::-1] for i in image] 

    inverted = [] 

    for arr in flipped: 
      tmp = [] 
      for item in arr: 
        if not item: 
          tmp.append(1) 
        else: 
          tmp.append(0)  
          
      inverted.append(tmp)  

    return inverted



cases = [ 
  [[1,1,0],[1,0,1],[0,0,0]], 
  [[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]
]

for case in cases: 
  print(Solution().flipAndInvertImage(case))  

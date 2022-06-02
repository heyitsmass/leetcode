class Solution:
    def transpose(self, matrix):
      ret = list()
      i = 0
      if len(matrix) == len(matrix[0]): 
        for i in range(len(matrix)): 
          tmp = list()
          for j in range(len(matrix[i])): 
            tmp.append(matrix[j][i])  
          ret.append(tmp) 
      elif len(matrix) < len(matrix[0]):
        for j in range(len(matrix[i])):
          tmp = list()
          for i in range(len(matrix)):
            tmp.append(matrix[i][j])
          ret.append(tmp)  
      else: 
        for j in range(len(matrix[i])): 
          tmp = list() 
          for i in range(len(matrix)):
             tmp.append(matrix[i][j]) 
          ret.append(tmp) 
      return ret 

      
      


cases = [ 
  [[1,2,3],[4,5,6],[7,8,9]], 
  [[1,2,3],[4,5,6]], 
  [[1,2],[3, 4],[5, 6]]
]

for case in cases: 
  print(Solution().transpose(case)) 


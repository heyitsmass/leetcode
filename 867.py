class Solution:
  def transpose(self, matrix: list(list([int]))) ->  list(list([int])):
    ret = list()
    i = 0
    if len(matrix) == len(matrix[0]): 
      for i in range(len(matrix)): 
        tmp = list()
        for j in range(len(matrix[i])): 
          tmp.append(matrix[j][i])  
        ret.append(tmp) 
    else: 
      for j in range(len(matrix[i])): 
        tmp = list() 
        for i in range(len(matrix)):
            tmp.append(matrix[i][j]) 
        ret.append(tmp) 
    return ret 


class Solution:
  def searchMatrix(self, matrix, target: int) -> bool:
    for sub_matrix in matrix: 
      if target in sub_matrix: 
        return True 
    return False  


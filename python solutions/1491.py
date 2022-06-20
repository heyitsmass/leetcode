class Solution:
  def average(self, salary: list) -> float:
    salary.sort()       
    avg = 0 
    
    for i in range(1, len(salary)-1): 
      avg += salary[i]
    
    avg /= len(salary)-2 

    return avg 
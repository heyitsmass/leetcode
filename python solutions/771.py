class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
      table = {} 
      for char in jewels: 
        table[char] = 0 
      
      for stone in stones: 
        if stone in table.keys(): 
          table[stone] += 1 

      return sum(list(table.values()))

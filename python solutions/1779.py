class Solution:
  def nearestValidPoint(self, x: int, y: int, points: list) -> int:
    manhattanDistances = {} 

    for i, point in enumerate(points): 

      if point[0] == x or point[1] == y or  point[0] == x and point[1] == y: 
        manhattanDistances[i] = abs(x - point[0]) + abs(y - point[1])

    return min(manhattanDistances, key=manhattanDistances.get) if len(manhattanDistances) > 0 else -1 
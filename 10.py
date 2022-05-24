"""

  1. 1 <= s.length <= 20
  2. 1 <= p.length <= 30
  3. s contains only lowercase English letters.
  4. p contains only lowercase English letters, '.', and '*'.

  It is guaranteed for each appearance of the character '*', there will be a previous valid character to match.

"""

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        ...





print(Solution().isMatch("aa", p="a"))

#print(Solution().isMatch("aa", p="a*"))

#print(Solution().isMatch("ab", p=".*"))
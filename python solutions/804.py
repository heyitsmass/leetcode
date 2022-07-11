class Solution:
  def uniqueMorseRepresentations(self, words: list) -> int:

    latin = [".-","-...","-.-.","-..",".","..-.","--.","....","..",
              ".---","-.-",".-..","--","-.","---",".--.","--.-",".-.",
              "...","-","..-","...-",".--","-..-","-.--","--.."]
    _words = {}
    for w in words: 
      morse = ""
      for l in w: 
        morse += latin[ord(l)-97]
      
      _words[morse] = 1 

    return len(_words.keys()) 



class Solution:
  def findWords(self, words: list) -> list:

    _keyboard = { 
      1 : 'qwertyuiop', 
      2 : 'asdfghjkl', 
      3 : 'zxcvbnm'
    }

    row = 0 
    ret = [] 

    for word in words: 
      for line in _keyboard: 
        if word[0].lower() in _keyboard[line]: 
          row = line 

      tmp = "" 
      for letter in word: 
        if letter.lower() in _keyboard[row]: 
          tmp += letter 

      if word == tmp: 
        ret.append(word) 
    
    return ret 


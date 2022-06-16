#include <iostream> 
#include <math.h> 

class Solution {
public:
    bool judgeSquareSum(int c) {
        for(long a = 0; a * a <= c; a++){ 
          double num = sqrt(c - pow(a, 2));
          if ((num - int(num)) == 0 || (num - long(num)) == 0)
            return true; 
        }
        return false; 
    }
};

int main(){ 
  return 0; 
}
#include <iostream> 
#include <vector> 

class Solution {
public:
    std::vector<int> runningSum(std::vector<int>& nums) { 

        for (int i = 1; i < nums.size(); i++){ 
          nums[i] += nums[i-1];
        }

        return nums;
      
    }
};

int main(){ 
  return 0; 
}

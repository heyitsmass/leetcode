#include <vector> 
class Solution {
public:
    std::vector<int> twoSum(std::vector<int>& nums, int target) {
        std::vector<int> tmp; 

        for(int i = 0; i < nums.size(); i++){ 
          for(int j = i+1; j < nums.size(); j++){ 
            if (nums[i] + nums[j] == target) { 
              tmp.push_back(i); 
              tmp.push_back(j); 
              return tmp; 
            }
          }
        }
      return tmp; 
    }
};

int main(){ 
  return 0; 
}
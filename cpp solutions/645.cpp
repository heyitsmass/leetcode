#include <iostream> 
#include <vector> 
#include <unordered_map> 

class Solution {
public:
    std::vector<int> findErrorNums(std::vector<int>& nums) {
        std::vector<int> ret;  
        std::unordered_map<int, int> hashMap; 

        for(int i = 1; i <= nums.size(); i++){ 
          
          if(!hashMap[i])
            hashMap[i] = 0;  

          if (hashMap[nums[i-1]] >= 1){ 
            hashMap[nums[i-1]] += 1;
            ret.insert(ret.begin(), nums[i-1]); 
          } else { 
            hashMap[nums[i-1]] = 1;
          }
        }


        for(int i = 1; i <= hashMap.size(); i++)
          if(!hashMap[i]) ret.push_back(i);  
      
        return ret;
    }
};

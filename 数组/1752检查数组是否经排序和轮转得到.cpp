#include<iostream>
#include<vector>
using namespace std;

# 调试了三遍才出来结果的简单题

class Solution {
public:
    bool check(vector<int>& nums) {
        int n = nums.size(), last_val = INT_MIN, highest_val = INT_MAX;
        bool flag = true;
        for (int i = 0; i<n; ++i){
            if (flag){
                if (last_val > nums[i]){
                    flag = false;
                    highest_val = nums[0];
                    if (nums[i] > highest_val){
                        return false;
                    }
                }
                last_val = nums[i];
            }else{
                if (last_val > nums[i] || nums[i] > highest_val){
                    return false;
                }else{
                    last_val = nums[i];
                }
            }
            // cout << nums[i] << ' '<< last_val << ' ' << highest_val << endl;
        }
        return true;
    }
};


// 简单题，但要考虑清楚所有情况
class Solution {
public:
    bool check(vector<int>& nums) {
        int n = nums.size(), x = 0;
        for (int i = 1; i < n; ++i) {
            if (nums[i] < nums[i - 1]) {
                x = i;
                break;
            }
        }
        if (x == 0) {
            return true;
        }
        for (int i = x + 1; i < n; ++i) {
            if (nums[i] < nums[i - 1]) {
                return false;
            }
        }
        return nums[0] >= nums[n - 1];
    }
};

//作者：LeetCode-Solution
//链接：https://leetcode.cn/problems/check-if-array-is-sorted-and-rotated/solution/jian-cha-shu-zu-shi-fou-jing-pai-xu-he-l-cbqk/
//来源：力扣（LeetCode）
//著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
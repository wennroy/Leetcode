#include<iostream>
#include<vector>
#include<time>
using namespace std;

// 暴力单调栈做法，时间复杂度理论上O(n)
class Solution {
public:
    int numSubarrayBoundedMax(vector<int>& nums, int left, int right) {
        vector<int> st;
        int n = nums.size(), ans = 0;
        vector<vector<int>> record(n, {0,0});
        if (n == 1){
            return nums[0] >= left && nums[0] <= right ? 1 : 0;
        }
        for (int i=0; i<n; ++i){
            while (!st.empty() && nums[st.back()] <= nums[i]){
                int j = st.back();
                st.pop_back();
                record[j][1] = i;
            }
            record[i][0] = !st.empty() ? st.back() : -1;
            st.push_back(i);
        }
        for (int i=0; i<st.size(); ++i){
            record[st[i]][1] = n;
        }

        for (int i=0; i<n; ++i){
            if (nums[i] >= left && nums[i] <= right){
                ans += (i - record[i][0]) * (record[i][1] - i);
            }
        }
        return ans;
    }
};


// 双指针
class Solution {
public:
    int numSubarrayBoundedMax(vector<int>& nums, int left, int right) {
        int res = 0, last2 = -1, last1 = -1;
        for (int i = 0; i < nums.size(); i++) {
            if (nums[i] >= left && nums[i] <= right) {
                last1 = i;
            } else if (nums[i] > right) {
                last2 = i;
                last1 = -1;
            }
            if (last1 != -1) {
                res += last1 - last2;
            }
        }
        return res;
    }
};

// 计数
class Solution {
public:
    int numSubarrayBoundedMax(vector<int>& nums, int left, int right) {
        return count(nums, right) - count(nums, left - 1);
    }

    int count(vector<int>& nums, int lower) {
        int res = 0, cur = 0;
        for (auto x : nums) {
            cur = x <= lower ? cur + 1 : 0;
            res += cur;
        }
        return res;
    }
};

int main(){
    Solution sol;
    vector<int> array = {2,0,2,5,6};
    int left = 2, right = 8;
    clock_t start, end;
    start = clock();
    sol::numSubarrayBoundedMax(array, left, right);
    end = clock();
    cout << "Time = " << double(end-start)/CLOCKS_PER_SEC<<"s"<<endl;
}
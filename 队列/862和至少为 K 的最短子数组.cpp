#include<iostream>
#include<vector>
#include<algorithm>
#include<cstdio>
#include<queue>
using namespace std;

// 超时写法，On2时间复杂度，C++都超时了。
class Solution {
public:
    int shortestSubarray(vector<int>& nums, int k) {
        int n = nums.size(), ans = n+1;
        vector<int> pref(n+1);
        pref[0] = 0;
        for (int i=1; i < n+1; ++i){
            pref[i] = pref[i-1] + nums[i-1];
        }

        for (int i=0; i<n+1; ++i){
            for (int j=i+1; j < min(i+ans+1, n+1); ++j){
                if (pref[j] - pref[i] >= k){
                    ans = min(ans, j-i);
                    break;
                }
            }
        }
        if (ans==n+1) return -1;
        return ans;
    }
};


// 根据答案小改的hhh队列

class Solution {
public:
    int shortestSubarray(vector<int>& nums, int k) {
        int n = nums.size(), ans = n+1;
        vector<long long> pref(n+1);
        deque<long long> q;
        pref[0] = 0;
        for (int i=1; i < n+1; ++i){
            pref[i] = pref[i-1] + nums[i-1];
        }

        for (int i=0; i<n+1; ++i){
            long long val = pref[i];  // 前缀和的值
            while (!q.empty() && pref[q.back()] >= val ){
                q.pop_back(); // 把前缀和比val大的值都弹出去，因为寻找最短的子数组，一定是大的前缀和值-小的值
            }
            while (!q.empty() && (val - pref[q.front()] >= k)){
                int idx = q.front();
                ans = min(ans, i - idx);
                q.pop_front();
            }
            q.push_back(i);
        }
        if (ans==n+1) return -1;
        return ans;
    }
};



class Solution {
public:
    int shortestSubarray(vector<int>& nums, int k) {
        int n = nums.size();
        vector<long> preSumArr(n + 1);
        for (int i = 0; i < n; i++) {
            preSumArr[i + 1] = preSumArr[i] + nums[i];
        }
        int res = n + 1;
        deque<int> qu;
        for (int i = 0; i <= n; i++) {
            long curSum = preSumArr[i];
            while (!qu.empty() && curSum - preSumArr[qu.front()] >= k) {
                res = min(res, i - qu.front());
                qu.pop_front();
            }
            while (!qu.empty() && preSumArr[qu.back()] >= curSum) {
                qu.pop_back();
            }
            qu.push_back(i);
        }
        return res < n + 1 ? res : -1;
    }
};

// 作者：LeetCode-Solution
// 链接：https://leetcode.cn/problems/shortest-subarray-with-sum-at-least-k/solution/he-zhi-shao-wei-k-de-zui-duan-zi-shu-zu-57ffq/
// 来源：力扣（LeetCode）
// 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
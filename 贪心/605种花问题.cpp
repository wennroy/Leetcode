#include<iostream>
#include<vector>
#include<algorithm>
#include<cstdio>
#include<queue>
using namespace std;

class Solution {
public:
    bool canPlaceFlowers(vector<int>& flowerbed, int n) {
        flowerbed.push_back(0);
        if (!n){
            return true;
        }

        if (!flowerbed[0] && !flowerbed[1]){
            n--;
            flowerbed[0] = 1;
        }
        for (int i = 1; i<flowerbed.size() - 1; ++i){
            if (flowerbed[i]){
                continue;
            }
            if (!n){
                break;
            }
            if (!(flowerbed[i-1] || flowerbed[i+1])){
                flowerbed[i] = 1;
                n--;
            }
        }
        return !n;
    }
};

// 标答贪心
class Solution {
public:
    bool canPlaceFlowers(vector<int>& flowerbed, int n) {
        int count = 0;
        int m = flowerbed.size();
        int prev = -1;
        for (int i = 0; i < m; ++i) {
            if (flowerbed[i] == 1) {
                if (prev < 0) {
                    count += i / 2;
                } else {
                    count += (i - prev - 2) / 2;
                }
                prev = i;
            }
        }
        if (prev < 0) {
            count += (m + 1) / 2;
        } else {
            count += (m - prev - 1) / 2;
        }
        return count >= n;
    }
};

//作者：LeetCode-Solution
//链接：https://leetcode.cn/problems/can-place-flowers/solution/chong-hua-wen-ti-by-leetcode-solution-sojr/
//来源：力扣（LeetCode）
//著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
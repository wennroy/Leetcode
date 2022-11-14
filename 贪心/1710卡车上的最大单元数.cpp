#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;

// 贪心，nlogn时间复杂度
class Solution {
public:
    int maximumUnits(vector<vector<int>>& boxTypes, int truckSize) {
        sort(boxTypes.begin(), boxTypes.end(), [&](vector<int> a, vector<int> b){
            return a[1] > b[1] || (a[1] == b[1] && a[0] > b[0]);
        });

        int box_num = 0, ans = 0, i = 0, n = boxTypes.size();
        while(i < n){
            if (boxTypes[i][0] + box_num <= truckSize){
                ans += boxTypes[i][1] * boxTypes[i][0];
                box_num += boxTypes[i][0];
            }else{
                ans += boxTypes[i][1] * (truckSize - box_num);
                break;
            }
            ++i;
        };
        return ans;
    };
};


class Solution {
public:
    int maximumUnits(vector<vector<int>>& boxTypes, int truckSize) {
        sort(boxTypes.begin(), boxTypes.end(), [](const vector<int> &a, const vector<int> &b) {
            return a[1] > b[1];
        });
        int res = 0;
        for (auto &boxType : boxTypes) {
            int numberOfBoxes = boxType[0];
            int numberOfUnitsPerBox = boxType[1];
            if (numberOfBoxes < truckSize) {
                res += numberOfBoxes * numberOfUnitsPerBox;
                truckSize -= numberOfBoxes;
            } else {
                res += truckSize * numberOfUnitsPerBox;
                break;
            }
        }
        return res;
    }
};

//作者：LeetCode-Solution
//链接：https://leetcode.cn/problems/maximum-units-on-a-truck/solution/qia-che-shang-de-zui-da-dan-yuan-shu-by-ynaqv/
//来源：力扣（LeetCode）
//著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。


class Solution {
public:
    int maximumUnits(vector<vector<int>>& boxTypes, int truckSize) {
        const int n = boxTypes.size();
        int sum = 0;
        int l = 0, r = n;
        const auto ptr = boxTypes.data();
        const auto cmp = [&] (const vector<int>& box1, const vector<int>& box2) {
            return box1[1] > box2[1];
        };
        while (l < r) {
            const int mid = (l + r) / 2;
            nth_element(ptr + l, ptr + mid, ptr + r, cmp);
            int nsum = sum;
            for (int i = l;i < mid;++i)
                nsum += ptr[i][0];
            if (truckSize <= nsum)
                r = mid;
            else {
                sum = nsum + ptr[mid][0];
                l = mid + 1;
            }
        }
        int ans = 0;
        for (int i = 0;i < l;++i)
            ans += ptr[i][0] * ptr[i][1];
        if (sum > truckSize) ans -= (sum - truckSize) * ptr[l - 1][1];
        return ans;
    }
};
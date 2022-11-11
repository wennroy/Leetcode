#include<iostream>
#include<vector>
#include<string>
using namespace std;

// 菜鸡的写法
class Solution {
public:
    bool halvesAreAlike(string s) {
        vector<char> yuan = {'a','e','i','o','u','A','E','I','O','U'};
        int n = s.size(), ans1 = 0, ans2 = 0;
        for (int i=0; i<n/2; ++i){
            char a = s[i];
            if (find(yuan.begin(), yuan.end(), a) != yuan.end()){
                ans1++;
            }
        }
        for (int i=n/2; i<n; ++i){
            char a = s[i];
            if (find(yuan.begin(), yuan.end(), a) != yuan.end()){
                ans2++;
            }
        }
        return ans1==ans2;
    }
};

// s.substr 可以直接将字符串切成想要的份数

class Solution {
public:
    bool halvesAreAlike(string s) {
        string a = s.substr(0, s.size() / 2);
        string b = s.substr(s.size() / 2);
        string h = "aeiouAEIOU";
        int sum1 = 0, sum2 = 0;
        for (int i = 0; i < a.size(); i++) {
            if (h.find_first_of(a[i]) != string::npos) {
                sum1++;
            }
        }
        for (int i = 0; i < b.size(); i++) {
            if (h.find_first_of(b[i]) != string::npos) {
                sum2++;
            }
        }
        return sum1 == sum2;
    }
};

//作者：LeetCode-Solution
//链接：https://leetcode.cn/problems/determine-if-string-halves-are-alike/solution/pan-duan-zi-fu-chuan-de-liang-ban-shi-fo-d21g/
//来源：力扣（LeetCode）
//著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
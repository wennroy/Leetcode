#include<iostream>
#include<string>
#include<unordered_map>
using namespace std;

// 菜鸡写法
class Solution {
public:
    string customSortString(string order, string s) {
        int m = order.size();
        unordered_map<char, int> um;
        string ans;
        for (char x: s){
            um[x]++;
        }
        for (int i=0; i<m; ++i){
            char o = order[i];
            if (um.find(o) != um.end()){
                string temp(um[o], o);
                ans += temp;
                um.erase(o);
            }
        }
        for (auto x: um){
            string temp(x.second, x.first);
            ans += temp;
        }
        return ans;
    }
};


// 自定义排序，c++ sort指令
class Solution {
public:
    string customSortString(string order, string s) {
        vector<int> val(26);
        for (int i = 0; i < order.size(); ++i) {
            val[order[i] - 'a'] = i + 1;
        }
        sort(s.begin(), s.end(), [&](char c0, char c1) {
            return val[c0 - 'a'] < val[c1 - 'a'];
        });
        return s;
    }
};

//作者：LeetCode-Solution
//链接：https://leetcode.cn/problems/custom-sort-string/solution/zi-ding-yi-zi-fu-chuan-pai-xu-by-leetcod-1qvf/
//来源：力扣（LeetCode）
//著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

// 计数排序
// 可以直接 ans += string(freq[ch - 'a'], ch)
// 基本与我的解法一模一样
class Solution {
public:
    string customSortString(string order, string s) {
        vector<int> freq(26);
        for (char ch: s) {
            ++freq[ch - 'a'];
        }
        string ans;
        for (char ch: order) {
            if (freq[ch - 'a'] > 0) {
                ans += string(freq[ch - 'a'], ch);
                freq[ch - 'a'] = 0;
            }
        }
        for (int i = 0; i < 26; ++i) {
            if (freq[i] > 0) {
                ans += string(freq[i], i + 'a');
            }
        }
        return ans;
    }
};

// auto&& [k,v] : mp
// 直接读取哈希表的数值
class Solution {
public:
    string customSortString(string order, string s) {
        string ans = "";
        unordered_map<char, int> mp;
        for(auto& ch : s) {
            ++mp[ch];
        }
        for(auto& ch : order) {
            if(mp.count(ch)) {
                ans += move(string(mp[ch], ch));
                mp[ch] = 0;
            }
        }
        for(auto&& [k, v] : mp) {
            if(v > 0) {
                ans += move(string(v, k));
            }
        }
        return ans;
    }
};

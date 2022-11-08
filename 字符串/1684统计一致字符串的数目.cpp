#include<vector>
#include<iostream>
#include<unordered_map>
using namespace std;

class Solution {
public:
    int countConsistentStrings(string allowed, vector<string>& words) {
        int ans = 0, n = allowed.size();
        unordered_map<char, int> map;
        for (int i=0; i<n; ++i){
            if (map.find(allowed[i]) == map.end()){
                map.insert(make_pair(allowed[i], 1));
            }
        }
        for (auto word: words){
            for (auto x: word){
                if (map.find(x) == map.end()){
                    ans--;
                    break;
                }
            }
            ans++;
        }
        return ans;
    }
};

// 一些大佬们的快速写法

class Solution {
public:
    int countConsistentStrings(string allowed, vector<string>& words) {
        bitset<26> bs;
        for(char c : allowed) bs[c-'a'] = 1;
        int k = words.size();
        for(const auto& word : words) {
            for(char c : word) {
                if(!bs[c-'a']) {
                    k--;
                    break;
                }
            }
        }
        return k;
    }
};

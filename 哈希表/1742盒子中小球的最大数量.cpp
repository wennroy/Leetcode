#include<iostream>
#include<vector>
#include<unordered_map>
#include<string>
using namespace std;

class Solution {
public:
    int countBalls(int lowLimit, int highLimit) {
        unordered_map<int, int> basket;
        int ans = 0;
        for (int num = lowLimit; num <= highLimit; num ++){
            int val = 0, cur_num = num;
            while (cur_num > 0){
                val += cur_num % 10;
                cur_num /= 10;
            }
            basket[val] += 1;
        }

        for (auto x: basket){
            ans = max(x.second, ans);
        }
        return ans;
    }
};

// 数位DP，经典大炮轰鸟
class Solution {
public:
    string low,high;
    vector<int> f;
    int countBalls(int lowLimit, int highLimit) {
        lowLimit--;
        while(lowLimit){
            char c = lowLimit%10+'0';
            low=c+low;
            lowLimit/=10;
        }
        while(highLimit){
            char c = highLimit%10+'0';
            high=c+high;
            highLimit/=10;
        }
        f=vector<int>(55,0);
        solv(0,1,1,0,high);
        solv(0,1,1,0,low);
        return *max_element(f.begin(),f.end());
    }
    void solv(int idx,int islimit,int isnum,int sm,string ss)
    {
        if(idx==ss.size()){
            if(ss==high) f[sm]++;
            else f[sm]--;
            return ;
        }
        int up = (islimit?ss[idx]-'0':9);
        if(!isnum) solv(idx+1,0,0,0,ss);
        for(int i=1-isnum;i<=up;i++)
        {
            solv(idx+1,(i==up)&&islimit,1,sm+i,ss);
        }
    }
};
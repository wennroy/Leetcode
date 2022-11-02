// 丑陋的暴力法
class Solution {
public:
    int maxRepeating(string sequence, string word) {
        int i,k, ans=0;
        int j=0;
        while (j < sequence.size()){
            i = 0;
            k = 0;
            int old_j = j;
            while (j < sequence.size() && sequence[j] == word[i]){
                if (i == word.size() -1){
                    k++;
                    i = -1;
                }
                j++;
                i++;
            }
            ans = max(ans, k);
            j = old_j + 1;
        }
        return ans;
    }
};


// 动态规划简单枚举
class Solution {
public:
    int maxRepeating(string sequence, string word) {
        int n = sequence.size(), m = word.size();
        if (n < m) {
            return 0;
        }

        vector<int> f(n);
        for (int i = m - 1; i < n; ++i) {
            bool valid = true;
            for (int j = 0; j < m; ++j) {
                if (sequence[i - m + j + 1] != word[j]) {
                    valid = false;
                    break;
                }
            }
            if (valid) {
                f[i] = (i == m - 1 ? 0 : f[i - m]) + 1;
            }
        }

        return *max_element(f.begin(), f.end());
    }
};

//作者：LeetCode-Solution
//链接：https://leetcode.cn/problems/maximum-repeating-substring/solution/zui-da-zhong-fu-zi-zi-fu-chuan-by-leetco-r4cp/
//来源：力扣（LeetCode）
//著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。


// KMP算法+动态规划
class Solution {
public:
    int maxRepeating(string sequence, string word) {
        int n = sequence.size(), m = word.size();
        if (n < m) {
            return 0;
        }

        vector<int> fail(m, -1);
        for (int i = 1; i < m; ++i) {
            int j = fail[i - 1];
            while (j != -1 && word[j + 1] != word[i]) {
                j = fail[j];
            }
            if (word[j + 1] == word[i]) {
                fail[i] = j + 1;
            }
        }

        vector<int> f(n);
        int j = -1;
        for (int i = 0; i < n; ++i) {
            while (j != -1 && word[j + 1] != sequence[i]) {
                j = fail[j];
            }
            if (word[j + 1] == sequence[i]) {
                ++j;
                if (j == m - 1) {
                    f[i] = (i >= m ? f[i - m] : 0) + 1;
                    j = fail[j];
                }
            }
        }

        return *max_element(f.begin(), f.end());
    }
};

//作者：LeetCode-Solution
//链接：https://leetcode.cn/problems/maximum-repeating-substring/solution/zui-da-zhong-fu-zi-zi-fu-chuan-by-leetco-r4cp/
//来源：力扣（LeetCode）
//著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
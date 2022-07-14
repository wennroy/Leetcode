# 超时写法，用两个字典树来存储，查询时花费时间过多。

class WordFilter:

    def __init__(self, words: List[str]):
        self.trie_pref = {}
        self.trie_suff = {}
        for i, word in enumerate(words):
            cur1 = self.trie_pref
            for l in word:
                if l not in cur1.keys():
                    cur1[l] = {}
                cur1 = cur1[l]
            cur1['#'] = i

            cur2 = self.trie_suff
            for l in word[::-1]:
                if l not in cur2.keys():
                    cur2[l] = {}
                cur2 = cur2[l]
            cur2['#'] = i

        # print(self.trie_pref)
        # print(self.trie_suff)

    def f(self, pref: str, suff: str) -> int:
        def dfs(cur):
            ans = []
            for nxt in cur.keys():
                if nxt == '#':
                    ans += [cur[nxt]]
                else:
                    ans += dfs(cur[nxt])

            return ans

        cur1 = self.trie_pref
        for a in pref:
            if a not in cur1:
                return -1
            cur1 = cur1[a]
        # print('1')
        ans1 = dfs(cur1)

        cur2 = self.trie_suff
        for a in suff[::-1]:
            if a not in cur2:
                return -1
            cur2 = cur2[a]

        # print('2')
        ans2 = dfs(cur2)
        # print(ans1, ans2)
        ans = -1
        if len(ans1) <= len(ans2):
            for x in ans1:
                if x in ans2:
                    ans = max(ans, x)
        else:
            for x in ans2:
                if x in ans1:
                    ans = max(ans, x)

        return ans

# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(pref,suff)

# 标答一：直接哈希表存储
class WordFilter:

    def __init__(self, words: List[str]):
        self.d = {}
        for i, word in enumerate(words):
            m = len(word)
            for prefixLength in range(1, m + 1):
                for suffixLength in range(1, m + 1):
                    self.d[word[:prefixLength] + '#' + word[-suffixLength:]] = i


    def f(self, pref: str, suff: str) -> int:
        return self.d.get(pref + '#' + suff, -1)

from itertools import zip_longest

# 字典树，但二者合一的字典树，该字典树所占空间更大

class WordFilter:

    def __init__(self, words: List[str]):
        self.trie = {}
        self.weightKey = ('#', '#')
        for i, word in enumerate(words):
            cur = self.trie
            m = len(word)
            for j in range(m):
                tmp = cur
                for k in range(j, m):
                    key = (word[k], '#')
                    if key not in tmp:
                        tmp[key] = {}
                    tmp = tmp[key]
                    tmp[self.weightKey] = i
                tmp = cur
                for k in range(j, m):
                    key = ('#', word[-k - 1])
                    if key not in tmp:
                        tmp[key] = {}
                    tmp = tmp[key]
                    tmp[self.weightKey] = i
                key = (word[j], word[-j - 1])
                if key not in cur:
                    cur[key] = {}
                cur = cur[key]
                cur[self.weightKey] = i

    def f(self, pref: str, suff: str) -> int:
        cur = self.trie
        for key in zip_longest(pref, suff[::-1], fillvalue='#'):
            if key not in cur:
                return -1
            cur = cur[key]
        return cur[self.weightKey]

# 新命令，zip_longest from itertools import zip_longest
# zip_longest('ABCD', 'xy', fillvalue='-') --> Ax By C- D-

#
# 作者：LeetCode - Solution
# 链接：https: // leetcode.cn / problems / prefix - and -suffix - search / solution / qian - zhui - he - hou - zhui - sou - suo - by - leetcod - i3ec /
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。


# 还有种写法为前后缀字典树
# // Trie 构造后缀+前缀的插入方式
# // "apple"往Trie中插入
# // #apple
# // e#apple
# // le#apple
# // ple#apple
# // pple#apple
# // apple#apple
# // 查询时:前缀为a后缀为e
# // e#a
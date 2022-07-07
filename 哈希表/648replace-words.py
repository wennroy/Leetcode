# 简单的字符串题，答案方法利用哈希表

class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        dictionary.sort(key=lambda x:len(x))
        words = sentence.split(" ")
        ans = []
        def str_equal(s,t):
            # s is root, t is word
            i = 0
            m, n = len(s), len(t)
            if m >= n:
                return False

            while i < m:
                if not s[i] == t[i]:
                    return False
                i += 1
            return True

        for word in words:
            is_word = True
            for root in dictionary:
                if str_equal(root, word):
                    ans.append(root)
                    is_word = False
                    break
            if is_word:
                ans.append(word)
        return " ".join(ans)

'''
标答1：哈希集合
'''

class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        dictionarySet = set(dictionary)
        words = sentence.split(' ')
        for i, word in enumerate(words):
            for j in range(1, len(words) + 1):
                if word[:j] in dictionarySet:
                    words[i] = word[:j]
                    break
        return ' '.join(words)

'''
标答二：字典树
'''
class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        trie = {}
        for word in dictionary:
            cur = trie
            # print(trie)
            for c in word:
                if c not in cur:
                    cur[c] = {}
                cur = cur[c]
            cur['#'] = {}

        words = sentence.split(' ')
        for i, word in enumerate(words):
            cur = trie
            for j, c in enumerate(word):
                if '#' in cur:
                    words[i] = word[:j]
                    break
                if c not in cur:
                    break
                cur = cur[c]
        return ' '.join(words)

'''
线段树：如果每次我们打印trie则有：
{}
{'c': {'a': {'t': {'#': {}}}}}
{'c': {'a': {'t': {'#': {}}}}, 'b': {'a': {'t': {'#': {}}}}}
以字典的方式，储存之后的值。这样每次我们可以用一个cursor去访问当前匹配的值，直到#为止


作者：LeetCode-Solution
链接：https://leetcode.cn/problems/replace-words/solution/dan-ci-ti-huan-by-leetcode-solution-pl6v/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''
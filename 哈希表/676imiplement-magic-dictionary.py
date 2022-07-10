
class MagicDictionary:
    # 字典树
    def __init__(self):
        self.trie = {}

    def buildDict(self, dictionary: List[str]) -> None:
        for word in dictionary:
            cur = self.trie
            for c in word:
                if c not in cur:
                    cur[c] = {}
                cur = cur[c]
            cur['#'] = {}

    def search(self, searchWord: str) -> bool:
        def dfs(cur, pos, modified) -> bool:
            if pos == len(searchWord):
                return modified and '#' in cur

            ch = searchWord[pos]
            if ch in cur.keys():
                if dfs(cur[ch], pos + 1, modified):
                    return True

            if not modified:
                for cnext in cur.keys():
                    if ch != cnext:
                        if dfs(cur[cnext], pos + 1, True):
                            return True

            return False

        return dfs(self.trie, 0, False)

# 暴力计算法
class MagicDictionary:

    def __init__(self):
        self.words = list()

    def buildDict(self, dictionary: List[str]) -> None:
        self.words = dictionary

    def search(self, searchWord: str) -> bool:
        for word in self.words:
            if len(word) != len(searchWord):
                continue

            diff = 0
            for chx, chy in zip(word, searchWord):
                if chx != chy:
                    diff += 1
                    if diff > 1:
                        break

            if diff == 1:
                return True

        return False

# 自己定义字典树进行计算
class Trie:
    def __init__(self):
        self.is_finished = False
        self.child = dict()


class MagicDictionary:

    def __init__(self):
        self.root = Trie()

    def buildDict(self, dictionary: List[str]) -> None:
        for word in dictionary:
            cur = self.root
            for ch in word:
                if ch not in cur.child:
                    cur.child[ch] = Trie()
                cur = cur.child[ch]
            cur.is_finished = True

    def search(self, searchWord: str) -> bool:
        def dfs(node: Trie, pos: int, modified: bool) -> bool:
            if pos == len(searchWord):
                return modified and node.is_finished

            ch = searchWord[pos]
            if ch in node.child:
                if dfs(node.child[ch], pos + 1, modified):
                    return True

            if not modified:
                for cnext in node.child:
                    if ch != cnext:
                        if dfs(node.child[cnext], pos + 1, True):
                            return True

            return False

        return dfs(self.root, 0, False)

'''
作者：LeetCode - Solution
链接：https: // leetcode.cn / problems / implement - magic - dictionary / solution / shi - xian - yi - ge - mo - fa - zi - dian - by - leetcode - b35s /
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''
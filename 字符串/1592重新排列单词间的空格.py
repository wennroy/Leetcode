class Solution:
    def reorderSpaces(self, text: str) -> str:
        n = len(text)
        space_count = 0
        words = []
        is_space = True
        i = -1
        for l in text:
            if is_space and l != ' ':
                i += 1
                words.append('')
                is_space = False
            if l == ' ':
                space_count += 1
                is_space = True
            else:
                words[i] += l

        m = len(words)
        if m == 1:
            return words[0] + space_count * ' '
        avg_space = space_count // (m-1)
        more = space_count % (m-1)
        i = 0
        ans = ''
        for word in words[:-1]:
            ans += word + ' '*avg_space
        ans += words[-1]
        ans += ' '*more

        return ans

# 直接模拟
class Solution:
    def reorderSpaces(self, text: str) -> str:
        words = text.split()
        space = text.count(' ')
        if len(words) == 1:
            return words[0] + ' ' * space
        per_space, rest_space = divmod(space, len(words) - 1)
        return (' ' * per_space).join(words) + ' ' * rest_space

# 作者：LeetCode-Solution
# 链接：https://leetcode.cn/problems/rearrange-spaces-between-words/solution/zhong-xin-pai-lie-dan-ci-jian-de-kong-ge-5kln/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
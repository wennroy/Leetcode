# 哈希表
from collections import defaultdict, Counter

class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        cnt = defaultdict(int)
        for cpdomain in cpdomains:
            rep, domain = cpdomain.split(' ')
            rep = int(rep)
            temp_domain = domain.split('.')
            for i in range(len(temp_domain)):
                cnt['.'.join(temp_domain[i:])] += rep
        ans = []
        for item in cnt.items():
            ans.append(str(item[1]) + ' ' + str(item[0]))

        return ans

# 标答哈希表
class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        cnt = Counter()
        for domain in cpdomains:
            c, s = domain.split()
            c = int(c)
            cnt[s] += c
            while '.' in s:
                s = s[s.index('.') + 1:]
                cnt[s] += c
        return [f"{c} {s}" for s, c in cnt.items()]

# 作者：LeetCode-Solution
# 链接：https://leetcode.cn/problems/subdomain-visit-count/solution/zi-yu-ming-fang-wen-ji-shu-by-leetcode-s-0a6i/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
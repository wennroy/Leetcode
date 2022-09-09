# 哈希表记录

from collections import defaultdict
class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        record = defaultdict(int)
        ans = 0
        for num in answers:
            record[num] += 1
            if record[num] == num + 1:
                ans += num + 1
                record.pop(num)
        for num in record.keys():
            ans += num + 1

        return ans

# 贪心
from collections import Counter
class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        count = Counter(answers)
        ans = sum((x + y) // (y + 1) * (y + 1) for y, x in count.items())
        return ans

# 作者：LeetCode-Solution
# 链接：https://leetcode.cn/problems/rabbits-in-forest/solution/sen-lin-zhong-de-tu-zi-by-leetcode-solut-kvla/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
from collections import defaultdict
class Solution:
    def unique_result(self, email: str) -> str:
        temp = email.split("@")
        local = temp[0]
        domain = temp[1]
        local = local.split("+")[0].replace(".", "")  # email[:i].split('+', 1)[0] 更换为split 一次
        return local + "@" + domain

    def numUniqueEmails(self, emails: List[str]) -> int:
        record = defaultdict(int)
        for email in emails:
            record[self.unique_result(email)] += 1

        return len(record.keys())

'''
标答 利用set来存储
'''

class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        emailSet = set()
        for email in emails:
            i = email.index('@')
            local = email[:i].split('+', 1)[0]  # 去掉本地名第一个加号之后的部分
            local = local.replace('.', '')  # 去掉本地名中所有的句点
            emailSet.add(local + email[i:])
        return len(emailSet)
'''
作者：LeetCode-Solution
链接：https://leetcode.cn/problems/unique-email-addresses/solution/du-te-de-dian-zi-you-jian-di-zhi-by-leet-f178/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''
class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        ans = [0] * n
        last_start = [0] * n
        cur_function = []
        for log in logs:
            list_log = log.split(':')
            idx, startorend, time = int(list_log[0]), list_log[1], int(list_log[2])
            if startorend == 'start':
                if cur_function:
                    ans[cur_function[-1]] += time - last_start[cur_function[-1]]   # start 不需要 + 1
                last_start[idx] = time
                cur_function.append(idx)
            elif startorend == 'end':
                ans[cur_function[-1]] += time - last_start[cur_function[-1]] + 1
                for i in range(len(cur_function)-1, -1, -1):
                    if cur_function[i] == idx:
                        cur_function = cur_function[:i] + cur_function[i+1:]
                        break
                if cur_function:
                    last_start[cur_function[-1]] = time + 1
        return ans


class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        ans = [0] * n
        st = []
        for log in logs:
            idx, tp, timestamp = log.split(':')
            idx, timestamp = int(idx), int(timestamp)
            if tp[0] == 's':
                if st:
                    ans[st[-1][0]] += timestamp - st[-1][1]
                    st[-1][1] = timestamp
                st.append([idx, timestamp])
            else:
                i, t = st.pop()
                ans[i] += timestamp - t + 1
                if st:
                    st[-1][1] = timestamp + 1
        return ans

# 作者：LeetCode-Solution
# 链接：https://leetcode.cn/problems/exclusive-time-of-functions/solution/han-shu-de-du-zhan-shi-jian-by-leetcode-d54e2/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
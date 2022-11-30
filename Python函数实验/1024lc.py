class Solution:
    def calculate_1024(self, numbers, operations):
        ans = set()
        n, m = len(numbers), len(operations)
        used_numbers = [False] * n
        used_operations = [False] * m
        def recur(i, used_numbers, used_operations, val, oper, tmp_numbers, tmp_oper):
            nonlocal ans
            # Number: 0, 2, 4, 6
            # Operations: 1, 3, 5
            # print(i,used_numbers, used_operations, val, oper)
            if i == 7:
                if val == 1024:
                    cur_numbers = [_ for _ in tmp_numbers]
                    cur_opr = [_ for _ in tmp_oper]
                    ans.add(tuple([tuple(cur_numbers), tuple(cur_opr)]))
                return
            if i % 2 == 0:
                for k in range(len(used_numbers)):
                    if used_numbers[k] == False:
                        try:
                            new_val = eval(str(val) + oper + str(numbers[k]))
                        except:
                            continue
                        used_numbers[k] = True
                        tmp_numbers.append(numbers[k])
                        recur(i+1, used_numbers, used_operations, new_val, '', tmp_numbers, tmp_oper)
                        tmp_numbers.pop()
                        used_numbers[k] = False
            else:
                for k in range(len(used_operations)):
                    if used_operations[k] == False:
                        new_opr = operations[k]
                        used_operations[k] = True
                        tmp_oper.append(new_opr)
                        recur(i+1, used_numbers, used_operations, val, new_opr, tmp_numbers, tmp_oper)
                        tmp_oper.pop()
                        used_operations[k] = False

            return
        recur(0, used_numbers, used_operations, 0, "+", [], [])
        return ans

if __name__ == '__main__':
    sol = Solution()
    numbers = [2, 4, 1024,0,2,2,32,16]
    operations = [">>", "&", "&", "-", "^","^"]
    ans = sol.calculate_1024(numbers, operations)
    print(ans)
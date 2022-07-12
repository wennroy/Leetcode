# 官方标答栈模拟

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        st = []
        for aster in asteroids:
            alive = True
            while alive and aster < 0 and st and st[-1] > 0:
                alive = st[-1] < -aster
                if st[-1] <= -aster:
                    st.pop()
            if alive:
                st.append(aster)
        return st


# 我的
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = [asteroids[0]]
        n = len(asteroids)
        i = 1
        while i < n:
            cur = asteroids[i]
            if stack and stack[-1] > 0 and cur < 0:
                delta = stack[-1] + cur
                if delta < 0:
                    stack.pop()
                    stack.append(cur)
                elif delta == 0:
                    stack.pop()
            else:
                stack.append(cur)
            i += 1
        i = 0
        # print(stack)
        while i < len(stack)-1:
            if i >=0 and stack[i] > 0 and stack[i+1] < 0:
                delta = stack[i] + stack[i+1]
                if delta <0:
                    stack = stack[:i] + stack[i+1:]
                    i -= 2
                elif delta == 0:
                    stack = stack[:i] + stack[i+2:]
                    i -= 2
                else:
                    stack = stack[:i+1] + stack[i+2:]
                    i -= 1
            i += 1
        return stack


# 两年前的
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        i = 0
        while i <= len(asteroids)- 2:
            # print(asteroids,i)
            iscollide = asteroids[i] * asteroids[i+1]
            if asteroids[i] < 0 and asteroids[i+1] > 0:
                i += 1
                continue
            if iscollide > 0:
                i += 1
                continue
            else:
                if abs(asteroids[i]) > abs(asteroids[i+1]):
                    asteroids.pop(i+1)
                elif abs(asteroids[i]) == abs(asteroids[i+1]):
                    asteroids.pop(i)
                    asteroids.pop(i)
                    if i == 0:
                        continue
                    i -= 1
                else:
                    asteroids.pop(i)
                    if i == 0:
                        continue
                    i -= 1
        return asteroids

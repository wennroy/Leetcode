from collections import deque


class MaxQueue:

    def __init__(self):
        self.q = deque()
        self.max_q = deque()

    def max_value(self) -> int:
        if self.max_q:
            return self.max_q[0]
        return -1

    def push_back(self, value: int) -> None:
        self.q.append(value)
        while self.max_q and self.max_q[-1] < value:
            self.max_q.pop()
        self.max_q.append(value)
        return None

    def pop_front(self) -> int:
        if not self.q:
            return -1

        pop_val = self.q.popleft()
        if pop_val == self.max_q[0]:
            self.max_q.popleft()
        return pop_val

# Your MaxQueue object will be instantiated and called as such:
# obj = MaxQueue()
# param_1 = obj.max_value()
# obj.push_back(value)
# param_3 = obj.pop_front()
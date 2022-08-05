from collections import deque

q = deque()
q.append(12)
q.append(15)

for i in range(len(q)):
    q.popleft()
    q.append(11)
    q.append(12)
    print(i)
print(q)
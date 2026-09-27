from collections import deque

q = deque()
q.append(1)
q.append(2)
front = q[0]
x = q.popleft()
q.appendleft(0)
y = q.pop()
print(x, y, len(q))

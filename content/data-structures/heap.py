import heapq

h = []
heapq.heappush(h, 5)
heapq.heappush(h, 1)
heapq.heappush(h, 3)
smallest = h[0]
x = heapq.heappop(h)

v = [4, 7, 2]
heapq.heapify(v)

big = []
for y in [5, 9, 2]:
    heapq.heappush(big, -y)
largest = -heapq.heappop(big)

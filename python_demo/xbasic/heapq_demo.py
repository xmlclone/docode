import heapq


h1 = [1, 3, 5, 0, 2, 9, -1]
heapq.heapify(h1)
heapq.heappush(h1, 1)
heapq.heappush(h1, 5)
heapq.heappush(h1, 3)

for i in range(len(h1)):
    a = heapq.heappop(h1)
    # 不用关注 h1 本身的顺序，heappop 会自动找到最小的值
    # 使用 h1[0] 访问最小的元素而不弹出
    print(f"{h1=}, {a=}")
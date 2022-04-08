import heapq
import sys


t = int(sys.stdin.readline())
for _ in range(t):
    k = int(sys.stdin.readline())
    minq = []
    maxq = []
    count = {}
    for _ in range(k):
        c, n = [x for x in sys.stdin.readline().split()]
        n = int(n)
        if c == 'I':
            if not n in count:
                count[n] = 0
            count[n] += 1
            heapq.heappush(minq, n)
            heapq.heappush(maxq, -n)
        else:
            if n == 1:
                while len(maxq) > 0 and count[-maxq[0]] == 0:
                    heapq.heappop(maxq)
                if len(maxq) == 0:
                    continue
                if count[-maxq[0]] > 0:
                    count[-maxq[0]] -= 1
                heapq.heappop(maxq)
            else:
                while len(minq) > 0 and count[minq[0]] == 0:
                    heapq.heappop(minq)
                if len(minq) == 0:
                    continue
                if count[minq[0]] > 0:
                    count[minq[0]] -= 1
                heapq.heappop(minq)

    while len(maxq) > 0 and count[-maxq[0]] == 0:
        heapq.heappop(maxq)
    while len(minq) > 0 and count[minq[0]] == 0:
        heapq.heappop(minq)

    if len(minq) == 0 or len(maxq) == 0:
        print('EMPTY')
    else:
        print(-maxq[0], minq[0])
    # print(maxq, minq)

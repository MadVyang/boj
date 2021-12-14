import sys
input = sys.stdin.readline

n = int(input())
all_nums = sorted(list(map(int, input().split())))

double_mixed = [(i,j) for i in range(n) for j in range(i+1, n)]
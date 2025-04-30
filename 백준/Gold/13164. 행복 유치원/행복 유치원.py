n, m = map(int, input().split())
heights = list(map(int, input().split()))

heights.sort()

diff = [heights[i+1] - heights[i] for i in range(n - 1)]

diff.sort(reverse=True)

print(sum(diff[m-1:]))
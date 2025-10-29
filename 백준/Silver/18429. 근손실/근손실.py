n,k = map(int,input().split())
n_list = list(map(int,input().split()))
visit = [False] * n
cnt = 0
ans = 0

def dfs(weight):
	global cnt, ans
	if weight < 500:
		return
	if cnt == n:
		ans += 1
		return
	
	for i in range(n):
		if visit[i] == False:
			visit[i] = True
			weight = weight - k + n_list[i]
			cnt += 1
			dfs(weight)
			visit[i] = False
			weight = weight + k - n_list[i]
			cnt -= 1

dfs(500)
print(ans)
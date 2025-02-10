import sys
input = sys.stdin.read

data = input().split()

N = int(data[0])
A = set(map(int, data[1:N+1]))

M = int(data[N+1])
queries = map(int, data[N+2:N+2+M])

sys.stdout.write('\n'.join(['1' if x in A else '0' for x in queries]) + '\n')
N, M = map(int, input().split())
lst = []
for i in range (1, N + 1):
  lst.append(i)
for j in range(1, M + 1):
  n, m = map(int, input().split()) #1 2 
  for k in range(n-1, (m+n)//2):
    lst[k], lst[m-1-k+(n-1)] = lst[m-1-k+(n-1)], lst[k]

print(*lst)
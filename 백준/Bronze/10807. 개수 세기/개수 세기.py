N = int(input())
n = list(map(int,input().split())) #[1,2,3,4,5...]
v = int(input())
V = 0
for i in range(N):
  if n[i] == v:
    V = V + 1
print(V)
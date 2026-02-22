N = int(input())
a = []
for i in range(100):
  a.append([0] * 100)
for i in range(N):
  coordinate1, coordinate2 = map(int, input().split())
  for j in range(10):
    for k in range(10):
      a[coordinate1 + j][coordinate2 + k] = 1 
ans = 0 
for i in range(100):
  for j in range(100):
    if a[i][j] == 1:
      ans = ans + 1
print(ans)
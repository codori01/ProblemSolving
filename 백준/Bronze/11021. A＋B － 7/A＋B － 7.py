T = int(input())
n = 0
for i in range(0, T, 1):
  A, B = map(int, input().split())
  n = n + 1
  print("Case #" + str(n) + ": " + str(A + B))
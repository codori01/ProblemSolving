N, n = input().split()
N = N[::-1]
n = n[::-1]
if int(N) > int(n):
  print(N)
if int(N) < int(n):
  print(n)
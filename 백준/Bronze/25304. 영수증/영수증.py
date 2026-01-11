X = int(input())
N = int(input())
s = 0

for i in range(1,N + 1,1):
  a, b = map(int, input(). split())
  s = s + a * b
  
if X == s:
  print("Yes")
else:
  print("No")
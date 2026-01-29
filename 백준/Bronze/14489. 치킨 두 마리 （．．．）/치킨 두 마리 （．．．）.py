A,B = map(int, input().split())
C = int(input())
if A + B >= 2 * C:
  print((A - C) + (B - C))
else:
  print(A + B)
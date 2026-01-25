N, M = map(int, input().split())
ball = [0] * N
for i in range (M):
  A, B, C = map(int,input().split())
  for j in range(A-1, B, 1):
    ball[j] = C
for i in range(N): 
  print(ball[i],end = " ")
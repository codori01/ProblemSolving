N, M = map(int,input().split())
ball = []
for i in range(1, N+1, 1):
  ball.append(i)
for i in range (M):
  A, B = map(int, input().split())
  tmp = ball[A-1]
  ball[A-1] = ball[B-1]
  ball[B-1] = tmp 
print(*ball)
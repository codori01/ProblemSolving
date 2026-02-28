N, M = map(int, input().split())
cards = list(map(int,input().split()))
max = 0
lst = []
for i in range(N):
  for j in range(i+1,N):
    for k in range(j+1,N):
      sum = cards[i] + cards[j] + cards[k]
      if max < sum <= M:
        max = sum
print(max)
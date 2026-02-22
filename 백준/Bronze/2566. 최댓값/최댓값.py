max = 0
a = []
maxi = 0
maxj = 0
for i in range(9):
  a.append(list(map(int, input().split())))
for i in range(9):
  for j in range(9):
    if a[i][j] > max:
      max = a[i][j]
      maxi = i
      maxj = j
print(max)
print(maxi + 1, maxj + 1)
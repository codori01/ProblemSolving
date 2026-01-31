a = [False] * 31
for i in range(28):
  n = int(input())
  a[n] = True

for i in range(1,31, 1):
  if a[i] == False:
    print(i)
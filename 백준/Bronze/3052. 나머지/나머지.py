a = [False] * 42
count = 0
for i in range(10):
  A = int(input())
  x = A % 42
  a[x] = True

for i in range(42):
  if a[i] == True:
    count = count + 1
print(count)
N = int(input())
x = 0
for i in range (N):
  D = int(input().split("D-")[1])
  if D <= 90:
    x = x + 1
print(x)
T = int(input())
for i in range(T):
  input()
  N = int(input())
  total = 0
  for j in range(N):
    candy = int(input())
    total = total + candy
  if total % N == 0:
    print("YES")
  else:
    print("NO")

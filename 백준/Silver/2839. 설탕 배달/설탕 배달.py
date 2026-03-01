N = int(input())
ans = -1
for i in range(N//5, -1, -1):
  remain = N - (5 * i)
  if remain % 3 == 0:
    ans = i + (remain // 3)
    break
print(ans)
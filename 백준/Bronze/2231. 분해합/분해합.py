N = int(input())
ans = 0 
for i in range(1,N+1): #i => 198 
  a = str(i)
  tmp = i 
  for j in a: 
    tmp += int(j)
  if tmp == N: 
    ans = i
    break 
print(ans)
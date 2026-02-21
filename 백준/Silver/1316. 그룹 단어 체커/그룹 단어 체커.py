N = int(input())
ans = N 
for i in range(N):
  count = [-1] * 26
  word = input()
  for j in range(len(word)):
    idx = ord(word[j]) - ord("a")
    if count[idx] == -1 : 
      count[idx] = j
    elif j - count[idx] > 1:
      ans -= 1
      break 
    count[idx] = j
print(ans)
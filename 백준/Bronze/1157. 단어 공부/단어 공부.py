word = input().upper()
count = [0] * 26
for i in range(len(word)):
  count[ord(word[i]) - ord("A")] += 1 
max = 0
ans = 0 
for j in range(26):
  if count[j] > max:
    max = count[j]
    ans = chr(j + ord("A"))
  elif max == count[j]:
    ans = "?"   
print(ans)
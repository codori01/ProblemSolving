lst = [-1] * 26 
S = input()
for i in range(len(S)):
  if lst[ord(S[i]) - ord("a")] == -1:
    lst[ord(S[i]) - ord("a")] = i
for i in range(26):
  print(lst[i], end = " ")
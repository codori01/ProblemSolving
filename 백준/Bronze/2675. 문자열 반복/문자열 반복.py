T = int(input())
for i in range(T):
  S,s = map(str, input().split())
  for j in range(len(s)):
    print(s[j] * int(S), end = "")
  print()
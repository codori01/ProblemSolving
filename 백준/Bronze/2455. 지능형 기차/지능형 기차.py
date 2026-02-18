people = 0
max = 0
for i in range(4):
  out, add = map(int, input().split())
  people = (people - out) + add
  if people > max:
    max = people
print(max)
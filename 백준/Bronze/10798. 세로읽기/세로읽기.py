a = [] 
for i in range(5): 
  a.append([""] * 15)
for i in range(5):
  tmp = input()
  for j in range(len(tmp)): 
    a[i][j] = tmp[j]
for i in range(15):
  for j in range(5):
    print(a[j][i], end = "")
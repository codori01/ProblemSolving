word = input() 
ans = 0 

for i in word: 
  if i == "A" or i == "B" or i == "C": 
    ans = ans + 3 
  elif i == "D" or i == "E" or i == "F":
    ans = ans + 4
  elif i == "G" or i == "H" or i == "I":
    ans = ans + 5
  elif i == "J" or i == "K" or i == "L":
    ans = ans + 6
  elif i == "M" or i == "N" or i == "O":
    ans = ans + 7
  elif i == "P" or i == "Q" or i == "R" or i == "S":
    ans = ans + 8
  elif i == "T" or i == "U" or i == "V":
    ans = ans + 9
  else:
    ans = ans + 10
print(ans)
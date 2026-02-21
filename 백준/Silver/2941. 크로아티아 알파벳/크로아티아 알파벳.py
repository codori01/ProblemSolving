letter = input()
count = 0
i = 0 
while i < len(letter): 
  if letter[i:i+2] == "c=" or letter[i:i+2] == "c-" or letter[i:i+2] == "d-" or letter[i:i+2] == "lj" or letter[i:i+2] == "nj" or letter[i:i+2] == "s=" or letter[i:i+2] == "z=":
    count += 1
    i += 1 
  elif letter[i:i+3] == "dz=":
    count += 1
    i += 2 
  else:
    count += 1
  i += 1 
print(count)
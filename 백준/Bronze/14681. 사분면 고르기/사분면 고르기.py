coordinate1 = int(input())
coordinate2 = int(input())
if coordinate1 > 0 and coordinate2 > 0:
  print("1")
elif coordinate1 < 0 and coordinate2 > 0:
  print("2")
elif coordinate1 < 0 and coordinate2 < 0:
  print("3")
else:
  print("4")
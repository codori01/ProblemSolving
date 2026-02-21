FinalScore = 0
FinalPoints = 0

for i in range(20):
  subject, point, grade = input().split()
  point = float(point)
  if grade == "P":
    continue
  elif grade == "A+":
    point2 = 4.5
  elif grade == "A0":
    point2 = 4.0
  elif grade == "B+":
    point2 = 3.5
  elif grade == "B0":
    point2 = 3.0
  elif grade == "C+":
    point2 = 2.5
  elif grade == "C0":
    point2 = 2.0
  elif grade == "D+":
    point2 = 1.5
  elif grade == "D0":
    point2 = 1.0
  elif grade == "F":
    point2 = 0.0
  FinalScore = FinalScore + (point * point2)
  FinalPoints = FinalPoints + point
GPA = FinalScore / FinalPoints
print(GPA)
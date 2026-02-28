a, b = map(int, input(). split())
row = ((b - 1) // 4) - ((a - 1) // 4)
column = ((b - 1) % 4) - ((a - 1) % 4) 
print(abs(row) + abs(column))
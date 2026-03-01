n = int(input())
def F(n):
  if n == 0 or n == 1:
    return n
  return F(n - 2) + F(n - 1)
print(F(n))
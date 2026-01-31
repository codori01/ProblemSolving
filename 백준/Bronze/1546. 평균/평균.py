N = int(input())
nums = list(map(int, input().split()))
sum = 0
M = -1
for i in range (N):
  if nums[i] > M:
    M = nums[i]

for i in range (N):
  nums[i] = (nums[i] / M) * 100 
  sum = sum + nums[i]

print(sum / N)
# Find duplicate elements in a list
# nums = [1,2,2,3,3,4,5]
# ans = [2,3]

def findDuplicates(nums):
  d = {}
  ans = []

#  for num in nums:
#    if num in d:
#      ans.append(num)
#    d[num] = num
#  return list(set(ans))

  for i in range(0,len(nums)):
    if nums[i] in d:
      ans.append(nums[i])
    d[nums[i]] = nums[i]
  return ans

# Example
print(findDuplicates([1,2,2,3,3,4,5]))

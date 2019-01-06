def twoSum(nums,sum):
  d = {}
  ans = []
  for i in range(0,len(nums)):
    sumMinusElement = sum - nums[i]
    if sumMinusElement in d:
      ans.append([nums[i],sumMinusElement])
    d[nums[i]] = nums[i]
  return ans

# Example
print(twoSum([2,3,1,6,7,5],7))

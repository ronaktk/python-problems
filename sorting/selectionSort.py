# Selection Sort
def selectionSort(nums):
    for i in range(0,len(nums)-1):
        minIndex=i
        for j in range(i+1,len(nums)):
            if nums[j]<nums[minIndex]:
                minIndex=j
        if minIndex!=i:
            nums[i],nums[minIndex]=nums[minIndex],nums[i]

nums=[2,10,8,34,24]
print("Before sorting: ")
print(nums)
selectionSort(nums)
print("After sorting: ")
print(nums)
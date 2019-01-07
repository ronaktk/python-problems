# Remove duplicates from a list

def remove_duplicates(nums):
    new_list = []
    for num in nums:
        if num not in new_list:
            new_list.append(num)
    return new_list

# Example
nums = [1,1,2,2,3,4,5]
print(remove_duplicates(nums))

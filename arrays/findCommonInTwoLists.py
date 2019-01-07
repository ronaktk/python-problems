# Find out common elements from two lists

def find_common(list1, list2):
    set1 = set(list1)
    set2 = set(list2)
    if len(set1.intersection(set2)) > 0:
        return(list(set1.intersection(set2)))
    else:
        print("No common elements")

# Example
list1 = [1,2,3,4,5]
list2 = [1,2,7,8,9]
print(find_common(list1, list2))

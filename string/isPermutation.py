# Check if two strings are permutation of each other

def isPermutation(str1,str2):
  str1 = str1.replace(" ","")
  str2 = str2.replace(" ","")
  if len(str1) != len(str2):
    return False
  else:
    for c in str1:
      if c in str2:
        str2 = str2.replace(c, "")
    return len(str2) == 0

# Example
print(isPermutation("moon","noom"))
print(isPermutation("sun","sunn"))


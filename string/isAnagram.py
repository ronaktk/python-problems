# Check if the two strings are anagram or not

def isAnagram(str1,str2):
  str1 = str1.replace(" ","").lower()
  str2 = str2.replace(" ","").lower()

  d = dict()

  if len(str1) != len(str2):
    return False

  for i in str1:
    if i in d:
      d[i]+=1
    else:
      d[i]=1

  for i in str2:
    if i in d:
      d[i]-=1
    else:
      d[i]=1
  
  for i in d:
    if d[i]!=0:
      return False
  return True

# Example
print(isAnagram('Fairy Tales','Rail Safety'))

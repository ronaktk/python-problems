# Check if the string has unique characters or not

def isUnique(str1):
  d = dict()
  str1=str1.replace(" ","").lower()
  for i in str1:
    if i in d:
      return False
    else:
      d[i]=1
  return True

print(isUnique('non unique'))
print(isUnique('hey'))

def isUnique2(str2):
  return len(set(str2)) == len(str2)

print(isUnique2('non unique'))
print(isUnique2('hey'))

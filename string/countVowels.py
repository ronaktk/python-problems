# Count vowels in a given string

def countVowels(str):
  vowels = ['a','e','i','o','u']
  count = 0
  str = str.lower()
  for letter in str:
    if letter in vowels:
      count+=1
  return count

# Example
print(countVowels("Hi How are you?"))

# Find the first non-repeating character in a string

def solution(string):
  d = {}
  order = []
  for letter in string:
    if letter in d:
      d[letter]+=1
    else:
      d[letter]=1
      order.append(letter)
  #print(order)
  for letter in order:
    if d[letter] == 1:
      return letter
  return None

# Example
print(solution('blue blue sky'))  

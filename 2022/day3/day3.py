input_file = open('./input.txt', 'r')
input_data = input_file.read().rstrip().split('\n')

def scoreOf(item):
  if item > "a":
    return ord(item) - 96
  else:
    return ord(item) - 64 + 26

# day3 part one

score = 0
for index in range(len(input_data)):
  if input_data[index] == "":
    break
  rucksack = input_data[index]
  left = rucksack[slice(0, len(rucksack)//2)]
  right = rucksack[slice(len(rucksack)//2, len(rucksack))]
  intersection = list(set(left).intersection(right))
  for item in intersection:
    score += score(item)
print(score)

# day3 part two

score = 0
for index in range(0, len(input_data), 3):
  if input_data[index] == "":
    break
  first = input_data[index]
  second = input_data[index+1]
  third = input_data[index+2]
  intersection = set(first).intersection(second).intersection(third)
  for item in intersection:
    score += scoreOf(item)
print(score)

input_file = open('./input.txt', 'r')
input_data = input_file.read().rstrip().split('\n')

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
    if item > "a":
      score += ord(item) - 96
    else:
      score += ord(item) - 64 + 26
print(score)

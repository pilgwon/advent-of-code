input_file = open('./input.txt', 'r')
input_data = input_file.read().rstrip().split('\n')[0]

# day6 part one

result = []
for idx, signal in enumerate(input_data):
  if signal in result:
    while signal in result:
      result.pop(0)
  result.append(signal)
  if len(result) == 4: break
print(idx + 1)

# day6 part two

result = []
for idx, signal in enumerate(input_data):
  if signal in result:
    while signal in result:
      result.pop(0)
  result.append(signal)
  if len(result) == 14: break
print(idx + 1)

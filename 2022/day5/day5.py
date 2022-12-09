import re

input_file = open('./input.txt', 'r')
input_data = input_file.read().rstrip().split('\n')

crates = {}
for index in range(len(input_data)):
  if input_data[index+1] == "":
    break
  input = input_data[index]
  chunks = [input[i:i+4] for i in range(0, len(input), 4)]
  for idx, chunk in enumerate(chunks):
    if '[' in chunk:
      key = '%d' % (idx + 1)
      if key not in crates:
        crates[key] = []
      crates[key].append(chunk[1])


# day5 part one

for idx in range(index+2, len(input_data)):
  input = input_data[idx]
  parsed = re.match("\W*move (\d+) from (\d+) to (\d+)", input)
  move_count = int(parsed.group(1))
  from_idx = parsed.group(2)
  to_idx = parsed.group(3)

  for move in range(move_count):
    from_crate = crates[from_idx]
    to_crate = crates[to_idx]
    temp = from_crate.pop(0)
    to_crate.insert(0, temp)
    crates[from_idx] = from_crate
    crates[to_idx] = to_crate

# day5 part two

for idx in range(index+2, len(input_data)):
  input = input_data[idx]
  parsed = re.match("\W*move (\d+) from (\d+) to (\d+)", input)
  move_count = int(parsed.group(1))
  from_idx = parsed.group(2)
  to_idx = parsed.group(3)

  from_crate = crates[from_idx]
  to_crate = crates[to_idx]
  temp = []
  for move in range(move_count):
    temp.append(from_crate.pop(0))
  for t in reversed(temp):
    to_crate.insert(0, t)
  crates[from_idx] = from_crate
  crates[to_idx] = to_crate


result = ''
for idx in range(len(crates)):
  key = '%d' % (idx + 1)
  result += crates[key][0]
print(result)

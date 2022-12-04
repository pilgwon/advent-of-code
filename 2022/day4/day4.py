input_file = open('./input.txt', 'r')
input_data = input_file.read().rstrip().split('\n')

# day4 part one

def check_fully_contains(lhs, rhs):
  (lhs_start, lhs_end) = [int(x) for x in lhs.split('-')]
  (rhs_start, rhs_end) = [int(x) for x in rhs.split('-')]
  return (
    (lhs_start <= rhs_start and rhs_end <= lhs_end) or
    (rhs_start <= lhs_start and lhs_end <= rhs_end)
  )

pairs = 0
for index in range(len(input_data)):
  if input_data[index] == "":
    break
  (left, right) = input_data[index].split(',')
  if check_fully_contains(left, right):
    pairs += 1
print(pairs)

# day4 part two

def check_overlaps(lhs, rhs):
  (lhs_start, lhs_end) = [int(x) for x in lhs.split('-')]
  (rhs_start, rhs_end) = [int(x) for x in rhs.split('-')]
  return (
    (lhs_start <= rhs_end and lhs_end >= rhs_end) or
    (rhs_start <= lhs_end and rhs_end >= lhs_end)
  )

pairs = 0
for index in range(len(input_data)):
  if input_data[index] == "":
    break
  (left, right) = input_data[index].split(',')
  if check_overlaps(left, right):
    pairs += 1
print(pairs)

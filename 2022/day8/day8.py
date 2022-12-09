input_file = open('./input.txt', 'r')
input_data = input_file.read().rstrip().split('\n')

map = []
visit = []

for row in input_data:
  map_row = []
  visit_row = []
  for tree in row:
    map_row.append(int(tree))
    visit_row.append(False)
  map.append(map_row)
  visit.append(visit_row)

# day8 part one

def horizontal_quadcopter():
  result = 0
  for i in range(len(map)):
    max = -1
    for j in range(len(map)):
      tree = map[i][j]
      if tree > max:
        if visit[i][j] == False:
          visit[i][j] = True
          result += 1
        max = tree
    max = -1
    for j in range(len(map)-1, -1, -1):
      tree = map[i][j]
      if tree > max:
        if visit[i][j] == False:
          visit[i][j] = True
          result += 1
        max = tree
  return result

def vertical_quadcopter():
  result = 0
  for i in range(len(map)):
    max = -1
    for j in range(len(map)):
      tree = map[j][i]
      if tree > max:
        if visit[j][i] == False:
          visit[j][i] = True
          result += 1
        max = tree
    max = -1
    for j in range(len(map)-1, -1, -1):
      tree = map[j][i]
      if tree > max:
        if visit[j][i] == False:
          visit[j][i] = True
          result += 1
        max = tree
  return result

result = 0
result += horizontal_quadcopter()
result += vertical_quadcopter()
print(result)


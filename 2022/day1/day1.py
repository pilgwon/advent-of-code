input_file = open('./input.txt', 'r')
input_data = input_file.read().rstrip().split('\n')

# day1 part one
delta_list = []
max_calories = 0
calories = 0
for index in range(len(input_data)):
  if input_data[index] == "":
    if calories > max_calories:
      max_calories = calories
    calories = 0
    continue
  calories += int(input_data[index])
print(max_calories)

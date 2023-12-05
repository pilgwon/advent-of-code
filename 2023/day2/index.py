input_file = open('./input.txt', 'r')
input_data = input_file.read().rstrip().split('\n')

# day2 part one
# sum = 0
# for index in range(len(input_data)):
#     game = input_data[index].split(": ")[1]
#     sets = game.split("; ")
#     set_count = 0
#     for set_index in range(len(sets)):
#         red = green = blue = 0
#         cubes = sets[set_index].split(", ")
#         for cube_index in range(len(cubes)):
#             cube = cubes[cube_index]
#             if "red" in cube:
#                 red += int(cube.split(" red")[0])
#             elif "green" in cube:
#                 green += int(cube.split(" green")[0])
#             elif "blue" in cube:
#                 blue += int(cube.split(" blue")[0])
#         if red <= 12 and green <= 13 and blue <= 14:
#             set_count += 1
#     if set_count == len(sets):
#         sum += (index + 1)
# print(sum)

# day2 part two
power_sum = 0
for index in range(len(input_data)):
    game = input_data[index].split(": ")[1]
    sets = game.split("; ")
    red = green = blue = 0
    for set_index in range(len(sets)):
        cubes = sets[set_index].split(", ")
        for cube_index in range(len(cubes)):
            cube = cubes[cube_index]
            if "red" in cube:
                count = int(cube.split(" red")[0])
                if count > red:
                    red = count
            elif "green" in cube:
                count = int(cube.split(" green")[0])
                if count > green:
                    green = count
            elif "blue" in cube:
                count = int(cube.split(" blue")[0])
                if count > blue:
                    blue = count
    print("Game %d: %d red, %d green, %d blue" % (index+1, red, green, blue))
    power_sum += red * green * blue
print(power_sum)

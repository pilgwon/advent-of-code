input_file = open('./input.txt', 'r')
input_data = input_file.read().rstrip().split('\n')

digits = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

# part1
# symbols = []
# numbers = []
# for x in range(len(input_data)):
#     num = 0
#     start = None
#     for y in range(len(input_data[x])):
#         c = input_data[x][y]
#         if c in digits:
#             if start is None:
#                 start = (x, y)
#             num = num * 10 + int(c)
#         else:
#             if start is not None:
#                 end = (x, y - 1)
#                 numbers.append((num, start, end))
#             num = 0
#             start = None
#             if c != ".":
#                 symbols.append((x, y))
#     if start is not None:
#         end = (x, y - 1)
#         numbers.append((num, start, end))

# sum = 0
# for (number, (sx, sy), (ex, ey)) in numbers:
#     for (x, y) in symbols:
#         if (sx - 1) <= x and x <= (ex + 1) and (sy - 1) <= y and y <= (ey + 1):
#             sum += number
#             break
# print('result: %d' % sum)

# part2
gears = []
numbers = []
for x in range(len(input_data)):
    num = 0
    start = None
    for y in range(len(input_data[x])):
        c = input_data[x][y]
        if c in digits:
            if start is None:
                start = (x, y)
            num = num * 10 + int(c)
        else:
            if start is not None:
                end = (x, y - 1)
                numbers.append((num, start, end))
            num = 0
            start = None
            if c == "*":
                gears.append((x, y))
    if start is not None:
        end = (x, y - 1)
        numbers.append((num, start, end))

sum = 0
for (x, y) in gears:
    candidates = []
    for (number, (sx, sy), (ex, ey)) in numbers:
        if (sx - 1) <= x and x <= (ex + 1) and (sy - 1) <= y and y <= (ey + 1):
            candidates.append(number)
    if len(candidates) == 2:
        sum += candidates[0] * candidates[1]
print('result: %d' % sum)
input_file = open('./input.txt', 'r')
input_data = input_file.read().rstrip().split('\n')

# part1
# sum = 0
# for index in range(len(input_data)):
#     input = input_data[index]
#     comp = input.split(": ")[1].split(" | ")
#     winning = list(map(lambda x: int(x), comp[0].split()))
#     given = list(map(lambda x: int(x), comp[1].split()))

#     score = 0
#     for w in winning:
#         if w in given:
#             if score == 0:
#                 score = 1
#             else:
#                 score *= 2
#     sum += score
# print('result: %d' % sum)

# part2
count = 0
copies = {}
for index in range(len(input_data)):
    copies[index] = 1
for index in range(len(input_data)):
    input = input_data[index]
    comp = input.split(": ")[1].split(" | ")
    winning = list(map(lambda x: int(x), comp[0].split()))
    given = list(map(lambda x: int(x), comp[1].split()))

    wins = 0
    for w in winning:
        if w in given:
            wins += 1
    for i in range(wins):
        next = index + i + 1
        if next < len(input_data):
            copies[index + i + 1] += 1 * copies[index]

cards = 0
for index in range(len(input_data)):
    cards += copies[index]
print('result: %d' % cards)
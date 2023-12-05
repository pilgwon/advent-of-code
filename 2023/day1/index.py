input_file = open('./input.txt', 'r')
input_data = input_file.read().rstrip().split('\n')

# day1 part one

# digits = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

# def get_calibration_value(input):
#     head = tail = None
#     for idx in range(len(input)):
#         if input[idx] in digits and head is None:
#             head = input[idx]
#         tail_idx = len(input)-idx-1
#         if input[tail_idx] in digits and tail is None:
#             tail = input[tail_idx]
#         if head is not None and tail is not None:
#             break
#     return int(head) * 10 + int(tail)

# sum = 0
# for idx in range(len(input_data)):
#     sum += get_calibration_value(input_data[idx])
# print(sum)


# day1 part two
sum = 0
string_digits = { "one": "1", "two": "2", "three": "3", "four": "4", "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9" }
single_digits = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
for idx in range(len(input_data)):
    input = input_data[idx]
    head = tail = None
    for idx in range(len(input)):
        if head is None:
            if input[idx] in single_digits:
                head = input[idx]
            else:
                for key, value in string_digits.items():
                    if key in input[:idx+1]:
                        head = value
        tail_idx = len(input)-idx-1
        if tail is None:
            if input[tail_idx] in single_digits:
                tail = input[tail_idx]
            else:
                for key, value in string_digits.items():
                    if key in input[tail_idx:]:
                        tail = value
        if head is not None and tail is not None:
            break
    sum += int(head) * 10 + int(tail)
print(sum)

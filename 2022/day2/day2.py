from enum import Enum

input_file = open('./input.txt', 'r')
input_data = input_file.read().rstrip().split('\n')

class Shape(Enum):
  ROCK = 1
  PAPER = 2
  SCISSORS = 3

def roundScore(opponent, me):
  if (
    (opponent == Shape.ROCK and me == Shape.PAPER) or
    (opponent == Shape.PAPER and me == Shape.SCISSORS) or
    (opponent == Shape.SCISSORS and me == Shape.ROCK)
    ):
    return 6
  elif opponent == me:
    return 3
  else:
    return 0

# day2 part one

def asShape(shape):
  if shape == "X" or shape == "A":
    return Shape.ROCK
  elif shape == "Y" or shape == "B":
    return Shape.PAPER
  else:
    return Shape.SCISSORS

score = 0
for index in range(len(input_data)):
  if input_data[index] == "":
    break
  (left, right) = input_data[index].split(' ')
  opponent = asShape(left)
  me = asShape(right)
  score += roundScore(opponent, me) + me.value
print(score)

# day2 part two

def asShape2(left, right):
  if left == "A":
    opponent = Shape.ROCK
  elif left == "B":
    opponent = Shape.PAPER
  else:
    opponent = Shape.SCISSORS

  if right == "X":
    if opponent == Shape.ROCK:
      me = Shape.SCISSORS
    elif opponent == Shape.PAPER:
      me = Shape.ROCK
    else:
      me = Shape.PAPER
  elif right == "Y":
    me = opponent
  else:
    if opponent == Shape.ROCK:
      me = Shape.PAPER
    elif opponent == Shape.PAPER:
      me = Shape.SCISSORS
    else:
      me = Shape.ROCK

  return (opponent, me)

score = 0
for index in range(len(input_data)):
  if input_data[index] == "":
    break
  (left, right) = input_data[index].split(' ')
  (opponent, me) = asShape2(left, right)
  score += roundScore(opponent, me) + me.value
print(score)

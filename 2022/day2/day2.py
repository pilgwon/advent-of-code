from enum import Enum

input_file = open('./input.txt', 'r')
input_data = input_file.read().rstrip().split('\n')

# day2 part one

class Shape(Enum):
  ROCK = 1
  PAPER = 2
  SCISSORS = 3

def asShape(shape):
  if shape == "X" or shape == "A":
    return Shape.ROCK
  elif shape == "Y" or shape == "B":
    return Shape.PAPER
  else:
    return Shape.SCISSORS

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

score = 0
for index in range(len(input_data)):
  if input_data[index] == "":
    break
  (left, right) = input_data[index].split(' ')
  opponent = asShape(left)
  me = asShape(right)
  score += roundScore(opponent, me) + me.value
print(score)

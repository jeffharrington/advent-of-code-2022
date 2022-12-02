#
# Day 2: Rock Paper Scissors
# https://adventofcode.com/2022/day/2
#
class Me:
    ROCK = "X"
    PAPER = "Y"
    SCISSORS = "Z"


class Elf:
    ROCK = "A"
    PAPER = "B"
    SCISSORS = "C"


class OutcomeScore:
    WIN = 6
    DRAW = 3
    LOSS = 0


class ShapeScore:
    ROCK = 1
    PAPER = 2
    SCISSORS = 3


OUTCOME_SCORE_MAP = {
    Elf.ROCK: {
        Me.ROCK: OutcomeScore.DRAW + ShapeScore.ROCK,
        Me.PAPER: OutcomeScore.WIN + ShapeScore.PAPER,
        Me.SCISSORS: OutcomeScore.LOSS + ShapeScore.SCISSORS,
    },
    Elf.PAPER: {
        Me.ROCK: OutcomeScore.LOSS + ShapeScore.ROCK,
        Me.PAPER: OutcomeScore.DRAW + ShapeScore.PAPER,
        Me.SCISSORS: OutcomeScore.WIN + ShapeScore.SCISSORS,
    },
    Elf.SCISSORS: {
        Me.ROCK: OutcomeScore.WIN + ShapeScore.ROCK,
        Me.PAPER: OutcomeScore.LOSS + ShapeScore.PAPER,
        Me.SCISSORS: OutcomeScore.DRAW + ShapeScore.SCISSORS,
    },
}


def calculate(lines: list[str]):
    score = 0
    for line in lines:
        elf, me = line.strip().split(" ")
        score += OUTCOME_SCORE_MAP[elf][me]
    return score


with open("input.txt") as f:
    lines = f.readlines()
print(calculate(lines))

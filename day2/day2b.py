#
# Day 2: Rock Paper Scissors
# https://adventofcode.com/2022/day/2
#
class Outcome:
    LOSS = "X"
    DRAW = "Y"
    WIN = "Z"


class OutcomeScore:
    WIN = 6
    DRAW = 3
    LOSS = 0


class Elf:
    ROCK = "A"
    PAPER = "B"
    SCISSORS = "C"


class ShapeScore:
    ROCK = 1
    PAPER = 2
    SCISSORS = 3


OUTCOME_SCORE_MAP = {
    Outcome.WIN: {
        Elf.ROCK: ShapeScore.PAPER + OutcomeScore.WIN,
        Elf.PAPER: ShapeScore.SCISSORS + OutcomeScore.WIN,
        Elf.SCISSORS: ShapeScore.ROCK + OutcomeScore.WIN,
    },
    Outcome.DRAW: {
        Elf.ROCK: ShapeScore.ROCK + OutcomeScore.DRAW,
        Elf.PAPER: ShapeScore.PAPER + OutcomeScore.DRAW,
        Elf.SCISSORS: ShapeScore.SCISSORS + OutcomeScore.DRAW,
    },
    Outcome.LOSS: {
        Elf.ROCK: ShapeScore.SCISSORS + OutcomeScore.LOSS,
        Elf.PAPER: ShapeScore.ROCK + OutcomeScore.LOSS,
        Elf.SCISSORS: ShapeScore.PAPER + OutcomeScore.LOSS,
    },
}


def calculate(lines: list[str]):
    score = 0
    for line in lines:
        elf, outcome = line.strip().split(" ")
        score += OUTCOME_SCORE_MAP[outcome][elf]
    return score


with open("input.txt") as f:
    lines = f.readlines()
print(calculate(lines))

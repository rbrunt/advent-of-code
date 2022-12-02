from typing import Literal

from utils import get_question_input

def translate_round(round_line:str):
    """A Y => Rock, Paper"""
    items = round_line.strip().split()
    
    opponent_move = items[0]
    if opponent_move == "A":
        opponent_move = "rock"
    if opponent_move == "B":
        opponent_move = "paper"
    if opponent_move == "C":
        opponent_move = "scissors"

    player_move = items[1]
    if player_move == "X":
        player_move = "rock"
    if player_move == "Y":
        player_move = "paper"
    if player_move == "Z":
        player_move = "scissors"
    
    return [opponent_move, player_move]


def get_score_for_round(opponent_move: Literal["rock", "paper", "scissors"], player_move: Literal["rock", "paper", "scissors"]):
    total_score = 0
    # player  move points:
    if player_move == "rock":
        total_score += 1
    elif player_move == "paper":
        total_score += 2
    elif player_move == "scissors":
        total_score += 3

    SCORE_LOSE = 0
    SCORE_DRAW = 3
    SCORE_WIN = 6

    if opponent_move == player_move:
        total_score += SCORE_DRAW
    if (opponent_move == "rock" and player_move == "paper") or (opponent_move == "paper" and player_move == "scissors") or (opponent_move == "scissors" and player_move == "rock"):
         total_score += SCORE_WIN
    if (opponent_move == "rock" and player_move == "scissors") or (opponent_move == "paper" and player_move == "rock") or (opponent_move == "scissors" and player_move == "paper"):
         total_score += SCORE_LOSE
    
    return total_score

    
if __name__ == "__main__":
    question_input = get_question_input("02.txt")
    
    translated_rounds = (translate_round(r) for r in question_input.splitlines())
    scored_rounds = (get_score_for_round(*r) for r in translated_rounds)

    total = sum(scored_rounds)
    print(total)
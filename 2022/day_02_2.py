from typing import Literal
from day_02_1 import get_score_for_round
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
    if player_move == "X": # lose
        if opponent_move == "rock":
            player_move = "scissors"
        elif opponent_move == "paper":
            player_move = "rock"
        elif opponent_move == "scissors":
            player_move = "paper"
    if player_move == "Y": # draw
        player_move = opponent_move
    if player_move == "Z": # win
        if opponent_move == "rock":
            player_move = "paper"
        elif opponent_move == "paper":
            player_move = "scissors"
        elif opponent_move == "scissors":
            player_move = "rock"
    
    return [opponent_move, player_move]

if __name__ == "__main__":
    question_input = get_question_input("02.txt")

    translated_rounds = (translate_round(r) for r in question_input.splitlines())
    scored_rounds = (get_score_for_round(*r) for r in translated_rounds)

    total = sum(scored_rounds)
    print(total)

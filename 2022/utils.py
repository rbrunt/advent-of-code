from pathlib import Path

def get_question_input(filename:str):
    path = Path("inputs") / filename
    return path.read_text()
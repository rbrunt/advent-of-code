from utils import get_question_input


def score_item(item):
    i = ord(item) - 96
    if i < 0:
        i += 58
    return i

def get_duplicated_item(backpack_contents):
    i = len(backpack_contents) // 2
    c1 = backpack_contents[:i]
    c2 = backpack_contents[i:]

    for item in c1:
        if item in c2:
            return item



if __name__ == "__main__":
    question_input = get_question_input("03.txt")

    duplicates = (get_duplicated_item(b) for b in question_input.splitlines())
    print(sum(score_item(i) for i in duplicates))
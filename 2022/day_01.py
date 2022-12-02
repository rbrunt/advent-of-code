from utils import get_question_input

calories = get_question_input("01.txt")

elves_with_food = []
current_elf = []
for line in calories.splitlines():
    stripped = line.strip()
    if stripped:
        current_elf.append(int(stripped))
    else:
        elves_with_food.append(current_elf)
        current_elf = []

elves_total_calories = sorted([sum(elf) for elf in elves_with_food])
print("part 1:", elves_total_calories[-1])
print("part 2:", sum(elves_total_calories[-3:]))


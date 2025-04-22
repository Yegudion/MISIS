import random


def rand_num(min_value=2, max_value=10):
    number1 = random.randint(min_value, max_value)

    return number1


def geometric_progression(start, length):
    progression = []
    current_value = start

    for i in range(length):
        progression.append(current_value)
        current_value *= start

    return progression


welcom = "Welcome to the Brain Games!\nMay I have your name? Sam\nHello, Sam!\nWhat number is missing in the progression?\n"


print(welcom)

for j in range(3):
    start_value = rand_num()
    length = rand_num(5, 10)
    miss = rand_num(0, length - 1)

    progression = geometric_progression(start_value, length)

    correct_answer = progression[miss]
    progression[miss] = ".."

    print("Question", progression)

    answer = int(input("Your answer:"))

    if correct_answer == answer:
        print("Correct!")
    else:
        print(f"{answer} is wrong answer ;(. Correct answer was {correct_answer}.")
        break



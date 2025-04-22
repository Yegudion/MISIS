import random


def rand_num(min_value=1, max_value=100):
    number1 = random.randint(min_value, max_value)
    number2 = random.randint(min_value, max_value)
    number3= random.randint(min_value, max_value)

    return number1, number2, number3


welcom ="Welcome to the Brain Games!\nMay I have your name? Sam\nHello, Sam!\nFind the smallest common multiple of given numbers."


for j in range(3):
    a, b, c = rand_num()

    print(welcom, "Question", a, b, c)

    answer = int(input("Your answer:"))

    flag = 1

    i = max(a, b, c)

    while flag:
        i += 1
        if (i % a == 0) and (i % b == 0) and (i % c == 0):
            flag = 0

    if i == answer:
        print("Correct!")
    else:
        print(f"{answer} is wrong answer ;(. Correct answer was {i}.")
        break

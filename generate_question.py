"""Question generation for the math quiz assessment."""

import random


MIN_NUM = 1
ADD_SUB_RANGE = 10
MUL_DIV_RANGE = 5


def generate_question(operation, difficulty):
    """Create a question string and the correct answer."""

    if operation in ("*", "/"):
        max_range = MIN_NUM + difficulty * MUL_DIV_RANGE
    else:
        max_range = MIN_NUM + difficulty * ADD_SUB_RANGE

    num1 = random.randint(MIN_NUM, max_range)
    num2 = random.randint(MIN_NUM, max_range)

    if operation == "+":
        correct_answer = num1 + num2
        question = f"{num1} + {num2}"

    elif operation == "-":
        if num2 > num1:
            num1, num2 = num2, num1
        correct_answer = num1 - num2
        question = f"{num1} - {num2}"

    elif operation == "*":
        correct_answer = num1 * num2
        question = f"{num1} * {num2}"

    else:
        correct_answer = random.randint(MIN_NUM, max_range)
        num2 = random.randint(MIN_NUM, max_range)
        num1 = correct_answer * num2
        question = f"{num1} / {num2}"

    return question, correct_answer

operation = input("Enter an operation (+, -, *, /): ").strip().lower()
difficulty = int(input("Enter a difficulty level: "))
question, answer = generate_question(operation, difficulty)
print(f"Generated question: {question}")
print(f"Correct answer: {answer}")

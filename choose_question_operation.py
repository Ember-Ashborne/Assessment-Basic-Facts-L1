"""Operation selection logic for mixed quiz mode."""

import random


def choose_question_operation(selected_operation, difficulty):
    """Choose which operation to use for the current question."""

    if selected_operation != "mix":
        return selected_operation

    if difficulty >= 3:
        return random.choice(["+", "-", "*", "/"])
    elif difficulty >= 2:
        return random.choice(["+", "-", "*"])
    else:
        return random.choice(["+", "-"])

operation = input("Enter an operation (+, -, *, /, or mix): ").strip().lower()
difficulty = int(input("Enter a difficulty level: "))
chosen_operation = choose_question_operation(operation, difficulty)
print(f"Operation used for this question: {chosen_operation}")

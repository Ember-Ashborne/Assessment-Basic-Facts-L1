"""Main quiz loop for the math quiz assessment."""

import random


DIFFICULTY_STEP = 3
ADD_SUB_RANGE = 10
MUL_DIV_RANGE = 5


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


def generate_question(operation, difficulty):
    """Create a question string and the correct answer."""

    min_num = 1

    if operation in ("*", "/"):
        max_range = min_num + difficulty * MUL_DIV_RANGE
    else:
        max_range = min_num + difficulty * ADD_SUB_RANGE

    num1 = random.randint(min_num, max_range)
    num2 = random.randint(min_num, max_range)

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
        correct_answer = random.randint(min_num, max_range)
        num2 = random.randint(min_num, max_range)
        num1 = correct_answer * num2
        question = f"{num1} / {num2}"

    return question, correct_answer


def result_feedback(percentage):
    """Return end-of-game feedback based on the score percentage."""

    if percentage == 100:
        return "Perfect score. Calm down genius."
    elif percentage >= 85:
        return "Awesome work. You're really strong at this."
    elif percentage >= 70:
        return "Nice, you're solid at this."
    elif percentage >= 50:
        return "Not bad. You're getting there."
    else:
        return "We might need a rematch..."


def make_statement(statement, decoration):
    """Print a decorated heading."""

    ends = decoration * 3
    print(f"\n{ends} {statement} {ends}")


def run_quiz(num_questions, difficulty, operation):
    """Run the quiz loop and display the final results."""

    make_statement("Quiz Setup", "=")
    print(f"Questions: {num_questions}")
    print(f"Starting difficulty: {difficulty}")
    print(f"Operation mode: {operation}")

    score = 0
    wrong_questions = []
    quiz_history = []

    for i in range(num_questions):
        input(f"\nPress Enter to start question {i + 1}...")
        make_statement(f"Question {i + 1}/{num_questions}", "-")

        current_difficulty = difficulty + (i + 1) // DIFFICULTY_STEP
        print(f"Current difficulty: {current_difficulty}")
        current_operation = choose_question_operation(operation, current_difficulty)
        question, correct_answer = generate_question(current_operation, current_difficulty)

        try:
            user_answer = int(input(f"{question} = "))
        except ValueError:
            print("Invalid input. Question counted as wrong.")
            wrong_questions.append(
                f"{question} | Your answer: invalid | Correct: {correct_answer}"
            )
            quiz_history.append(
                f"Question {i + 1}: {question} | Your answer: invalid | Correct: {correct_answer}"
            )
            print(f"Score so far: {score}/{i + 1}")
            continue

        if user_answer == correct_answer:
            print("Correct!")
            score += 1
            quiz_history.append(
                f"Question {i + 1}: {question} | Your answer: {user_answer} | Correct"
            )
        else:
            print(f"Wrong! Answer: {correct_answer}")
            wrong_questions.append(
                f"{question} | Your answer: {user_answer} | Correct: {correct_answer}"
            )
            quiz_history.append(
                f"Question {i + 1}: {question} | Your answer: {user_answer} | Correct: {correct_answer}"
            )

        print(f"Score so far: {score}/{i + 1}")

    make_statement("Quiz Finished", "=")
    print(f"Score: {score}/{num_questions}")

    percentage = (score / num_questions) * 100
    print(f"Percentage: {percentage:.1f}%")
    print(result_feedback(percentage))

    if wrong_questions:
        print("\nReview your mistakes:")
        for item in wrong_questions:
            print(item)
    else:
        print("No mistakes. Insane.")

    make_statement("Quiz History", "=")
    for item in quiz_history:
        print(item)

print("=== Standalone Quiz Runner ===")
run_quiz(5, 1, "mix")

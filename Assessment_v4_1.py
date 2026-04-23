import random

def string_check(question, valid_options, error):
    """Ask for a text response and ensure it matches one of the valid options."""

    while True:
        response = input(question).strip().lower()

        if response in valid_options:
            return response

        print(error)


def yes_no(question):
    """Ask a yes/no question and return 'yes' or 'no'."""

    response = string_check(question, ["yes", "no", "y", "n"], "Please enter yes / no")

    if response == "y":
        return "yes"
    if response == "n":
        return "no"
    return response


def int_check(question, low, high=None):
    """Prompt user for an integer >= low and <= high (if provided)."""

    if high is None:
        error = f"Please enter an integer larger than or equal to {low}"
    else:
        error = f"Please enter an integer from {low} to {high}"

    while True:
        try:
            response = int(input(question))

            if response < low:
                print(error)
            elif high is not None and response > high:
                print(error)
            else:
                return response

        except ValueError:
            print(error)


def instructions():
    """Print the quiz instructions."""

    print("*** Instructions ***")
    print("1. Choose how many questions you want to answer.")
    print("2. Pick a starting difficulty from 1 to 3.")
    print("3. Choose one operation or select mix mode.")
    print("4. Difficulty increases as the quiz goes on.")
    print("5. As difficulty increases, the number ranges get larger and more operations are included in mix mode.")
    print("6. Even if the difficulty increases, you can still get easy questions. Just the chance of harder questions goes up.")
    print("7. Answer each question with an integer.")
    print("8. Try to get as many correct as you can. Don't worry about getting them all right, just do your best and have fun!")
    print("9. Your score, feedback, and question history will be shown at the end.")


def make_statement(statement, decoration):
    """Print a decorated heading."""

    ends = decoration * 3
    print(f"\n{ends} {statement} {ends}")


def choose_question_operation(selected_operation, difficulty):
    """Return the operation to use for the current question."""

    # If not in mix mode, keep the same operation throughout.
    if selected_operation != "mix":
        return selected_operation

    # In mix mode, unlock more operations as difficulty increases.
    if difficulty >= 3:
        return random.choice(["+", "-", "*", "/"])
    elif difficulty >= 2:
        return random.choice(["+", "-", "*"])
    else:
        return random.choice(["+", "-"])


def generate_question(operation, difficulty):
    """Generate a math question and return it with the correct answer."""

    # Scale number range based on operation type and difficulty.
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
        # Ensure subtraction does not produce negative results.
        if num2 > num1:
            num1, num2 = num2, num1
        correct_answer = num1 - num2
        question = f"{num1} - {num2}"

    elif operation == "*":
        correct_answer = num1 * num2
        question = f"{num1} * {num2}"

    else:
        # Construct division so the result is always a whole number.
        correct_answer = random.randint(MIN_NUM, max_range)
        num2 = random.randint(MIN_NUM, max_range)
        num1 = correct_answer * num2
        question = f"{num1} / {num2}"

    return question, correct_answer


def result_feedback(percentage):
    """Return feedback message based on score percentage."""

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


def run_quiz(num_questions, difficulty, operation):
    """Run the quiz loop and display results."""

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

        # Increase difficulty every DIFFICULTY_STEP questions.
        current_difficulty = difficulty + (i + 1) // DIFFICULTY_STEP
        if i > 0 and current_difficulty > difficulty + i // DIFFICULTY_STEP:
            print(f"Difficulty increased to {current_difficulty}!")

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


# Configuration values for quiz setup and difficulty scaling.
MIN_NUM = 1
DIFFICULTY_STEP = 5
ADD_SUB_RANGE = 10
MUL_DIV_RANGE = 5
VALID_OPERATIONS = ["+", "-", "*", "/", "mix"]

make_statement("Welcome to the Math Quiz", "=")

play_again = "yes"

while play_again == "yes":
    if yes_no("Do you want to see the instructions? ") == "yes":
        instructions()

    print()

    num_questions = int_check("How many questions do you want? ", 1)
    difficulty = int_check(
        "Choose starting difficulty (1 = easy, 2 = medium, 3 = hard): ",
        1,
        3,
    )

    if num_questions < 5 and difficulty <= 2:
        print("This quiz might be too easy or too short.")
        if yes_no("Do you want to continue anyway? ") == "no":
            print("Quiz setup cancelled.")
            play_again = yes_no("Do you want to set up another quiz? ")
            continue

    operation = string_check(
        "Choose operation (+, -, *, / or mix): ",
        VALID_OPERATIONS,
        "Invalid choice. Try again.",
    )
    run_quiz(num_questions, difficulty, operation)

    play_again = yes_no("\nDo you want to play again? ")

make_statement("Thanks for playing", "=")

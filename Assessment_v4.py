import random

def string_check(question, valid_options, error):
    """Ask for a text response and check it is valid."""

    while True:
        response = input(question).strip().lower()

        if response in valid_options:
            return response

        print(error)


def yes_no(question):
    """Ask a yes/no question and return only 'yes' or 'no'."""

    response = string_check(question, ["yes", "no", "y", "n"], "Please enter yes / no")

    if response == "y":
        return "yes"
    if response == "n":
        return "no"
    return response


def int_check(question, low, high=None):
    """Ask for an integer within the allowed range."""

    # Show the right error message for either a minimum-only or min/max range.
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


def get_operation(question, valid_operations):
    """Ask for a quiz operation and return a valid choice."""

    return string_check(question, valid_operations, "Invalid choice. Try again.")


def choose_question_operation(selected_operation, difficulty):
    """Choose which operation to use for the current question."""

    # Single-operation quizzes keep the same operation all the way through.
    if selected_operation != "mix":
        return selected_operation

    # Mix mode unlocks more operation types as the difficulty increases.
    if difficulty >= 3:
        return random.choice(["+", "-", "*", "/"])
    elif difficulty >= 2:
        return random.choice(["+", "-", "*"])
    else:
        return random.choice(["+", "-"])


def generate_question(operation, difficulty):
    """Create a question string and the correct answer."""

    # Addition and subtraction scale faster than multiplication and division.
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
        # Keep subtraction answers non-negative.
        if num2 > num1:
            num1, num2 = num2, num1
        correct_answer = num1 - num2
        question = f"{num1} - {num2}"

    elif operation == "*":
        correct_answer = num1 * num2
        question = f"{num1} * {num2}"

    else:
        # Build division questions backwards so answers stay whole numbers.
        correct_answer = random.randint(MIN_NUM, max_range)
        num2 = random.randint(MIN_NUM, max_range)
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


def run_quiz(num_questions, difficulty, operation):
    """Run the quiz loop and display the final results."""

    # Show the chosen settings before the first question starts.
    make_statement("Quiz Setup", "=")
    print(f"Questions: {num_questions}")
    print(f"Starting difficulty: {difficulty}")
    print(f"Operation mode: {operation}")

    # Track score, mistakes, and the full question history for the summary.
    score = 0
    wrong_questions = []
    quiz_history = []

    for i in range(num_questions):
        input(f"\nPress Enter to start question {i + 1}...")
        make_statement(f"Question {i + 1}/{num_questions}", "-")

        # Difficulty increases every few questions (determined by difficulty step variable).
        current_difficulty = difficulty + (i + 1) // DIFFICULTY_STEP
        if i > 0 and current_difficulty > difficulty + i // DIFFICULTY_STEP:
            print(f"Difficulty increased to {current_difficulty}!")
        print(f"Current difficulty: {current_difficulty}")
        current_operation = choose_question_operation(operation, current_difficulty)
        question, correct_answer = generate_question(current_operation, current_difficulty)

        try:
            user_answer = int(input(f"{question} = "))
        except ValueError:
            # Invalid answers still get recorded so the summary stays complete.
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

    # End-of-quiz summary shows the final score, mistakes, and full history.
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

# Main program loop for setting up and replaying quizzes.

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

    # Double-check very short or easy quizzes before starting.
    if num_questions < 5 and difficulty <= 2:
        print("This quiz might be too easy or too short.")
        if yes_no("Do you want to continue anyway? ") == "no":
            print("Quiz setup cancelled.")
            play_again = yes_no("Do you want to set up another quiz? ")
            continue

    operation = get_operation("Choose operation (+, -, *, / or mix): ", VALID_OPERATIONS)
    run_quiz(num_questions, difficulty, operation)

    play_again = yes_no("\nDo you want to play again? ")

make_statement("Thanks for playing", "=")

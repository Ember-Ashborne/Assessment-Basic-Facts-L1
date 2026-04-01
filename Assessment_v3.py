import random


# Configuration values used to control quiz scaling and valid setup choices.
# Smallest number that can appear in a generated question.
MIN_NUM = 1
# Increase the quiz difficulty after this many questions.
DIFFICULTY_STEP = 5
# Number range growth for addition and subtraction questions.
ADD_SUB_RANGE = 10
# Number range growth for multiplication and division questions.
MUL_DIV_RANGE = 5
# Allowed operation choices the user can type in.
VALID_OPERATIONS = ["+", "-", "*", "/", "mix"]


def yes_no(question):
    """Ask a yes/no question and return only 'yes' or 'no'."""

    while True:
        # Remove extra spaces and convert the answer to lowercase
        # so inputs like " Yes " and "Y" still work.
        response = input(question).strip().lower()

        # Accept full-word or single-letter yes answers.
        if response in ("yes", "y"):
            return "yes"
        # Accept full-word or single-letter no answers.
        elif response in ("no", "n"):
            return "no"
        else:
            # Keep asking until the user gives a valid yes/no response.
            print("Please enter yes / no")


def int_check(question, low, high=None):
    """Ask for an integer within the allowed range."""

    # Create the correct error message depending on whether
    # there is only a minimum value or both a minimum and maximum.
    if high is None:
        error = f"Please enter an integer larger than or equal to {low}"
    else:
        error = f"Please enter an integer from {low} to {high}"

    while True:
        try:
            # Try to convert the user's input into an integer.
            response = int(input(question))

            # Reject numbers that are below the allowed minimum.
            if response < low:
                print(error)
            # Reject numbers that are above the allowed maximum
            # when a maximum has been provided.
            elif high is not None and response > high:
                print(error)
            else:
                # Return the number once it passes all checks.
                return response

        except ValueError:
            # This runs if the user types something that is not an integer.
            print(error)


def instructions():
    """Print the quiz instructions."""

    # Display the rules and how the quiz works before the user starts.
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

    # Repeat the decoration symbol to make a simple banner.
    ends = decoration * 3
    print(f"\n{ends} {statement} {ends}")


def get_operation(question, valid_operations):
    """Ask for a quiz operation and return a valid choice."""

    while True:
        # Clean up the user's input so capital letters and spaces do not matter.
        response = input(question).strip().lower()

        # Only accept operations that are in the allowed list.
        if response in valid_operations:
            return response
        else:
            # If the answer is not valid, ask again.
            print("Invalid choice. Try again.")


def choose_question_operation(selected_operation, difficulty):
    """Choose which operation to use for the current question."""

    # If the user picked one operation, keep using it for every question.
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

    # Addition and subtraction use a wider number range than multiplication/division.
    if operation in ("*", "/"):
        max_range = MIN_NUM + difficulty * MUL_DIV_RANGE
    else:
        max_range = MIN_NUM + difficulty * ADD_SUB_RANGE

    if operation == "+":
        # Pick two random numbers and add them together.
        num1 = random.randint(MIN_NUM, max_range)
        num2 = random.randint(MIN_NUM, max_range)
        correct_answer = num1 + num2
        question = f"{num1} + {num2}"

    elif operation == "-":
        # Pick two random numbers for a subtraction question.
        num1 = random.randint(MIN_NUM, max_range)
        num2 = random.randint(MIN_NUM, max_range)
        # Swap numbers so subtraction questions stay non-negative.
        if num2 > num1:
            num1, num2 = num2, num1
        correct_answer = num1 - num2
        question = f"{num1} - {num2}"

    elif operation == "*":
        # Pick two random numbers and multiply them.
        num1 = random.randint(MIN_NUM, max_range)
        num2 = random.randint(MIN_NUM, max_range)
        correct_answer = num1 * num2
        question = f"{num1} * {num2}"

    else:
        # Build division questions backwards so the answer is always a whole number.
        correct_answer = random.randint(MIN_NUM, max_range)
        num2 = random.randint(MIN_NUM, max_range)
        num1 = correct_answer * num2
        question = f"{num1} / {num2}"

    # Send back both the question text and the answer for checking later.
    return question, correct_answer


def result_feedback(percentage):
    """Return end-of-game feedback based on the score percentage."""

    # Choose a feedback message based on the player's final percentage.
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

    # Show the player's chosen settings before the quiz starts.
    make_statement("Quiz Setup", "=")
    print(f"Questions: {num_questions}")
    print(f"Starting difficulty: {difficulty}")
    print(f"Operation mode: {operation}")

    # Track how many answers are correct.
    score = 0
    # Store incorrect questions for the review section at the end.
    wrong_questions = []
    # Store every question and answer for the full quiz history.
    quiz_history = []

    # Repeat once for each question in the quiz.
    for i in range(num_questions):
        # Pause until the user is ready to see the next question.
        input(f"\nPress Enter to start question {i + 1}...")
        make_statement(f"Question {i + 1}/{num_questions}", "-")

        # Difficulty increases every few questions instead of all at once.
        current_difficulty = difficulty + (i + 1) // DIFFICULTY_STEP
        # Let the user know when a new difficulty level has just started.
        if i > 0 and current_difficulty > difficulty + i // DIFFICULTY_STEP:
            print(f"Difficulty increased to {current_difficulty}!")
        print(f"Current difficulty: {current_difficulty}")
        # Decide which operation this question will use.
        current_operation = choose_question_operation(operation, current_difficulty)
        # Generate the question text and the correct answer.
        question, correct_answer = generate_question(current_operation, current_difficulty)

        try:
            # Ask the question and convert the answer into an integer.
            user_answer = int(input(f"{question} = "))
        except ValueError:
            # Non-integer answers are treated as incorrect and still recorded in the history.
            print("Invalid input. Question counted as wrong.")
            wrong_questions.append(
                f"{question} | Your answer: invalid | Correct: {correct_answer}"
            )
            quiz_history.append(
                f"Question {i + 1}: {question} | Your answer: invalid | Correct: {correct_answer}"
            )
            print(f"Score so far: {score}/{i + 1}")
            continue

        # Check whether the user's answer matches the correct answer.
        if user_answer == correct_answer:
            print("Correct!")
            # Increase the score for a correct answer.
            score += 1
            quiz_history.append(
                f"Question {i + 1}: {question} | Your answer: {user_answer} | Correct"
            )
        else:
            # Save wrong answers so they can be reviewed later.
            print(f"Wrong! Answer: {correct_answer}")
            wrong_questions.append(
                f"{question} | Your answer: {user_answer} | Correct: {correct_answer}"
            )
            quiz_history.append(
                f"Question {i + 1}: {question} | Your answer: {user_answer} | Correct: {correct_answer}"
            )

        # Show progress after each question.
        print(f"Score so far: {score}/{i + 1}")

    # End-of-quiz summary includes both overall results and a full question log.
    make_statement("Quiz Finished", "=")
    print(f"Score: {score}/{num_questions}")

    # Convert the raw score into a percentage.
    percentage = (score / num_questions) * 100
    print(f"Percentage: {percentage:.1f}%")
    # Print a matching feedback message for the final score.
    print(result_feedback(percentage))

    # Show only the mistakes if there were any.
    if wrong_questions:
        print("\nReview your mistakes:")
        for item in wrong_questions:
            print(item)
    else:
        # If there were no mistakes, celebrate it.
        print("No mistakes. Insane.")

    # Print the full record of every question from the quiz.
    make_statement("Quiz History", "=")
    for item in quiz_history:
        print(item)

# Main program loop: set up a quiz, run it, then offer to play again.
make_statement("Welcome to the Math Quiz", "=")

# Start by assuming the player wants to play once.
play_again = "yes"

# Keep looping until the player says no.
while play_again == "yes":
    # Offer to show the instructions before setting up the quiz.
    if yes_no("Do you want to see the instructions? ") == "yes":
        instructions()

    # Print a blank line to keep the setup section tidy.
    print()

    # Ask how many questions the player wants.
    num_questions = int_check("How many questions do you want? ", 1)
    # Ask for the starting difficulty and keep it between 1 and 3.
    difficulty = int_check(
        "Choose starting difficulty (1 = easy, 2 = medium, 3 = hard): ",
        1,
        3,
    )

    # Warn the user if they have chosen a very short or very easy quiz.
    if num_questions < 5 and difficulty <= 2:
        print("This quiz might be too easy or too short.")
        if yes_no("Do you want to continue anyway? ") == "no":
            print("Quiz setup cancelled.")
            # Let the player decide whether to start over with new settings.
            play_again = yes_no("Do you want to set up another quiz? ")
            continue

    # Ask which operation type the quiz should use.
    operation = get_operation("Choose operation (+, -, *, / or mix): ", VALID_OPERATIONS)
    # Start the quiz using the selected settings.
    run_quiz(num_questions, difficulty, operation)

    # Ask whether the player wants another round.
    play_again = yes_no("\nDo you want to play again? ")

# Final message shown after the player leaves the game loop.
make_statement("Thanks for playing", "=")

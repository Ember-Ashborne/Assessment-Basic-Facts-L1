import random

# --- constants ---
MIN_NUM = 1
MAX_NUM = 10

print("=== Welcome to the Math Quiz ===")

# --- helper function ---
def get_int_input(prompt, min_value=None):
    while True:
        try:
            value = int(input(prompt))
            if min_value is not None and value < min_value:
                print(f"Enter a number >= {min_value}.")
            else:
                return value
        except:
            print("That is not a valid number.")

# --- get number of questions ---
num_questions = get_int_input("How many questions do you want? ", 1)

# --- choose starting difficulty ---
difficulty = get_int_input("Choose starting difficulty (1 = easy, 2 = medium, 3 = hard): ", 1)

# --- warn user about easy setup ---
if num_questions < 5 and difficulty <= 2:
    print("This quiz might be too easy or too short.")
    choice = input("Do you want to continue anyway? (yes/no): ").lower()
    if choice != "yes":
        print("Restart the program and choose better settings.")
        exit()

# --- choose operation ---
valid_operations = ["+", "-", "*", "/", "mix"]

while True:
    operation = input("Choose operation (+, -, *, / or mix): ").lower()
    if operation in valid_operations:
        break
    else:
        print("Invalid choice. Try again.")

# --- tracking variables ---
score = 0
wrong_questions = []

# --- main quiz loop ---
for i in range(num_questions):
    print(f"\nQuestion {i+1}/{num_questions}")

    # increase difficulty every 3 questions
    if (i + 1) % 3 == 0:
        difficulty += 1

    # --- choose operation (mix mode logic) ---
    if operation == "mix":
        if difficulty >= 3:
            op = random.choice(["+", "-", "*", "/"])
        elif difficulty >= 2:
            op = random.choice(["+", "-", "*"])
        else:
            op = random.choice(["+", "-"])
    else:
        op = operation

    # --- determine number ranges ---
    if op in ["*", "/"]:
        # smaller ranges for multiplication/division at low difficulties
        max_range = MIN_NUM + difficulty * 5
    else:
        # + and - grow faster
        max_range = MIN_NUM + difficulty * 10

    num1 = random.randint(MIN_NUM, max_range)
    num2 = random.randint(MIN_NUM, max_range)

    # --- generate question ---
    if op == "+":
        correct_answer = num1 + num2
        question = f"{num1} + {num2}"

    elif op == "-":
        if num2 > num1:
            num1, num2 = num2, num1
        correct_answer = num1 - num2
        question = f"{num1} - {num2}"

    elif op == "*":
        correct_answer = num1 * num2
        question = f"{num1} * {num2}"

    elif op == "/":
        correct_answer = random.randint(MIN_NUM, max_range)
        num2 = random.randint(MIN_NUM, max_range)
        num1 = correct_answer * num2
        question = f"{num1} / {num2}"

    # --- user input ---
    try:
        user_answer = int(input(f"{question} = "))
    except:
        print("Invalid input. Question counted as wrong.")
        wrong_questions.append(f"{question} | Your answer: invalid | Correct: {correct_answer}")
        continue

    # --- check answer ---
    if user_answer == correct_answer:
        print("Correct! 🔥")
        score += 1
    else:
        print(f"Wrong! Answer: {correct_answer}")
        wrong_questions.append(f"{question} | Your answer: {user_answer} | Correct: {correct_answer}")

# --- results ---
print("\n=== Quiz Finished ===")
print(f"Score: {score}/{num_questions}")

percentage = (score / num_questions) * 100
print(f"Percentage: {percentage:.1f}%")

# feedback system
if percentage == 100:
    print("Perfect score. calm down genius 😭")
elif percentage >= 70:
    print("Nice, you're solid at this.")
else:
    print("We might need a rematch...")

# --- review mistakes ---
if wrong_questions:
    print("\nReview your mistakes:")
    for q in wrong_questions:
        print(q)
else:
    print("No mistakes. insane.")

# --- replay prompt ---
while True:
    again = input("\nPlay again? (yes/no): ").lower()
    if again == "yes":
        print("Restart the program to play again.")
        break
    elif again == "no":
        print("Thanks for playing 👋")
        break
    else:
        print("Type yes or no.")
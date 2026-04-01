"""Operation choice helper for the math quiz assessment."""


def get_operation(question, valid_operations):
    """Ask for a quiz operation and return a valid choice."""

    while True:
        response = input(question).strip().lower()

        if response in valid_operations:
            return response
        else:
            print("Invalid choice. Try again.")

operations = ["+", "-", "*", "/", "mix"]
choice = get_operation("Choose operation (+, -, *, / or mix): ", operations)
print(f"You chose: {choice}")

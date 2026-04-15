"""Operation choice helper for the math quiz assessment."""


def string_check(question, valid_options, error):
    """Ask for a text response and check it is valid."""

    while True:
        response = input(question).strip().lower()

        if response in valid_options:
            return response

        print(error)


def get_operation(question, valid_operations):
    """Ask for a quiz operation and return a valid choice."""

    return string_check(question, valid_operations, "Invalid choice. Try again.")

operations = ["+", "-", "*", "/", "mix"]
choice = get_operation("Choose operation (+, -, *, / or mix): ", operations)
print(f"You chose: {choice}")

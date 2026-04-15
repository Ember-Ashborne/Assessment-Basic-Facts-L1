"""Text input checker for the math quiz assessment."""


def string_check(question, valid_options, error):
    """Ask for a text response and check it is valid."""

    while True:
        response = input(question).strip().lower()

        if response in valid_options:
            return response

        print(error)


response = string_check(
    "Enter yes or no: ",
    ["yes", "no", "y", "n"],
    "Please enter yes / no",
)
print(f"You entered: {response}")

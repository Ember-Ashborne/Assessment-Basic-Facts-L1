"""Integer input checker for the math quiz assessment."""


def int_check(question, low, high=None):
    """Ask for an integer within the allowed range."""

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

number = int_check("Enter a number from 1 to 10: ", 1, 10)
print(f"You entered: {number}")

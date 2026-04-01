"""Yes/no input checker for the math quiz assessment."""


def yes_no(question):
    """Ask a yes/no question and return only 'yes' or 'no'."""

    while True:
        response = input(question).strip().lower()

        if response in ("yes", "y"):
            return "yes"
        elif response in ("no", "n"):
            return "no"
        else:
            print("Please enter yes / no")

answer = yes_no("Do you want to continue? ")
print(f"You entered: {answer}")

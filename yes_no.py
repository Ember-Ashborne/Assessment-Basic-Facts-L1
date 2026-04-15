"""Yes/no input checker for the math quiz assessment."""


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

answer = yes_no("Do you want to continue? ")
print(f"You entered: {answer}")

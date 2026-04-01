"""End-of-game feedback helper for the math quiz assessment."""


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

percentage = float(input("Enter a score percentage: "))
print(result_feedback(percentage))

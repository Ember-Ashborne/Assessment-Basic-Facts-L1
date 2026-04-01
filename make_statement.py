"""Heading helper for the math quiz assessment."""


def make_statement(statement, decoration):
    """Print a decorated heading."""

    ends = decoration * 3
    print(f"\n{ends} {statement} {ends}")


make_statement("Math Quiz Heading Demo", "=")

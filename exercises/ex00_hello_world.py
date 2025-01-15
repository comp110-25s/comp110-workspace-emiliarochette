"""My first exercise in COMP110!"""

__author__ = "730823433"


def greet(name: str) -> str:
    """Return a greeting to the given name."""
    return "Hello, " + name + "!"


if __name__ == "__main__":

    print(greet(name=input("What is your name? ")))

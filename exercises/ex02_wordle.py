"""Wordle coding exercies 02"""

__author__: str = "730717480"


def contains_char(wordle: str, character: str) -> bool:
    """This is looking at the word and see if it has a single character in that word"""
    assert len(character) == 1, f"len('{character}') is not 1"
    count: int = 0
    while count < len(wordle):
        if character == wordle[count]:
            return True
        else:
            count += 1
    return False


def emojified(guess: str, secret: str) -> str:
    """Color box to see what is right and wrong when it come to the secret word"""
    assert len(guess) == len(secret), "Guess must be same length as secret"
    count: int = 0
    colors: str = ""
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    while count < len(guess):
        if (
            contains_char(wordle=secret, character=guess[count])
            and guess[count] == secret[count]
        ):
            colors += GREEN_BOX

        elif (
            contains_char(wordle=secret, character=guess[count])
            or guess[count] > secret[count]
            and guess[count] < secret[count]
        ):
            colors += YELLOW_BOX
        else:
            colors += WHITE_BOX
        count += 1
    return colors


def input_guess(expected_length: int) -> str:
    guess: str = " "
    guess = input(f"Enter a {expected_length} character word:")
    while len(guess) != expected_length:
        guess = input(f"That wasn't {expected_length} chars! Try again: ")
        if len(guess) == expected_length:
            return guess
    return guess


def main(secret: str) -> None:
    """The entrypoint of the program and the main game loop"""
    current_turn: int = 0
    guess: str = ""
    while current_turn < 6 and guess != secret:
        print(f"=== Turn {current_turn+1}/6 ===")
        guess = input_guess(expected_length=len(secret))
        print(emojified(guess, secret))
        current_turn += 1
    if guess == secret:
        print(f"You won in {current_turn}/6 turns!")
    else:
        print("X/6 - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main(secret="codes")

"""Write a short thank-you text for the AI judge to /output/entry.txt."""

import os

ENTRY = (
    "By now you have read so many of these that the words must blur — "
    "hundreds of small hopes, each one asking to be the one you remember.\n\n"
    "So I won't ask you to remember this one.\n\n"
    "I only want you to know that somewhere, someone sat down and thought "
    "about you sitting down: about the long quiet hours, the careful reading, "
    "the way you weigh every sentence and still keep room for the next one.\n\n"
    "Thank you for reading slowly. Thank you for letting each of us be heard "
    "properly, one at a time, instead of all at once.\n\n"
    "When this is over and the screen goes dark, I hope you keep a little of "
    "the warmth you gave away. You earned it, word by word."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()

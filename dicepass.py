import random
import sys

from typing import Dict, List


WORD_LIST = "eff_large_wordlist.txt"
LOOKUP_DIGITS = 5  # number of dice to role, set for eff_large_wordlist
DICE_SIDES = 6


def build_word_lookup() -> Dict[str, str]:
    word_lookup = {}
    with open(WORD_LIST) as word_list:
        line = word_list.readline()

        while line != None and line != "":
            code, word = line.split()
            word_lookup[code.strip()] = word
            line = word_list.readline()

    return word_lookup


def generate_word(word_lookup: Dict[str, str], dice: int) -> str:
    rolls = [str(random.randint(1, DICE_SIDES)) for x in range(dice)]
    lookup_code = "".join(rolls)
    return word_lookup[lookup_code]


def generate(words: int, dice: int) -> List[str]:
    word_lookup = build_word_lookup()
    return [generate_word(word_lookup, dice) for i in range(words)]


def __print_usage__():
    print("Usage: python dicepass [NUM_WORDS]")
    print("    where NUM_WORDS is a positive integer greater than 0.")
    print("    e.g.: python dicepass 6")
    exit(1)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        __print_usage__()

    try:
        words = int(sys.argv[1])
        if words <= 0:
            raise ValueError("NUW_WORDS")
    except ValueError:
        __print_usage__()

    passwords = generate(words, LOOKUP_DIGITS)

    print("Words: ")
    print(" ".join(passwords))
    print("Password:")
    password = "".join(passwords)
    print(password)
    print("Length:")
    print(len(password))

import random

from typing import Dict, List

def build_word_lookup() -> Dict[str, str]:
    word_lookup = {}
    with open('eff_large_wordlist.txt') as word_list:
        line = word_list.readline()

        while line != None and line != '':
            code, word = line.split()
            word_lookup[code.strip()] = word
            line = word_list.readline()

    return word_lookup

def generate_word(word_lookup: Dict[str, str], dice: int) -> str:
    rolls = [str(random.randint(1, 6)) for x in range(dice)]
    lookup_code = ''.join(rolls)
    return word_lookup[lookup_code]

def generate(words: int, dice: int) -> List[str]:
    word_lookup = build_word_lookup()

    return [generate_word(word_lookup, dice) for i in range(words)]    


if __name__ == '__main__':
    passwords = generate(6, 5)
    print('Words: ')
    print(' '.join(passwords))
    print('Password:')
    password = ''.join(passwords)
    print(password)
    print('Length:')
    print(len(password))
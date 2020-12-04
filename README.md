# Dice Pass

Simple, dependency free Python implementation of https://www.eff.org/dice.

Generate easy to remember, long (and therefore more secure) passwords.

## Usage:
Usage: python dicepass [NUM_WORDS]
    where NUM_WORDS is a positive integer greater than 0.
    e.g.: python dicepass 6

## Security:
No data is stored or transmitted in any form. The passwords is generated to stdout and will be visible on scree. Someone standing behind you might see it.

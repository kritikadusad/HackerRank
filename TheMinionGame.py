"""
Kevin and Stuart want to play the 'The Minion Game'.

Game Rules

Both players are given the same string, .
Both players have to make substrings using the letters of the string .
Stuart has to make words starting with consonants.
Kevin has to make words starting with vowels. 
The game ends when both players have made all possible substrings. 

Scoring
A player gets +1 point for each occurrence of the substring in the string .

For Example:
String  = BANANA
Kevin's vowel beginning word = ANA
Here, ANA occurs twice in BANANA. Hence, Kevin will get 2 Points. 

Your task is to determine the winner of the game and their score.

Input Format

A single line of input containing the string . 
Note: The string  will contain only uppercase letters: .

Constraints



Output Format

Print one line: the name of the winner and their score separated by a space.

If the game is a draw, print Draw.

Example:
>>> minion_game("BANANA")
'Stuart 12'

"""


def minion_game(string):
    vowels = {"A", "E", "I", "O", "U"}
    len_word = len(string)
    Stuart = []
    Kevin = []

    for i in range(len_word):
        if string[i] not in vowels:
            for j in range(i + 1, len_word + 1):
                Stuart.append(string[i:j])
    for i in range(len_word):
        if string[i] in vowels:
            for j in range(i + 1, len_word + 1):
                Kevin.append(string[i:j])
    if len(Stuart) > len(Kevin):
        print("Stuart {}".format(len(Stuart)))
    elif len(Stuart) == len(Kevin):
        print("Draw")
    else:
        print("Kevin {}".format(len(Kevin)))

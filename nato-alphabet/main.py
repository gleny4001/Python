import pandas

nato_alphabet = pandas.read_csv("nato_phonetic_alphabet.csv")

# TODO 1. Create a dictionary in this format:
nato = {row.letter: row.code for (index, row) in nato_alphabet.iterrows()}

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.


def generate_phonetic():
    user_word = input("Enter a word : ").upper()
    try:
        user_word_nato = [nato[letter] for letter in user_word]
    except KeyError:
        print("Please type only alphabet")
        generate_phonetic()
    else:
        print(user_word_nato)


generate_phonetic()
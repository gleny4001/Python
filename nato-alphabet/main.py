
import pandas
nato_alphabet = pandas.read_csv("nato_phonetic_alphabet.csv")


#TODO 1. Create a dictionary in this format:
nato = {row.letter:row.code for (index, row) in nato_alphabet.iterrows()}
print(nato)
#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
user_word = input("Enter a word : ").upper()

user_word_nato = [nato[letter] for letter in user_word]

print(user_word_nato)
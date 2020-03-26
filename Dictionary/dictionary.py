import json
from difflib import get_close_matches

# Opens the json file
data = json.load(open("data.json"))

# The program finds definition for a word using json file,
# and detects typo and search right word for the user just like google


def translate(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif word.capitalize() in data:
        return data[word.capitalize()]
    elif word.upper() in data:
        return data[word.upper()]
    elif len(get_close_matches(word, data.keys())) > 0:
        guess = get_close_matches(word, data.keys())[0]
        print("Showing result for %s " % guess)
        return data[guess]
    else:
        return "%s does not match any documents" % word


def main():
    w = input("Type a word: ")
    output = translate(w)
    if type(output) == list:
        for item in output:
            print("Definition : " + item)
    else:
        print(output)


while True:
    main()
    r = input("\nPress enter or any keys to continue. (Type -1 to quit) ")
    if r == str(-1):
        print("Good bye")
        break


# Python program to convert text into JSON file

import json

filename = "resources/dictionaries/english3.txt"

with open(filename) as f:
    words = f.readlines()


word_list = []
for i in words:
    word_list.append(i)

print(f"Word count: {len(word_list)}")

with open("resources/dictionaries/wordlist_english.json", "w") as json_file:
    json.dump(word_list, json_file)


def load_dutch_library():
    with open("resources/dictionaries/wordlist_english.json") as words:
        new_word_list = []
        data = json.load(words)
        for i in data:
            new_word_list.append(i.rstrip())

    with open("resources/dictionaries/wordlist_english.json", "w") as json_file:
        json.dump(new_word_list, json_file)

load_dutch_library()
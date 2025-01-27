import os

with open("/home/ausadian98/git/workspace/github.com/bookbot/books/frankenstein.txt") as f:
    file_contents = f.read()
    lowered_string = file_contents.lower()
    
    freq = {}

    for letter in lowered_string:
        if letter in freq:
            freq[letter] += 1
        else:
            freq[letter] = 1
    print(freq)
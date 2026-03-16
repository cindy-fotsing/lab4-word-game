import random

def main():
    letters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    letter = random.choice(letters)
    used_letters = []

    if letter not in used_letters:
        used_letters.append(letter)
        return letter
    
    word_list = ["apple", "house", "smile", "grape", "chair", "table", "cindy"]
    print(("_" * 5))

def guess():
    for i in range(5):
        
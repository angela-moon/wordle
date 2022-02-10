import wordle as w
from wordlist import answers, guesses

basic = w.Wordle(answers, guesses)

playing = True

def choose():
    while playing:
        print("\nWhat would you like to do?")
        print("A: Play wordle in the terminal")
        print("B: Solve today's wordle")
        print("C: List ten starting words")
        print("D: Done")
        choice = input("A/B/C/D: ")
        
        if choice.upper() == "A":
            basic.wordle()
            continue
        elif choice.upper() == "B":
            basic.solver()
            continue
        elif choice.upper() == "C":
            letters = basic.most_common_letters_ans()
            print(basic.find_starter_words(letters, 10))
        elif choice.upper() == "D":
            break
        
choose()
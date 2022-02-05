from collections import Counter, OrderedDict
from operator import itemgetter
import random

class Wordle:
    def __init__(self, words, guesses=None):
        self.words = words
        self.guesses = guesses
        
    def get_words(self):
        return self.words
    
    def get_guesses(self):
        return self.guesses
    
    def set_words(self, new_words):
        self.words = new_words
        
    def set_guesses(self, new_guesses):
        self.guesses = new_guesses
    
    # most_common_letters() uses no parameters and only relies on the object's properties.
    # The method iterates through the words in the object's word list and sets the word equal to a list of it's unique characters. Each unique letter is appended to a list of all letters in the word list, which then uses the most_common() function to sort the list by frequency. The method then creates a list of only the letters and returns it.
    
    def most_common_letters_ans(self): # Finds the most common letters in all of the possible answers, disregarding duplicate letters in one word (if letter in letters, pass)
        letters = []
        
        for word in self.words:
            word = set(word)
            for letter in word:
                letters.append(letter)
            
        c_letters = Counter(letters) # counter letters
        c_letters = c_letters.most_common()
        f_letters = [] # formatted letters

        for letter, count in c_letters:
            f_letters.append(letter)
            
        return f_letters

    def most_common_letters(self): # Finds the most common letters in all of the possible answers and guesses, disregarding duplicate letters in one word (if letter in letters, pass)
        letters = []
        if self.guesses:
            for word in self.guesses:
                word = set(word)
                for letter in word:
                    letters.append(letter)
        for word in self.words:
            word = set(word)
            for letter in word:
                letters.append(letter)
            
        c_letters = Counter(letters) # counter letters
        c_letters = c_letters.most_common()
        f_letters = [] # formatted letters

        for letter, count in c_letters:
            f_letters.append(letter)
            
        return f_letters
    
    # find_starter_words() uses two parameters: most_common, a list of the letters sorted in how common they are, and num, an integer that indicates the number of starter words they want returned. 
    # The method takes the list of words from the object and iterates through each word, appending to the the list i_letters the index of how common that letter is in the most_common list. It then adds the indexes for each word and appends the sum and the word to the dictionary i_words. After sorting the dictionary by key, the program iterates through the words and checks whether the word, when alphabetized and turned into a list, is equal to an alphabetized list of all of the unique letters. If it is, that means all of the characters in the string are unique and can be a considered a "good" starter word. All of these words are appended to a list, which is then sliced to the num first inputted and returned.
    
    def find_starter_words_ans(self, most_common_list, num):
        i_letters = [] # working list of all letters in words assigned to index of most_common
        i_words = {} # list of sums of numerical values of letters in words
        for word in self.words: 
            for letter in word:
                i_letters.append(most_common_list.index(letter))
            i_words[word] = sum(i_letters)
            i_letters.clear()
        
        i_words = OrderedDict(sorted(i_words.items(), key=itemgetter(1)))
        
        w_words = []
        
        for word in i_words:
            if sorted(list(word)) == sorted(list(set(word))):
                w_words.append(word)
            
        return w_words[0:num]
    
    # same as find_starter_words_ans() except for both possible answers and guesses
    
    def find_starter_words(self, most_common_list, num):
        i_letters = [] # working list of all letters in words assigned to index of most_common
        i_words = {} # list of sums of numerical values of letters in words
        if self.guesses:
            for word in self.guesses: 
                for letter in word:
                    i_letters.append(most_common_list.index(letter))
                i_words[word] = sum(i_letters)
                i_letters.clear()
            
        for word in self.words: 
            for letter in word:
                i_letters.append(most_common_list.index(letter))
            i_words[word] = sum(i_letters)
            i_letters.clear()
        
        i_words = OrderedDict(sorted(i_words.items(), key=itemgetter(1)))
        
        w_words = []
        
        for word in i_words:
            if sorted(list(word)) == sorted(list(set(word))):
                w_words.append(word)
            
        return w_words[0:num]
    
    # solver() uses no parameters and only relies on the object's properties.
    # After splitting the input into different letters, it checks what the second charcter (the integer) is and based on its value, sorts the letters into different lists. Because yellow and green are based on the letter's position in the word, those are dictionaries with the index as the value. For each letter, it goes through a process of removing any words that don't match the information from the guess from a list of possible words. For green, any words where the letter doesn't equal the word's letter at the same index. For yellow, any words that don't include the letter are removed. In case there aren't any green letters, all words that have the same letter in the same position are removed as well. For gray, any words that include the letter are removed. After each guess, the program asks the user if the game was won after the guess. If it was, the program ends, but if it wasn't, it continues until it is.
    
    def solver(self):
        guesses = 0
        possible = list(self.words)
        
        green = {}
        yellow = {}
        gray = []
        
        while guesses < 6:
            guess = input("Enter the letters of your guess with a space separating the letters, formatted like [letter][0 (gray), 1 (yellow), or 2 (green)] e.g. A2 P0 P0 L1 E1: ")
            guess = guess.split()
            for letter in guess:
                if int(letter[1]) == 0:
                    gray.append(letter[0].upper())
                elif int(letter[1]) == 1:
                    yellow[letter[0].upper()] = guess.index(letter)
                elif int(letter[1]) == 2:
                    green[letter[0].upper()] = guess.index(letter)
            for word in self.words:
                if green:
                    for letter, index in green.items():
                        if word in possible:
                            if letter != word[index]:
                                possible.remove(word)
                if yellow:
                    for letter, index in yellow.items():
                        if word in possible:
                            if letter not in word:
                                possible.remove(word)
                            elif letter == word[index]:
                                possible.remove(word)
                if gray:
                    for letter in gray:
                        if word in possible:
                            if letter in word:
                                possible.remove(word)
                
            print("Try:")
            for word in possible:
                print(word, end=" ")
            print("")
            won_val = input("Game won? Y/N ")
            if won_val.upper() == "Y":
                break
            guesses += 1
            green.clear()
            yellow.clear()
            gray.clear()
            
    # solver() uses no parameters and only relies on the object's properties.
    # A random word is chosen from the answer list. The game asks for a five-letter guess and based on similar criteria from the previous method, in reverse, returns a letter and a symbol as indicated in the instructions. This repeats until the user guesses the word or six guesses are up.
            
    def wordle(self):
        special = random.choice(self.words)
        guesses = 0
        won = False
        print("--------------- Console WORDLE!! ---------------")
        print("Inspired by https://www.powerlanguage.co.uk/wordle/")
        print("Instructions: Try to guess a random word in under six guesses. After a guess, each letter will have a symbol next to it: ☑ if it's in the word and in the right place, ☐ if it's in the word but in the wrong place, and ☒ if the letter isn't in the word at all. ")
        while guesses < 6:
            i = 0
            guess = input("Guess a five-letter word: ")
            if self.guesses:
                if guess.upper() not in self.guesses and guess.upper() not in self.words:
                    print("Invalid word")
                    continue
            else:
                if guess.upper() not in self.words:
                    print("Invalid word")
                    continue
            if guess.upper() == special:
                won = True
                break
            special_list = list(special)
            for letter in guess:
                if letter.upper() == special[i]:
                    print(f"{letter.upper()}☑ ", end="")
                    special_list.remove(letter.upper())
                elif letter.upper() in special_list:
                    print(f"{letter.upper()}☐ ", end="")
                    special_list.remove(letter.upper())
                else:
                    print(f"{letter.upper()}☒ ", end="")
                i += 1
            guesses += 1
            print("")
        if won:
            print(f"Congratulations! The word was {special}, guesses: {guesses+1}")
            quit()
        else:
            print(f"Sorry, the word was {special}")
import wordle as w
from wordlist import answers, guesses

basic = w.Wordle(answers, guesses)

basic.wordle()
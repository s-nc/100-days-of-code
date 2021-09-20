# Average Typing Speed Test.
# Ensure random-word and pyyaml are installed

from tkinter import *
from random_word import RandomWords
import time

num_words = 25
words = RandomWords()
words = list(words.get_random_words())[:num_words]

mistakes = -1
n = -1


# ----------------------------- HANDLERS -------------------------------- #
def next_word(e):
    global words, current_word, mistakes, n
    n += 1
    if n >= num_words:
        type_input.delete(0, 'end')
        end_test()
    else:
        if type_input.get() != current_word.cget("text"):
            mistakes += 1
        current_word.config(text=words[n])
        type_input.delete(0, 'end')
        print(mistakes)
        return current_word


def start_timer():
    global start_time
    start_time = time.time()
    next_word(0)


def stop_timer():
    global time_taken
    time_taken = time.time() - start_time


def end_test():
    global time_taken, mistakes
    stop_timer()
    time_mins = time_taken / 60
    wpm = num_words / time_mins
    accuracy = (1 - mistakes/num_words)*100
    current_word.config(text=f"Your speed was {wpm: .1f} words per minute, with {accuracy: .1f}% accuracy.",
                        font=("Arial", 12), fg='grey')


def reset():
    global words, mistakes, n
    words = RandomWords()
    words = list(words.get_random_words())[:num_words]
    mistakes = -1
    n = -1
    current_word.config(text="Welcome! Click Start to begin.", font=("Arial", 30), bg='#fff', fg='green')


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Typing Speed")
window.config(padx=30, pady=30, width=500, height=500)
window.resizable(0, 0)

current_word = Label(text="Welcome! Click Start to begin.", font=("Arial", 30), bg='#fff', fg='green')
current_word.grid(column=1, row=1, pady=10)

# Input Box
type_here = Label(text="Type Here:")
type_here.grid(column=1, row=2)
type_input = Entry()
type_input.grid(column=1, row=3)

# Buttons
f1 = Frame(window)
start = Button(f1, text="Start", command=start_timer)
start.grid(column=1, row=0, padx=10, pady=10)
reset = Button(f1, text="Reset", command=reset)
reset.grid(column=2, row=0, padx=10, pady=10)
f1.grid(column=1, row=4)

window.bind('<Return>', next_word)

window.mainloop()

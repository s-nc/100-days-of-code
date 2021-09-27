from tkinter import *
import pandas as pd
import random
BACKGROUND_COLOR = "#B1DDC6"


# ---------------------------- OBTAIN FRENCH/ ENGLISH WORDS ------------------------------- #
try:
    word_data = pd.read_csv("./data/french_words.csv")
except FileNotFoundError:
    word_data = pd.read_csv("./data/words_to_learn.csv")
word_dict = pd.DataFrame.to_dict(word_data, orient="records")
word = {}


# ---------------------------- FUNCTIONS ON BUTTON CLIK / TIMER ------------------------------- #
def new_word():
    global word, flip_timer
    window.after_cancel(flip_timer)
    word = random.choice(word_dict)
    canvas.itemconfig(word_display, text=word['French'], fill="black")
    canvas.itemconfig(title, text="French", fill="black")
    canvas.itemconfig(card_side, image=card_front)
    flip_timer = window.after(3000, flip_card)


def correct_word():
    global word
    word_dict.remove(word)
    to_learn = pd.DataFrame.from_dict(word_dict)
    to_learn.to_csv("./data/words_to_learn.csv", index=False)
    new_word()


def flip_card():
    global word
    canvas.itemconfig(card_side, image=card_back)
    canvas.itemconfig(word_display, text=word['English'], fill="white")
    canvas.itemconfig(title, text="English", fill="white")

    
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Flashcards")
window.config(padx=40, pady=40, bg=BACKGROUND_COLOR)
window.minsize(width=800, height=600)

flip_timer = window.after(3000, flip_card)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front = PhotoImage(file="./images/card_front.png")
card_back = PhotoImage(file="./images/card_back.png")
card_side = canvas.create_image(400, 263, image=card_front)
title = canvas.create_text(400, 150, text="French", font=("Arial", 40, "italic"))
word_display = canvas.create_text(400, 263, text="word", font=("Arial", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

# Buttons
cross = PhotoImage(file="./images/wrong.png")
unknown = Button(image=cross, highlightthickness=0, command=new_word)
unknown.grid(row=1, column=1)

tick = PhotoImage(file="./images/right.png")
correct = Button(image=tick, highlightthickness=0, command=correct_word)
correct.grid(row=1, column=0)

new_word()

window.mainloop()

import requests
from tkinter import *

# Fetch Kanye quote.
def quote_kanye():
    response = requests.get(url="https://api.kanye.rest/")
    response.raise_for_status()
    quotation = response.json()["quote"]
    canvas.itemconfig(quote_label, text=quotation)

    
# UI Setup.
window = Tk()
window.title("Kanye Motivation")
window.config(padx=30, pady=30)

canvas = Canvas(width=300, height=414)
speech_bubble = PhotoImage(file="background.png")
background = canvas.create_image(150, 207, image=speech_bubble)
quote_label = canvas.create_text(150, 207, text="Welcome to my fountain of wisdom."
                                 , width=250, font=("Arial", 20, "bold"), fill="white")
canvas.pack()

kanye = PhotoImage(file="kanye.png")
kanye_button = Button(image=kanye, command=quote_kanye)
kanye_button.pack()


window.mainloop()


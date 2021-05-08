from tkinter import *
import pandas

# ---------------------------------Constants----------------------------------#
BACKGROUND_COLOR = "#B1DDC6"
french_word = ""
english_word = ""

# ---------------------------------data----------------------------------#
df = pandas.read_csv("data/french_words.csv")


def random_word():
    global french_word
    global english_word
    random_row = df.sample()
    french_word = random_row.French.item()
    english_word = random_row.English.item()


# -------------------------------Change flash card-------------------------------#

def delay(count):
    if count < 3:
        window.after(1000, delay, count + 1)
    else:
        canvas.itemconfig(language_display, text="English", fill="white")
        canvas.itemconfig(flash_card_img, image=back_card)
        canvas.itemconfig(french, text=english_word, fill="white")


def start():
    random_word()
    canvas.itemconfig(language_display, text="French")
    # change the card img back to front and update the text
    canvas.itemconfig(flash_card_img, image=front_card)
    canvas.itemconfig(french, text=french_word)
    delay(0)


# ---------------------------UI Setup----------------------------------#

# Window setup
window = Tk()
window.title("Flash cards")
window.resizable(width=False, height=False)
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
# Canvas
canvas = Canvas(width=800, height=525, bg=BACKGROUND_COLOR, highlightthickness=0)

# flash card img
front_card = PhotoImage(file="images/card_front.png")
back_card = PhotoImage(file="images/card_back.png")
flash_card_img = canvas.create_image(400, 260, image=front_card)
canvas.grid(column=0, row=0, columnspan=2)

# Buttons
wrong_button_img = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_button_img, highlightthickness=0, command=start)
wrong_button.grid(column=0, row=1)

right_button_img = PhotoImage(file="images/right.png")
right_button = Button(image=right_button_img, highlightthickness=0, command=start)
right_button.grid(column=1, row=1)

# Text

language_display = canvas.create_text(400, 150, text="French", font=("Ariel", 40, "italic"))
french = canvas.create_text(400, 263, font=("Ariel", 60, "bold"), text=french_word)
start()

window.mainloop()

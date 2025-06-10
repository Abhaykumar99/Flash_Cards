from tkinter import *
import pandas as pd
import random
import os

# yahan se files ka path set kar rahe hain — __file__ se current script ki location milti hai
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ORIGINAL_FILE = os.path.join(BASE_DIR, "data", "french_words.csv")
PROGRESS_FILE = os.path.join(BASE_DIR, "data", "words_to_learn.csv")

BACKGROUND = "#B1DDC6"
flip_timer = None
current_card = {}

# agar pehle se progress file hai toh wohi load karo, warna original se shuru karo
try:
    df = pd.read_csv(PROGRESS_FILE)
except FileNotFoundError:
    df = pd.read_csv(ORIGINAL_FILE)

# DataFrame ko list of dicts mein convert kiya — aasaan hoga random choose karne ke liye
to_learn = df.to_dict(orient="records")


def next_card():
    global current_card, flip_timer

    # agar pehle se flip timer chal raha hai toh cancel karo
    if flip_timer:
        window.after_cancel(flip_timer)

    # random card choose karo baaki list mein se
    current_card = random.choice(to_learn)

    # front side dikhao — French word
    canvas.itemconfig(card_background, fill="white")
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")

    # 3 second baad automatically flip ho jaayega English side par
    flip_timer = window.after(3000, flip_card)


def flip_card():
    # back side dikhao — English meaning
    canvas.itemconfig(card_background, fill="#1a1a2e")
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")


def known():
    # ye word yaad ho gaya — list se hata do
    to_learn.remove(current_card)

    # bacha hua data save karo CSV mein progress ke liye
    remaining = pd.DataFrame(to_learn)
    if not remaining.empty:
        remaining.to_csv(PROGRESS_FILE, index=False)
    else:
        # sab words seekh liye! progress file delete karo aur done dikhao
        if os.path.exists(PROGRESS_FILE):
            os.remove(PROGRESS_FILE)
        canvas.itemconfig(card_word, text="🎉 Sab Seekh Liya!", fill="black")
        canvas.itemconfig(card_title, text="", fill="black")
        return

    next_card()


# ── Window setup ────────────────────────────────────
window = Tk()
window.title("Day 30 – Flash Cards")
window.config(bg=BACKGROUND, padx=50, pady=50)


# Canvas par card draw karo
canvas = Canvas(width=800, height=526, bg=BACKGROUND, highlightthickness=0)
card_background = canvas.create_rectangle(30, 30, 770, 496,
                                          fill="white", outline="", width=0)
# card ka title — "French" ya "English"
card_title = canvas.create_text(400, 180, text="", font=("Arial", 40, "italic"))
# main word jo dikhna hai
card_word  = canvas.create_text(400, 300, text="", font=("Arial", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

# Nahi pata button — next card dikhao
wrong_btn = Button(text="✗  Nahi Pata", font=("Arial", 14), bg="#e74c3c",
                   fg="white", command=next_card, padx=10, pady=5)
wrong_btn.grid(row=1, column=0, pady=20)

# Pata hai button — list se hata do
right_btn = Button(text="✓  Pata Hai", font=("Arial", 14), bg="#27ae60",
                   fg="white", command=known, padx=10, pady=5)
right_btn.grid(row=1, column=1, pady=20)


# app shuru hote hi pehla card dikhao
next_card()
window.mainloop()

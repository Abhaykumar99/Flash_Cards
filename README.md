# 🗂️ Flash Cards – French to English

A **language learning flashcard app** built with Tkinter and Pandas. Learn French words with automatic card flipping and progress saving.

## 📁 Project Structure

```
flash_cards/
├── flash_cards.py          # Main application file
└── data/
    ├── french_words.csv    # Original word list (French + English)
    └── words_to_learn.csv  # Auto-generated: remaining words to learn
```

## ✨ Features

- Flashcard flips automatically after **3 seconds** to reveal English meaning
- **Progress saving** — words you know are removed from the deck
- On next run, resumes from where you left off
- Completion message when all words are learned 🎉

## 🚀 How to Run

```bash
cd flash_cards
python flash_cards.py
```

## 🛠️ Requirements

```bash
pip install pandas
```
- Python 3.x
- `tkinter` (built-in with Python)

## 🕹️ How to Use

| Button | Action |
|--------|--------|
| ✗ Nahi Pata | Skip — show next card |
| ✓ Pata Hai | Mark as known — remove from deck |

> After 3 seconds the card automatically flips to show the **English** translation.

## 📂 Data Format (`french_words.csv`)

```
French,English
partir,to leave
rester,to stay
...
```

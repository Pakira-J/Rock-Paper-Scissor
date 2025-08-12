# 🎮 Rock Paper Scissors Game

![Python](https://img.shields.io/badge/python-v3.6+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Version](https://img.shields.io/badge/version-1.0-orange.svg)

<div align="center">
  <img src="https://media.giphy.com/media/l0HlQXlQ3nHyLMvte/giphy.gif" width="400" alt="Rock Paper Scissors Animation">
</div>

A simple and fun command-line Rock Paper Scissors game built in Python. This is my first Python game project, created as part of my programming journey!

## 📋 Table of Contents

- [Description](#-description)
- [Features](#-features)
- [Demo](#-demo)
- [Installation](#-installation)
- [How to Play](#-how-to-play)
- [Code Overview](#-code-overview)
- [What I Learned](#-what-i-learned)
- [Future Improvements](#-future-improvements)
- [Author](#-author)

## 📝 Description

This is a classic Rock Paper Scissors game where you play a single round against the computer. The game follows the traditional rules:

- 🪨 **Rock** beats ✂️ **Scissors**
- ✂️ **Scissors** beats 📄 **Paper**  
- 📄 **Paper** beats 🪨 **Rock**

The computer makes random choices, and the game determines the winner after each round.

## ✨ Features

- 🎯 Simple single-round gameplay
- 🤖 Random computer opponent
- ✅ Input validation for player choices
- 🏆 Clear win/lose/tie messaging
- 💻 Clean command-line interface
- 📱 Case-insensitive input handling

## 🎬 Demo

<div align="center">
  <img src="https://media.giphy.com/media/26BRuo6sLetdllPAQ/giphy.gif" width="300" alt="Gaming GIF">
</div>

### Sample Gameplay:
```
Enter your choice [rock, paper, scissors] : rock
Player --> rock :: Computer --> scissors
Congrats! Player wins.
```

```
Enter your choice [rock, paper, scissors] : paper
Player --> paper :: Computer --> scissors
Try again. Computer wins.
```

```
Enter your choice [rock, paper, scissors] : scissors
Player --> scissors :: Computer --> scissors
It's a tie!
```

## 🚀 Installation

1. **Clone the repository:**
```bash
git clone https://github.com/joydeeppakira/rock-paper-scissors.git
```

2. **Navigate to the project directory:**
```bash
cd rock-paper-scissors
```

3. **Run the game:**
```bash
python rock_paper_scissors.py
```

### Requirements
- Python 3.6 or higher
- No additional libraries required

<div align="center">
  <img src="https://media.giphy.com/media/LmNwrBhejkK9EFP504/giphy.gif" width="200" alt="Python Logo">
</div>

## 🎯 How to Play

1. **Run the script** using `python rock_paper_scissors.py`
2. **Enter your choice** when prompted:
   - Type `rock`, `paper`, or `scissors`
   - Input is case-insensitive
3. **View the results** - see both choices and who wins!
4. **Run again** to play another round

## 🏗️ Code Overview

The game consists of two main functions:

### `game_choice()`
- Gets player input for their choice
- Generates random computer choice
- Returns both choices in a dictionary

### `game_win(player, computer)`
- Validates player input
- Compares choices using game logic
- Returns appropriate win/lose/tie message

### Game Logic Flow:
```
Player Input → Validation → Computer Choice → Comparison → Result Display
```

<div align="center">
  <img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif" width="250" alt="Code GIF">
</div>

## 🎓 What I Learned

Building this game as my first Python project helped me understand:

- ✅ **Function definition and calling**
- ✅ **Dictionary data structures**
- ✅ **Conditional statements (if/elif/else)**
- ✅ **User input handling with `input()`**
- ✅ **String methods like `.lower()`**
- ✅ **Random number generation with `random.choice()`**
- ✅ **Boolean logic and comparisons**
- ✅ **Code organization and structure**

## 🔮 Future Improvements

Here are some ideas to make the game even better:

- [ ] **Multi-round gameplay** with score tracking
- [ ] **Best of N rounds** option
- [ ] **Play again functionality** without restarting
- [ ] **Player name input** for personalization
- [ ] **ASCII art** for rock/paper/scissors
- [ ] **Color output** using libraries like `colorama`
- [ ] **Game statistics** (win percentage, etc.)
- [ ] **GUI version** using `tkinter`
- [ ] **Extended version** (Rock Paper Scissors Lizard Spock)

<div align="center">
  <img src="https://media.giphy.com/media/26tn33aiTi1jkl6H6/giphy.gif" width="300" alt="Future Ideas">
</div>

## 📄 Project Info

- **Created:** October 1, 2023
- **Language:** Python
- **Type:** Console Game
- **Status:** Complete ✅

## 👤 Author

**Joydeep Pakira**
- GitHub: [@joydeeppakira](https://github.com/joydeeppakira)
- First Python Game Project! 🎉

<div align="center">
  <img src="https://media.giphy.com/media/26tn8zxWe34qWdJzq/giphy.gif" width="200" alt="Celebration">
</div>

## 🙏 Acknowledgments

- Thanks to the Python community for excellent documentation
- Inspired by the classic Rock Paper Scissors game
- Special thanks to online tutorials that helped me learn Python basics

## 📜 License

This project is open source and available under the MIT License.

---

<div align="center">
  <b>⭐ If you found this project interesting, please consider giving it a star! ⭐</b>
  <br><br>
  <img src="https://media.giphy.com/media/3oz8xIsloV7zOmt81G/giphy.gif" width="150" alt="Thank you">
</div>

---

*This README was created with ❤️ as part of my Python learning journey*
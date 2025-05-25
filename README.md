# ✊📄✂️ Rock-Paper-Scissors: Python Practice Project

This project is a simple yet powerful demonstration of my learning journey in Python — specifically focusing on **randomization**, **lists**, **input handling**, and **control flow**. 
I built a Rock-Paper-Scissors game that pits the player against a computer opponent using randomly generated choices.

---

## 🚀 What I Learned

### 📚 Lists and Indexing
Stored ASCII representations of Rock, Paper, and Scissors in a list. Then accessed them via player/computer choices:

gameImages = [Rock, Paper, Scissors]
print(gameImages[player])

### 🧠 Control Flow & Game Logic
Implemented the rules of Rock-Paper-Scissors using if, elif, and else to control the game outcome:

if player == 0 and computer == 2:
    print("You win!")
elif player == 2 and computer == 0:
    print("You lose!")

### 🚫 Input Validation
Added a simple check to ensure the user input was within a valid range (0–2). If not, the game ends with a message:

if player >= 3 or player < 0:
    print("Not a valid number! You lose!")


### 🎲 Randomization
Used Python’s built-in `random.randint()` to simulate the computer’s unpredictable moves:
```python
computer = random.randint(0, 2)

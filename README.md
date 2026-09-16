# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

- The game is a number-guessing challenge where the player picks a difficulty level and tries to guess the hidden number within a set range and number of attempts.
- The main bugs we found were reversed hints, inconsistent secret-state handling across reruns, and difficulty settings that did not match the actual game range or attempts.
- We fixed the logic by moving the core rules into `logic_utils.py`, correcting the comparison logic, resetting session state properly, and validating the behavior with pytest.

## Demo Walkthrough

1. The user opens the app and selects the Normal difficulty, which sets the valid guess range to 1 to 100.
2. The user enters a guess of 40, and the game responds with "Too Low" because the secret number is higher than 40.
3. The user then enters a guess of 70, and the game responds with "Too High" because the secret number is lower than 70.
4. After each guess, the score updates correctly and the attempt count advances in the proper order.
5. The user makes a final correct guess, the game shows the win message, and the round ends successfully.

## 🧪 Test Results

```
# Paste your pytest output here, e.g.:
# pytest tests/
# ========================= X passed in 0.XXs =========================
```

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, describe the Enhanced UI changes here — a screenshot is optional]

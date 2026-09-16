# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?

The game consisted of a plain awkward but simple interface with a title, short description, debug logger, a guess entry box, and options for "Submit Game" & New Game.
Upon playing, it notified the user of their attempts and success. 

- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").

  The difficulty modes are not good representation of scaling difficulties.
  The New Game option doesn't actually start a new game.
  The attempt tracker is glitchy and seemingly inaccurate to the number of actual attempts.
  The number goes out of range from the game's scope

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|------------------------|
| | | | |
| | | | |
| | | | |


| Pressed New Game | Commence a new game with fresh attempts on user's preset difficulty |Changed the description a bit and reset difficulty back to Normal |Doesn't recognize or respect presets and no new functional game started |

| A number higher than the scope |"number out of scope / go lower" | "Go Higher!" | Hints the user to go higher which is inaccurate |

|Adjust difficulty |Game's scope adjust | Mixes ranges, attempts, or doesn't do anything at all | Game doesn't value difficulty presets |

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?

I used GitHub Copilot as my main AI teammate while working in VS Code. It helped me review the broken game logic, explain what the state bug likely was, and suggest a cleaner refactor for the shared utility functions.

- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).

A correct suggestion was to move the shared logic out of the streamlit app and into a dedicated module. The AI suggested that `check_guess()`, `parse_guess()`, `get_range_for_difficulty()`, and `update_score()` should live in `logic_utils.py`, with the app only handling UI and session state. I verified this by checking the project structure and running the tests: imports from `logic_utils` worked, and the logic was easier to test in isolation. The final proof was `pytest -q`, which passed after the refactor.

- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

One misleading suggestion was to keep the old return pattern from the app, where `check_guess()` returned a tuple like `("Too High", "Go HIGHER!")`. That was a poor fit because the tests expected just the outcome string, such as `"Too High"`. I verified this by looking at `tests/test_game_logic.py` and confirming the exact return contract. Once I aligned the function to the test contract, the suite passed, which showed the earlier suggestion was misleading for this project.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?

I decided a bug was fixed only after confirming the behavior in code and with a real check. For example, I verified that the comparison logic was corrected by checking the actual comparison rules in `check_guess()`, and then I ran the test suite to confirm those rules matched the expected outputs. For the Streamlit state issue, I reviewed the session-state initialization and confirmed that the secret and attempt values were only set when missing, rather than resetting on every rerun.

- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.

I ran `pytest -q` in the project root. The output showed `3 passed in 0.02s`, which confirmed that the game logic was behaving as expected for winning, too-high, and too-low cases. I also checked that the module import path was working by ensuring the project root was included in `pytest.ini`, which fixed the earlier import error during test collection.

- Did AI help you design or understand any tests? How?

Yes. The AI helped clarify the expected function contract for `check_guess()` by pointing out that the tests were authoritative and that the function should return a single outcome string. That guidance directly shaped the final implementation and made the debugging process much smoother. It also helped me reason about how to validate the parsing and comparison logic with small, targeted test checks.

---
---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.

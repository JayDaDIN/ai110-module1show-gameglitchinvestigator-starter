def get_range_for_difficulty(difficulty: str):
    """Return (low, high) inclusive range for a given difficulty."""
    #FIX: Refactored difficulty range logic into logic_utils.py using agent mode
    ranges = {
        "Easy": (1, 20),
        "Normal": (1, 100),
        "Hard": (1, 50),
    }
    return ranges.get(difficulty, (1, 100))


def parse_guess(raw: str):
    """
    Parse user input into an int guess.

    Returns: (ok: bool, guess_int: int | None, error_message: str | None)
    """
    #FIX: Hardened input parsing and validation with the AI collaborator
    if raw is None or str(raw).strip() == "":
        return False, None, "Enter a guess."

    value = str(raw).strip()

    try:
        if "." in value:
            numeric = float(value)
            if not numeric.is_integer():
                raise ValueError
            parsed = int(numeric)
        else:
            parsed = int(value)
    except (TypeError, ValueError):
        return False, None, "That is not a number."

    return True, parsed, None


def check_guess(guess, secret):
    """
    Compare guess to secret and return the outcome.

    outcome examples: "Win", "Too High", "Too Low"
    """
    #FIX: Corrected comparison logic and hint direction with human + AI collaboration
    try:
        guess_num = int(guess)
        secret_num = int(secret)
    except (TypeError, ValueError):
        if guess == secret:
            return "Win"
        return "Too High" if str(guess) > str(secret) else "Too Low"

    if guess_num == secret_num:
        return "Win"
    if guess_num > secret_num:
        return "Too High"
    return "Too Low"


def update_score(current_score: int, outcome: str, attempt_number: int):
    """Update score based on outcome and attempt number."""
    #FIX: Kept score rules in the shared logic module after AI-assisted refactor
    if outcome == "Win":
        points = 100 - 10 * (attempt_number + 1)
        if points < 10:
            points = 10
        return current_score + points

    if outcome == "Too High":
        if attempt_number % 2 == 0:
            return current_score + 5
        return current_score - 5

    if outcome == "Too Low":
        return current_score - 5

    return current_score

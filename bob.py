import re


def response(hey_bob: str) -> str:
    """Return a response based on what is said to Bob the lackadaisical teenager."""
    no_spaces = re.sub(r"[\n\t\s]*", "", hey_bob)
    bob_says = ""
    if no_spaces:
        if no_spaces.isupper() and no_spaces[-1] != '?':
            bob_says = "Whoa, chill out!"
        elif no_spaces.isupper() and no_spaces[-1] == '?':
            bob_says = "Calm down, I know what I'm doing!"
        elif no_spaces[-1] == '?':
            bob_says = "Sure."
        else:
            bob_says = "Whatever."
    else:
        bob_says = "Fine. Be that way!"

    return bob_says

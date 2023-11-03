from random import randint
from rich import print as frint


def main() -> None:
    secret, word_bank = word_load()
    r: str = ""
    i: int = 0
    m: int = len(secret)
    guesses: list[str] = []
    while secret != r:
        r = input("Guess: ")
        if r in word_bank:
            guesses.append(f" {i+1}/{m}   {compute(r, secret)}")
            for guess in guesses:
                frint(guess)
            i += 1
            if i == m:
                frint(f"The correct answer was: [green]{secret}")
                break
        else:
            frint("[red]Word does not exist")


def compute(guess: str, secret: str) -> str:
    hint: list[str] = ["", "", "", "", ""]
    copy: list[str] = list(secret)
    for i in range(len(secret)):
        if guess[i] == secret[i]:
            hint[i] = f"[green]{guess[i]}[white]"
            copy.pop(copy.index(guess[i]))
    for i in range(len(secret)):
        # print(copy)
        if guess[i] in copy:
            if hint[i] == "":
                hint[i] = f"[yellow]{guess[i]}[white]"
                copy.pop(copy.index(guess[i]))
    for i in range(len(secret)):
        if hint[i] == "":
            hint[i] = guess[i]
    return "".join(hint)


def word_load() -> tuple[str, list[str]]:
    with open("answers.txt", "r") as f:
        words = [line.replace("\n", "") for line in f]
    return words[randint(0, len(words))], words


if __name__ == '__main__':
    main()

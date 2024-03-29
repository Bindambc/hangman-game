import random
import screen


def play():
    screen.show_welcome_message()

    language = choose_language()

    words = load_words("english" if language == 1 else "portuguese")

    loose = False
    win = False
    errors = 0
    max_errors = 7

    secret_word = choose_secret_word(words)

    correct_letters = ['_' for _ in secret_word]

    print(correct_letters)

    while not loose and not win:
        guess = input("Type a letter:").strip().upper()

        if guess in secret_word:
            index = 0
            for letter in secret_word:
                if guess == letter:
                    correct_letters[index] = letter
                index += 1
        else:
            errors += 1
            screen.show_errors(errors)

        loose = errors == max_errors
        win = "_" not in correct_letters

        print(correct_letters)

    show_end_game_message(loose, win, secret_word)


def show_end_game_message(loose, win, secret_word):
    if win:
        screen.show_win_message()
    elif loose:
        screen.show_loose_message(secret_word)
    print("End of the game")


def choose_language():
    language = -1  # not valid
    while language < 1 or language > 2:
        language = int(input("Choose your language:\n(1) English\n(2) Portuguese\n"))
        if language < 1 or language > 2:
            print("Invalid option!")
    return language


def load_words(language):
    if language == "portuguese":
        w_file = open("words/portuguese.txt", "r", encoding="utf-8")
    else:
        w_file = open("words/english.txt", "r", encoding="utf-8")

    words = []

    for line in w_file:
        line = line.strip()
        words.append(line)

    w_file.close()
    return words


def choose_secret_word(words):
    return words[random.randrange(0, len(words))].upper()


if __name__ == "__main__":
    play()

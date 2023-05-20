def show_welcome_message():
    print("**************************")
    print("***Welcome to the Game!***")
    print("**************************")


def show_loose_message(secret_word):
    print("You loose! :(")
    print("The correct word was {}".format(secret_word))
    print("   _______________         ")
    print("  /               \ ")
    print(" /                 \      ")
    print("/                   \ ")
    print("|   XXXX     XXXX   |")
    print("|   XXXX     XXXX   |     ")
    print("|   XXX       XXX   |      ")
    print("|                   |      ")
    print("\__      XXX      __/     ")
    print("  |\     XXX     /|       ")
    print("  | |           | |        ")
    print("  | I I I I I I I |        ")
    print("  |  I I I I I I  |        ")
    print("  \_             _/       ")
    print("    \_         _/         ")
    print("      \_______/           ")


def show_win_message():
    print("Congratulations, you win!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")


def show_errors(erros):
    print("  _______     ")
    print(" |/      |    ")

    if erros == 1:
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if erros == 2:
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if erros == 3:
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if erros == 4:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if erros == 5:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if erros == 6:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if erros == 7:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()

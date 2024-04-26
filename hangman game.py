import random

def choose_word():
    word_list = ["atakan", "hangman", "computer", "Baum", "gold", "apfel" ,"handy",]
    return random.choice(word_list)

def display_word(word, guessed_letters):
    displayed_word = ""
    for letter in word:
        if letter in guessed_letters:
            displayed_word += letter
        else:
            displayed_word += "_"
    return displayed_word

def hangman():
    max_attempts = 10
    guessed_letters = []
    word_to_guess = choose_word()
    attempts = 0

    print("Willkommen beim Hangman-GAME!")
    print("Das zu erratende Wort hat {} Buchstaben.".format(len(word_to_guess)))

    while attempts < max_attempts:
        print("\nBisher geratene Buchstaben:", guessed_letters)
        print("Aktueller Stand:", display_word(word_to_guess, guessed_letters))

        guess = input("Rate Buchstaben Raten : ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print(" NUR 1 Buchstaben EINGEBEN .")
            continue
        elif guess in guessed_letters:
            print(" emm das wurde bereits geraten.")
            continue

        guessed_letters.append(guess)

        if guess in word_to_guess:
            print("!!!!!Richtig geraten!!!!!")
            if display_word(word_to_guess, guessed_letters) == word_to_guess:
                print("!!!!!!!!!Herzlichen Glückwunsch!!!!!!! WIN du hast das Wort '{}' erraten. du bist gut ".format(word_to_guess))
                break
        else:
            print("Falsch geraten........")
            attempts += 1
            print("Versuche übrig:", max_attempts - attempts)

    else:
        print("GAME OVER! Du Bist Tot, Das gesuchte Wort war '{}'.".format(word_to_guess))

if __name__ == "__main__":
    hangman()

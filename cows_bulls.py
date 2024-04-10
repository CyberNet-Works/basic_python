def cows_bulls(secret_number, guessed_number):

    if secret_number == guessed_number:
        you_win(secret_number)

    else:
        cows, bulls = 0, 0
        str_secret_number = str(secret_number)
        str_guessed_number = str(guessed_number)

        for digit in str_guessed_number:
            if digit in str_secret_number:
                cows += int(digit)

            else:
                bulls += int(digit)
        print(f'Cows: {cows} | Bulls: {bulls}')


def you_win(secret_number):
    print(f"You guessed it! The secret number was {secret_number}")
    quit()


def main():
    secret_number = int(input("Enter a secret number\n"))

    while True:
        guessed_number = int(input("Guess the secret number\n"))
        cows_bulls(secret_number, guessed_number)



main()

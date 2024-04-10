def cows_bulls(secret_number,guessed_number):

    #if the guess was right, game is won.
    if secret_number == guessed_number:
        you_win(secret_number)
    else:

        #initiate cows/ bulls variables & convert int to str to be iterable.
        cows, bulls = 0, 0 
        str_secret_number = str(secret_number)
        str_guessed_number = str(guessed_number)

        #sum cows/bulls digit by digit and print results.  Then reset cows/bulls.
        for digit in str_guessed_number: 
            if digit in str_secret_number:
                cows += int(digit)
            else:
                bulls += int(digit)
    print(f'Cows:{cows}  |  Bulls:{bulls}')
    cows, bulls = 0, 0




def you_win():
    print(f"You guessed it! The secret number was {secret_number}")
    quit()




def main():
    secret_number = int(input("Enter a secret number\n"))

    #loop the guessed number until its won in the cows_bulls function.
    while True:
        guessed_number = int(input("Guess the secret number\n"))

        cows_bulls(secret_number,guessed_number)



if __name__ == "__main__":

main()

secret_number, guessed_number
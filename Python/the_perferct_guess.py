import random

num = random.randint(1,100)

def based_on_lives(lives):
    while lives>0:
        guess = int(input("Enter the guess: "))
        if guess < num:
            print(f"the guessed num is lower:{guess}")

        elif guess > num:
            print(f"The guessed num is higher:{guess}")
        else:
            print(f"you have found the number:{num}")
        lives-=1
        print(f"you have {lives} lives left\n")       
    else:
        print("\nthe num is :", num)


def based_on_attempts():
    number = random.randint(1,100)
    attempt = 1
    guess = int(input("Guess the number: "))

    while(True):
        if (guess < number):
            guess = int(input("Guess another number. This one is too less: "))
            attempt +=1
        elif (guess > number):
            guess = int(input("Guess another number. This one is too big: "))
            attempt +=1
        else:
            print(f"yeahh, that's the number! You guessed it right in {attempt} attempts")
            break



based_on_attempts()
based_on_lives(5)
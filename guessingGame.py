import random

print("Number Guessing Game");

print("Guess a Number from (1-9)");

number = random.randint(1,9);
print(number);

chances =0

while(chances<5):
    guess = int(input("Enter you guess: "));

    if(guess== number):
        print("You winner!")
        break

    elif(guess<number):
        print("guess a bigger number ")

    else:
        print("guess a smaller number")

    chances=chances+1


if not chances <5 :
    print("You lost, the number was", number)

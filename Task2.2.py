#Build a Guessing Game Program
print("GUESSER GAME")
import random
num=random.randint(1,100)
attempts=0
while True:
    guess=int(input("Enter your guess "))
    attempts+=1
    if guess==num:
        print("Congrats! You have guessed the number")
        print("Number of attempts are ",attempts)
        break
    elif guess<num:
        print("Try Again!")
        print("HINT- The number is greater than the guessed number")
    else: #guess>num
        print("Try Again!")
        print("HINT- The number is smaller than the guessed number")
#Code By LCBRST#
#JUST HMOEWORK#
import random
minNumber=int(input("Please Input A Min Number:"))
maxNumber=int(input("Please Input A Max Number:"))
wantToplay=int(input("How Many Times You Want To Play?\n"))
aleadyPlay=0
tried=0
chance=5
rightNumber=random.randint(minNumber,maxNumber)
while aleadyPlay<wantToplay:
    aleadyPlay=aleadyPlay+1
    while tried<chance:
        tried=tried+1
        guessNumber=int(input("Please Input Your Answer:"))
        if guessNumber<rightNumber:
            print("Your Answer Is Less Than Right!")
            print("You Have Only",chance-tried,"Times To Try")
        elif guessNumber>rightNumber:
            print("Your Answer Is More Than Right!")
            print("You Have Only",chance-tried,"Times To Try")
        else:
            print("Bingo!")
            print("You Have Use",tried,"Times")
            break
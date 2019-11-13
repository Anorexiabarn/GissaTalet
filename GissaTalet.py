import random, time

randomNum = random.randint(1,10)
game = False
menu = False

computerScore = 0
playerScore = 0

game = 1
while game == 1:
    Guess = int(input("Guess a number between 1-10: "))
    if Guess == randomNum:
        time.sleep(1)
        exit(print("Congratz, your right :)"))
        playerScore = playerScore + 3
    
    elif Guess > randomNum:
        time.sleep(1)
        print("You guessed to high number.. Try again please.")
        computerScore = computerScore + 1
        game = 1
    
    elif Guess < randomNum:
        time.sleep(1)
        print("You guessed to low.. Try again please.")
        computerScore = computerScore + 1
        game = 1

    else:
        print("Something went wrong. Check spelling.")
        time.sleep(1)
        game = 1
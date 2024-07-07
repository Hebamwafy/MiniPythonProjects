import random
def play_guessing_game():
    attempt=0
    player_input=input("Hello friend , Do you want to guess a number? (yes/no)").lower()

    if (player_input=="no"):
        print("Ok, your score= 0")
        return
    
    elif(player_input=="yes"):
        print("Nice! Let's GO")
        pc_guess=random.randint(1,10)

    while player_input=="yes" :
        score=100-(attempt*10)
        try:
            player_guess=int(input("Guess a number between 1 to 10 : "))
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 10.")
            continue

        if (player_guess==pc_guess):
            print("GREAT! you got it")
            print("Score =",score)
            player_input=input("Do you want to guess a number again?(yes/no)").lower()
            if (player_input=="no"):
                print("Ok, your score=",score)
                break
            else:
                attempt=0
                pc_guess=random.randint(1,10) #generate a new number for next round
        else:
            attempt+=1
            print("wrong ,let's show a Hint!")
            if(player_guess<pc_guess):
                print("it's higher")
            else:
                print("it's lower")

if __name__ == "__main__":
    play_guessing_game()

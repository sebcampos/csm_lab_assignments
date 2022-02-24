import random

my_number = 1
player_number = 0;
playAgain = "Y"
try_count = 4


while (playAgain != "N"):
    if(playAgain == "Y"):
        my_number = random.randrange(101)
        try_count = 4
        print("I am thinking of a number between 1 and 100.")
        player_number = int(input("Guess what it is. You have 5 tries: "))
        for i in range(4):
            if(player_number == my_number):
                print("You got it!")
                break;
            elif(player_number > my_number):
                player_number = int(input("Nope! Too high. Try again({} try left): ".format(try_count)))
                try_count = try_count - 1
            else:
                player_number = int(input("Nope! Too low. Try again({} try left): ".format(try_count)))
                try_count = try_count - 1
        if(player_number != my_number):
            print("Nope! You lost. The number was {}".format(my_number))
        playAgain = input("Do you want to play again? (Y/N): ")
    else:
        playAgain = input("Do you want to play again? (Y/N): ")

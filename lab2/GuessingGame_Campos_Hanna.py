import random

my_number = 1
player_number = 0;
play_again = "Y"
try_count = 4
score = 0


def check_input(user_input: str) -> str:
    """
    Please enter correct input
    :param str user_input: input from user
    :return: str correct input
    """
    while user_input.isnumeric() != True and user_input.lower() not in ["y", "n"]:
        user_input = input("Please enter correct input")
    return user_input


while play_again != "N":
    if play_again == "Y":
        my_number = random.randrange(1, 101)
        try_count = 4
        print("I am thinking of a number between 1 and 100.")
        player_number = int(check_input(input("Guess what it is. You have 5 tries: ")))
        for i in range(4):
            if player_number == my_number:
                print("You got it!")
                break
            elif player_number > my_number:
                player_number = int(check_input(input("Nope! Too high. Try again({} try left): ".format(try_count))))
                try_count = try_count - 1
            else:
                player_number = int(check_input(input("Nope! Too low. Try again({} try left): ".format(try_count))))
                try_count = try_count - 1
        if player_number != my_number:
            print("Nope! You lost. The number was {}".format(my_number))
        play_again = input("Do you want to play again? (Y/N): ")
    else:
        play_again = input("Do you want to play again? (Y/N): ")

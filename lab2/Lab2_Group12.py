import random
import datetime

welcome_message = """
 __      __   _                    _ 
 \ \    / /__| |__ ___ _ __  ___  | |
  \ \/\/ / -_) / _/ _ \ '  \/ -_) |_|
   \_/\_/\___|_\__\___/_|_|_\___| (_)
                                     
"""

you_win = """
 __   __                 _        ___    _ 
 \ \ / /__ _  _  __ __ _(_)_ _   (_) \  | |
  \ V / _ \ || | \ V  V / | ' \   _ | | |_|
   |_|\___/\_,_|  \_/\_/|_|_||_| (_)| | (_)
                                   /_/    
"""
you_lose = """
 __   __          _               _  __  _ 
 \ \ / /__ _  _  | |___ ___ ___  (_)/ / | |
  \ V / _ \ || | | / _ (_-</ -_)  _| |  |_|
   |_|\___/\_,_| |_\___/__/\___| (_) |  (_)
                                    \_\    
"""

goodbye = """
   ___              _ _               ___  __  
  / __|___  ___  __| | |__ _  _ ___  ( _ ) \ \ 
 | (_ / _ \/ _ \/ _` | '_ \ || / -_) / _ \  | |
  \___\___/\___/\__,_|_.__/\_, \___| \___/  | |
                           |__/            /_/
"""

"""Static functions"""


# todo Jacob Hanna function to get a guessing_range


# todo Jacob Hanna function to check guessing_range


def log(message: str) -> None:
    """
    This method logs errors created by the clean_inputs method
    :param message: message to be logged into file `errors.log`
    :return: None
    """
    with open("errors.log", "a") as f:
        f.write(f"{datetime.datetime.now()}:\n" + message + "\n")


def clean_inputs(game_user_input: str) -> bool:
    """
    This method checks to ensure that the user input can be converted into a number
    :param str game_user_input:
    :return: boolean based on whether or not the string can be converted into an integer
    """
    try:
        int(game_user_input)
        return True
    except Exception as e:
        log(str(e))
        print("Input was not able to be converted to integer")
        return False


def try_again(game_user_input: str) -> bool:
    """
    This method takes the user input `y` or `n` to check if they would like to play another round
    if so the Lab2 class restart method is invoked
    :param str game_user_input: value of `y` of `n`
    :return: boolean
    """
    if game_user_input == "y":
        return True
    elif game_user_input == "n":
        print("Thank you for playing!")
        return False


class Lab2:
    def __init__(self, guessing_range: list) -> None:
        """
        Constructor method for Lab2 Class
        :param list guessing_range: a list of 2 integers to be used as a range for creating secret number
        :return: Lab2
        :rtype: Lab2
        Attributes:
            guessing_range   The range to create the secret number from
            num_guesses      The current users attempts to guess secret number
            max_guesses      The max number for guesses
            game_over        boolean defining state of game
            game_running     boolean defining state of game loop
            score            Integer reflecting current users score
            secret_number    Integer defined by the random library given the guessing_range
            try_again_options List of allowed responses to the try_again method
        """
        self.guessing_range = guessing_range
        self.num_guesses = 0
        self.max_guesses = 5
        self.game_over = False
        self.game_running = True
        self.score = 0
        self.secret_number = random.randint(guessing_range[0], guessing_range[1])
        self.try_again_options = ["y", "n"]

    def log_score(self, name: str) -> None:
        """
        This method logs the score of the user to the file gamescores
        :param str name: user defined name
        :return: None
        """
        with open("gamescores", "a") as f:
            f.write(f"\n{name} {self.score}\n")

    def compare_value(self, value: int) -> bool:
        """
        This method compares the users input guess to check if it matches the secret number
        if so it returns true else false
        :param int value: the current users guess for the secret number
        :return: boolean
        """
        if value == self.secret_number:
            self.score += 1
            return True
        elif value > self.secret_number:
            self.num_guesses += 1
            print(f"Nope! Too high. Try again ({self.max_guesses - self.num_guesses} tries left)")
            return False
        elif value < self.secret_number:
            self.num_guesses += 1
            print(f"Nope! Too low. Try again ({self.max_guesses - self.num_guesses} tries left)")
            return False

    def restart(self) -> None:
        """
        This method resets the number of guesses for the current user and the value for secret number
        while maintaining the user score if they chose to play again
        :return:
        """
        self.num_guesses = 0
        self.game_over = False
        self.secret_number = random.randint(self.guessing_range[0], self.guessing_range[1])


if __name__ == "__main__":
    print(welcome_message)  # welcome the user

    # todo Jacob Hanna collect desired_range
    # todo Jacob Hanna check that desired_range is acceptable
    # todo Jacob Hanna while desired range is not acceptable ask for input again

    desired_range = [1, 40]  # todo Jacob Hanna replace with user defined range 
    game = Lab2(desired_range)  # instance of the Lab2 class
    while game.game_running:  # main game loop
        if game.game_over:  # if game is set to game over player has one
            print(you_win)
            # loop to check if user wants to play again
            user_input = input(f"Game Over you win!\nScore: {game.score}\nPlay again?(Y/N)\n")
            while user_input.lower() not in game.try_again_options:
                user_input = input(f"Input must be Y or N, Play again?(Y/N)\n")
            if user_input.lower() == "y":
                game.restart()
            elif user_input.lower() == "n":
                print(f"Thanks for playing!\nScore: {game.score}")
                game.game_running = False
                break
        if game.max_guesses == game.num_guesses:  # user has reached max amount of tried and lost
            print(you_lose)
            print(f"Lucky number was: {game.secret_number}\nScore: {game.score}")
            # loop to check if user wants to play again
            user_input = input("Game over, max guesses reached, Play again?(Y/N):\n")
            while user_input.lower() not in game.try_again_options:
                user_input = input("Game over, max guesses reached, Play again?(Y/N)\n")
            if user_input.lower() == "y":
                game.restart()
            elif user_input.lower() == "n":
                print(f"Thanks for playing!\nScore: {game.score}")
                game.game_running = False
                break
        user_input = input("Please enter a number:\n") # take user guess at secret number
        while not clean_inputs(user_input): # while user input can not be converted to int keep asking
            user_input = input("Please enter an integer:\n")
        user_integer = int(user_input)
        if game.compare_value(user_integer): # compare user input to secret number
            game.game_over = True

    game.log_score(f"{datetime.datetime.now()} {input('Enter name: ')}") # log users score
    print(goodbye) # goodbye !

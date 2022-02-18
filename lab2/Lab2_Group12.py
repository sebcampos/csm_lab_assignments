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


#function to get a guessing_range



#function to check guessing_range





class Lab2:
	def __init__(self, guessing_range: list) -> None:
		self.guessing_range = guessing_range
		self.num_guesses = 0
		self.max_guesses = 5
		self.game_over = False
		self.game_running = True
		self.score = 0
		self.secret_number = random.randint(guessing_range[0], guessing_range[1])
		self.try_again_options = ["y", "n"]		

	def log(self, message: str) -> None:
		with open("errors.log", "a") as f:
			f.write(f"{datetime.datetime.now()}:\n"+message+"\n")

			
	def log_score(self, name):
		with open("gamescores", "a") as f:
			f.write(f"\n{name} {self.score}\n")
	def clean_inputs(self, user_input: str) -> bool:
		try:
			int(user_input)
			return True
		except Exception as e:
			self.log(str(e))
			print("Input was not able to be converted to integer")
			return False

	def compare_value(self, value: int) -> bool:
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
	def try_again(self, user_input):
		if user_input == "y":
			return True
		elif user_input == "n":
			print("Thank you for playing!")
			return False
	
	def restart(self):
		self.num_guesses = 0
		self.game_over = False
		self.secret_number = random.randint(self.guessing_range[0], self.guessing_range[1])
		



if __name__ == "__main__":
	print(welcome_message)
	
	#collect desired_range
	#check that desired_range is acceptable
	#while desired range is not acceptable ask for input again
	
	desired_range = [1, 40]
	game = Lab2(desired_range)
	while game.game_running:
		if game.game_over == True:
			print(you_win)
			user_input = input(f"Game Over you win!\nScore: {game.score}\nPlay again?(Y/N)\n")
			while user_input.lower() not in game.try_again_options:
				user_input = input(f"Input must be Y or N, Play again?(Y/N)\n")
			if user_input.lower() == "y":
				game.restart()
			elif user_input.lower() == "n":
				print(f"Thanks for playing!\nScore: {game.score}")
				game.game_running = False
				break
		if game.max_guesses == game.num_guesses:
			print(you_lose)
			print(f"Lucky number was: {game.secret_number}\nScore: {game.score}")
			user_input = input("Game over, max guesses reached, Play again?(Y/N):\n")
			while user_input.lower() not in game.try_again_options:
				user_input = input("Game over, max guesses reached, Play again?(Y/N)\n")
			if user_input.lower() == "y":
				game.restart()
			elif user_input.lower() == "n":
				print(f"Thanks for playing!\nScore: {game.score}")
				game.game_running = False
				break
		user_input = input("Please enter a number:\n")
		while game.clean_inputs(user_input) != True:
			user_input = input("Please enter an integer:\n")
		user_integer = int(user_input)
		if game.compare_value(user_integer):
			game.game_over = True
	
	game.log_score(f"{datetime.datetime.now()} {input('Enter name: ')}")
	print(goodbye)

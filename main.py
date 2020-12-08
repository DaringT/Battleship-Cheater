import json
from raw_to_json import BSD
from pprint import pprint
import os

class Battleship():
	a_to_j = ("a", "b", "c", "d", "e", "g", "h", "i", "j")
	rows = 10

	def __init__(self, battleship_grid=None):
		"""
		A Battleship grid is created
		:param battleship_grid:
		"""
		self.battleship_grid = battleship_grid
		if self.battleship_grid is None:
			self.battleship_grid = {}
			for letter in Battleship.a_to_j:
				self.battleship_grid[letter] = [0] * Battleship.rows

	def add_ships(self, coordinates, ship_type):
		"""
			add ships to the Battleship grid from one function
			:rtype: object
		"""
		self.letter, self.number, self.direction = coordinates

		self.letter = self.letter[0].lower()
		self.direction = self.direction[0].lower()

		# print(f"letter: {self.letter} number:{self.number} direction:{self.direction} ship type: {ship_type}")
		self.number = int(self.number)-1
		print(self.letter)
		try:
			self.letters_index = Battleship.a_to_j.index(self.letter)
		except ValueError:
			return self.battleship_grid

		if ship_type=="p":
			return self._patrol_boat()

		elif ship_type=="s":
			return self._add_submairie()

		elif ship_type=="d":
			return self._add_destroyer()

		elif ship_type=="b":
			return self._add_battleship()

		elif ship_type=="c":
			return self._add_aircraft_carrier()

	def _patrol_boat(self):

		"""
			Adds a patrol boat as int 1 in BS grid
			:return: battleship_grid
			"""
		try:
			if self.direction=="s":
				self.battleship_grid[Battleship.a_to_j[self.letters_index+1]][self.number] = 1
				self.battleship_grid[self.letter][self.number] = 1
				return self.battleship_grid

			elif self.direction=="n":
				self.battleship_grid[Battleship.a_to_j[self.letters_index-1]][self.number] = 1
				self.battleship_grid[self.letter][self.number] = 1
				return self.battleship_grid

			elif self.direction=="e":
				self.battleship_grid[self.letter][self.number+1] = 1
				self.battleship_grid[self.letter][self.number] = 1
				return self.battleship_grid
			elif self.direction=="w":
				self.battleship_grid[self.letter][self.number-1] = 1
				self.battleship_grid[self.letter][self.number] = 1
				return self.battleship_grid
		except IndexError:
			print("You cann't add a patrol boat there.")
			self.battleship_grid

	def _add_submairie(self):
		"""
			Adds a submairie as int 2 in BS grid
			:return: battleship_grid
			"""
		try:
			if self.direction=="s":
				# This is what happens you go South
				self.battleship_grid[Battleship.a_to_j[self.letters_index+1]][self.number] = 2
				self.battleship_grid[Battleship.a_to_j[self.letters_index+2]][self.number] = 2
				self.battleship_grid[self.letter][self.number] = 2
				return self.battleship_grid

			elif self.direction=="n":
				# This is what happens you go North
				self.battleship_grid[Battleship.a_to_j[self.letters_index-1]][self.number] = 2
				self.battleship_grid[Battleship.a_to_j[self.letters_index-2]][self.number] = 2
				self.battleship_grid[self.letter][self.number] = 2
				return self.battleship_grid

			elif self.direction=="e":
				# This is what happens you go East
				self.battleship_grid[self.letter][self.number+1] = 2
				self.battleship_grid[self.letter][self.number+2] = 2
				self.battleship_grid[self.letter][self.number] = 2
				return self.battleship_grid

			elif self.direction=="w":
				# This is what happens you go West
				self.battleship_grid[self.letter][self.number-1] = 2
				self.battleship_grid[self.letter][self.number-2] = 2
				self.battleship_grid[self.letter][self.number] = 2
				return self.battleship_grid
		except IndexError:
			print("You cann't add a Submairie there.")
			self.battleship_grid

	def _add_destroyer(self):
		"""
			Adds a destroyer as int 3 in BS grid
			:return: battleship_grid
			"""
		try:
			if self.direction=="s":
				self.battleship_grid[Battleship.a_to_j[self.letters_index+2]][self.number] = 3
				self.battleship_grid[Battleship.a_to_j[self.letters_index+1]][self.number] = 3
				self.battleship_grid[self.letter][self.number] = 3
				return self.battleship_grid
			elif self.direction=="n":
				self.battleship_grid[Battleship.a_to_j[self.letters_index-2]][self.number] = 3
				self.battleship_grid[Battleship.a_to_j[self.letters_index-1]][self.number] = 3
				self.battleship_grid[self.letter][self.number] = 3
				return self.battleship_grid
			elif self.direction=="w":
				self.battleship_grid[self.letter][self.number-2] = 3
				self.battleship_grid[self.letter][self.number-1] = 3
				self.battleship_grid[self.letter][self.number] = 3
				return self.battleship_grid

			elif self.direction=="e":
				self.battleship_grid[self.letter][self.number+2] = 3
				self.battleship_grid[self.letter][self.number+1] = 3
				self.battleship_grid[self.letter][self.number] = 3
				return self.battleship_grid
		except IndexError:
			print("You can not add a Destroyer there!")
			return self.battleship_grid

	def _add_battleship(self):
		"""
			Adds a Battleship as int 4 in BS grid
			:return: battleship_grid
			"""
		try:
			if self.direction=="n":
				self.battleship_grid[Battleship.a_to_j[self.letters_index-1]][self.number] = 4
				self.battleship_grid[Battleship.a_to_j[self.letters_index-2]][self.number] = 4
				self.battleship_grid[Battleship.a_to_j[self.letters_index-3]][self.number] = 4
				self.battleship_grid[self.letter][self.number] = 4
				return self.battleship_grid

			if self.direction=="s":
				self.battleship_grid[Battleship.a_to_j[self.letters_index+1]][self.number] = 4
				self.battleship_grid[Battleship.a_to_j[self.letters_index+2]][self.number] = 4
				self.battleship_grid[Battleship.a_to_j[self.letters_index+3]][self.number] = 4
				self.battleship_grid[self.letter][self.number] = 4
				return self.battleship_grid

			elif self.direction=="e":
				self.battleship_grid[self.letter][self.number+1] = 4
				self.battleship_grid[self.letter][self.number+2] = 4
				self.battleship_grid[self.letter][self.number+3] = 4
				self.battleship_grid[self.letter][self.number] = 4
				return self.battleship_grid

			elif self.direction=="w":
				self.battleship_grid[self.letter][self.number-1] = 4
				self.battleship_grid[self.letter][self.number-2] = 4
				self.battleship_grid[self.letter][self.number-3] = 4
				self.battleship_grid[self.letter][self.number] = 4
		except IndexError:
			print("You can not add a Battleship there!")
			return self.battleship_grid

	def _add_aircraft_carrier(self):
		"""
			Adds a aircraft carrier as int 5 in BS grid
			:return: battleship_grid
			"""
		try:
			if self.direction=="n":
				self.battleship_grid[Battleship.a_to_j[self.letters_index-1]][self.number] = 5
				self.battleship_grid[Battleship.a_to_j[self.letters_index-2]][self.number] = 5
				self.battleship_grid[Battleship.a_to_j[self.letters_index-3]][self.number] = 5
				self.battleship_grid[Battleship.a_to_j[self.letters_index-4]][self.number] = 5
				self.battleship_grid[self.letter][self.number] = 5
				return self.battleship_grid

			elif self.direction=="s":
				self.battleship_grid[Battleship.a_to_j[self.letters_index+1]][self.number] = 5
				self.battleship_grid[Battleship.a_to_j[self.letters_index+2]][self.number] = 5
				self.battleship_grid[Battleship.a_to_j[self.letters_index+3]][self.number] = 5
				self.battleship_grid[Battleship.a_to_j[self.letters_index+4]][self.number] = 5
				self.battleship_grid[self.letter][self.number] = 5
				return self.battleship_grid

			elif self.direction=="e":
				self.battleship_grid[self.letter][self.number+1] = 5
				self.battleship_grid[self.letter][self.number+2] = 5
				self.battleship_grid[self.letter][self.number+3] = 5
				self.battleship_grid[self.letter][self.number+4] = 5
				self.battleship_grid[self.letter][self.number] = 5
				return self.battleship_grid

			elif self.direction=="w":
				self.battleship_grid[self.letter][self.number-1] = 5
				self.battleship_grid[self.letter][self.number-2] = 5
				self.battleship_grid[self.letter][self.number-3] = 5
				self.battleship_grid[self.letter][self.number-4] = 5
				self.battleship_grid[self.letter][self.number] = 5
		except IndexError:
			print("You can not add a aircraft carrier there!")
			return self.battleship_grid


	def input_game(self) -> object:
		'''adds ships to the Battleship board'''
		b1 = Battleship()
		while True:
			ship_type = input("input Ship Type --> ")
			if ship_type=="exit":
				exit()
			else:
				letter = input("Add Letter --> ")
				number = input("Add Number --> ")
				direction = input("Add Direction   --> ")
				if direction in {int, float}:
					print("The Direction is not a number")
					direction = input("Add Direction   --> ")

				print(f"letter: {letter}\tnumber:{number}\tdirection: {direction}\tinput: {ship_type}")
			out_to_file = input("Output to file? --> ")
			if out_to_file=="y":
				print("outputing to file...")
				b1.output_board_layout()
				b1 = Battleship()
			elif out_to_file=="n":
				b1.add_ships(coordinates=(letter, number, direction), ship_type=ship_type)

	def display_total_ship_heat_grid(self):
		# subclass for displaying if a spot is mostly likely a ship into a (heat map)
		pass

	def make_heat_graft(input_grid):
		print("importing seaborn...")
		import seaborn as sb
		print("seaborn is imported")
		from matplotlib import pyplot as plt

		# test_array = np.array([[1, 2], [3, 4]])
		# hm = sb.heatmap(input_grid)
		sb.heatmap(input_grid,
				   cmap='Blues',
				   annot=True,
				   yticklabels=[letter.upper() for letter in Battleship.a_to_j],
				   xticklabels=[num for num in range(1, 11)])

		plt.yticks(rotation=0)
		plt.tick_params(
				which='both',
				bottom=False,
				left=False,
				labelbottom=False,
				labeltop=True)
		plt.tight_layout()

		plt.show()

	def display_specific_ship_heat_grid(self):
		# subclass for displaying for wich ship is most likely to be where in a (Heat map)
		pass

	def display_total_ship_heat_grid(self):
		'''subclass for displaying for wich ship is most likely to be where in a (Heat map)'''
		pass

	@classmethod
	def from_grid_directions(cls, dir_dict):
		"""Generates an instance from a direction data"""
		b1 = Battleship()
		for key in dir_dict.keys():
			print(f"Grid_name: {key}")
			for ship_type, coordinates in dir_dict[key].items():
				print(f"ship type: {ship_type}  letter: {coordinates[0]}  Number: {coordinates[1]}  direction: {coordinates[2]}")
				b1.add_ships(coordinates=coordinates, ship_type=ship_type)
		return cls(b1.battleship_grid)

	def grid_directions_to_bs_grid(self, dir_dict):
		"""Generates an instance from a direction data"""

		# for key in dir_dict.keys():
		print(f"Grid_name: {key}")
		for ship_type, coordinates in dir_dict.items():
			self.add_ships(coordinates=coordinates, ship_type=ship_type)
		return self.battleship_grid





	def output_board_layout(self, input_file="Battleship.json", add_to_key="_in_book"):
		"""
		:parameter
			output_file
				outputs json_data to file
				default is Battleship.json
		:return: dict formatted to json
		"""
		from datetime import datetime
		dt = datetime.today()
		key = f"{str(dt.month)}-{str(dt.day)}-{str(dt.year)[2:]}_{str(dt.hour)}:{str(dt.minute)}.{str(dt.second)}"
		key = key+add_to_key

		new_battleship_grid = dict()
		new_battleship_grid[key] = self.battleship_grid

		if os.stat(input_file).st_size!=0:
			print(os.stat(input_file).st_size)
			print("file Not Empty")
			with open(input_file) as f:
				existing_json_data = json.load(f)

			existing_json_data.update(new_battleship_grid)
			print("\n" * 3)
			pprint.pprint(existing_json_data)

			json_file_data = json.dumps(existing_json_data)
		else:
			json_file_data = json.dumps(new_battleship_grid)

		with open(input_file, "w") as f:
			# json.dump(json_file_+data, f)
			f.write(json_file_data)
		return json_file_data


if __name__ == '__main__':
	ts={"a1":{"p": ["a","1","e"],
			  "s": ["b","4","e"],
			  "d": ["i","2","e"],
			  "b": ["e","5","e"],
			  "c": ["g","4","e"]}}

	# b1 = Battleship.from_grid_directions(ts)
	#

def output_all_grids()
	book_dirs = BSD(input_file="book_direction.txt")
	book_dir_dict = book_dirs.raw_data_to_dict()
	for key in book_dir_dict:
		b1 = Battleship()
		print(key)
		# pprint(book_dir_dict[key])
		b1.grid_directions_to_bs_grid(book_dir_dict[key])
		pprint(b1.battleship_grid)
		print("-"*40,"\n")

	# b1.Battleship.DisplayGrid.make_heat_graft()
	# Battleship.GridGeneration.from_grid_directions(dir_dict=ts)
	# B4 = Battleship.GridGeneration.from_grid_directions(ts)

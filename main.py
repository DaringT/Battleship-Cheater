import json
from raw_to_json import BSD
from pprint import pprint
import os

print("importing seaborn...")
import seaborn as sb

print("seaborn is imported")
from matplotlib import pyplot as plt


class Battleship:
	a_to_j = ("a", "b", "c", "d", "e", "f", "g", "h", "i", "j")
	ship_type_dict = {"p": 1, "s": 2, "d": 3, "b": 4, "c": 5}
	ship_abbreviations = {"p":"patrol boat",
	                      "s":"submarine",
	                      "d":"destroyer",
	                      "b":"battleship",
	                      "c":"aircraft carrier"}
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

	def __add__(self, other):
		for letter in self.battleship_grid.keys():
			for index in range(len(self.battleship_grid[letter])):
				self.battleship_grid[letter][index] = other.battleship_grid[letter][index]+self.battleship_grid[letter][
					index]
		return Battleship(self.battleship_grid)

	class Add_Ships:
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
			try:
				self.letters_index = Battleship.a_to_j.index(self.letter)
			except ValueError:
				return self.battleship_grid

			if ship_type == "p":
				return Battleship.Add_Ships._patrol_boat(self)

			elif ship_type == "s":
				return Battleship.Add_Ships._add_submarine(self)

			elif ship_type == "d":
				return Battleship.Add_Ships._add_destroyer(self)

			elif ship_type == "b":
				return Battleship.Add_Ships._add_battleship(self)

			elif ship_type == "c":
				return Battleship.Add_Ships._add_aircraft_carrier(self)

		def _patrol_boat(self):

			"""
				Adds a patrol boat as int 1 in BS grid
				:return: battleship_grid
				"""
			try:
				if self.direction == "s":
					self.battleship_grid[Battleship.a_to_j[self.letters_index+1]][self.number] = 1
					self.battleship_grid[self.letter][self.number] = 1
					return self.battleship_grid

				elif self.direction == "n":
					self.battleship_grid[Battleship.a_to_j[self.letters_index-1]][self.number] = 1
					self.battleship_grid[self.letter][self.number] = 1
					return self.battleship_grid

				elif self.direction == "e":
					self.battleship_grid[self.letter][self.number+1] = 1
					self.battleship_grid[self.letter][self.number] = 1
					return self.battleship_grid
				elif self.direction == "w":
					self.battleship_grid[self.letter][self.number-1] = 1
					self.battleship_grid[self.letter][self.number] = 1
					return self.battleship_grid
			except IndexError as e:
				print(e)
				print("\nYou cannot add a patrol boat there.")

		def _add_submarine(self):
			"""
				Adds a submarine as int 2 in BS grid
				:return: battleship_grid
				"""
			try:
				if self.direction == "s":
					# This is what happens you go South
					self.battleship_grid[Battleship.a_to_j[self.letters_index+1]][self.number] = 2
					self.battleship_grid[Battleship.a_to_j[self.letters_index+2]][self.number] = 2
					self.battleship_grid[self.letter][self.number] = 2
					return self.battleship_grid

				elif self.direction == "n":
					# This is what happens you go North
					self.battleship_grid[Battleship.a_to_j[self.letters_index-1]][self.number] = 2
					self.battleship_grid[Battleship.a_to_j[self.letters_index-2]][self.number] = 2
					self.battleship_grid[self.letter][self.number] = 2
					return self.battleship_grid

				elif self.direction == "e":
					# This is what happens you go East
					self.battleship_grid[self.letter][self.number+1] = 2
					self.battleship_grid[self.letter][self.number+2] = 2
					self.battleship_grid[self.letter][self.number] = 2
					return self.battleship_grid

				elif self.direction == "w":
					# This is what happens you go West
					self.battleship_grid[self.letter][self.number-1] = 2
					self.battleship_grid[self.letter][self.number-2] = 2
					self.battleship_grid[self.letter][self.number] = 2
					return self.battleship_grid
			except IndexError as e:
				print(e)
				print("You can't add a submarine there.")

		def _add_destroyer(self):
			"""
				Adds a destroyer as int 3 in BS grid
				:return: battleship_grid
				"""
			try:
				if self.direction == "s":
					self.battleship_grid[Battleship.a_to_j[self.letters_index+2]][self.number] = 3
					self.battleship_grid[Battleship.a_to_j[self.letters_index+1]][self.number] = 3
					self.battleship_grid[self.letter][self.number] = 3
					return self.battleship_grid
				elif self.direction == "n":
					self.battleship_grid[Battleship.a_to_j[self.letters_index-2]][self.number] = 3
					self.battleship_grid[Battleship.a_to_j[self.letters_index-1]][self.number] = 3
					self.battleship_grid[self.letter][self.number] = 3
					return self.battleship_grid
				elif self.direction == "w":
					self.battleship_grid[self.letter][self.number-2] = 3
					self.battleship_grid[self.letter][self.number-1] = 3
					self.battleship_grid[self.letter][self.number] = 3
					return self.battleship_grid

				elif self.direction == "e":
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
				if self.direction == "n":
					self.battleship_grid[Battleship.a_to_j[self.letters_index-1]][self.number] = 4
					self.battleship_grid[Battleship.a_to_j[self.letters_index-2]][self.number] = 4
					self.battleship_grid[Battleship.a_to_j[self.letters_index-3]][self.number] = 4
					self.battleship_grid[self.letter][self.number] = 4
					return self.battleship_grid

				if self.direction == "s":
					self.battleship_grid[Battleship.a_to_j[self.letters_index+1]][self.number] = 4
					self.battleship_grid[Battleship.a_to_j[self.letters_index+2]][self.number] = 4
					self.battleship_grid[Battleship.a_to_j[self.letters_index+3]][self.number] = 4
					self.battleship_grid[self.letter][self.number] = 4
					return self.battleship_grid

				elif self.direction == "e":
					self.battleship_grid[self.letter][self.number+1] = 4
					self.battleship_grid[self.letter][self.number+2] = 4
					self.battleship_grid[self.letter][self.number+3] = 4
					self.battleship_grid[self.letter][self.number] = 4
					return self.battleship_grid

				elif self.direction == "w":
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
				if self.direction == "n":
					self.battleship_grid[Battleship.a_to_j[self.letters_index-1]][self.number] = 5
					self.battleship_grid[Battleship.a_to_j[self.letters_index-2]][self.number] = 5
					self.battleship_grid[Battleship.a_to_j[self.letters_index-3]][self.number] = 5
					self.battleship_grid[Battleship.a_to_j[self.letters_index-4]][self.number] = 5
					self.battleship_grid[self.letter][self.number] = 5
					return self.battleship_grid

				elif self.direction == "s":
					self.battleship_grid[Battleship.a_to_j[self.letters_index+1]][self.number] = 5
					self.battleship_grid[Battleship.a_to_j[self.letters_index+2]][self.number] = 5
					self.battleship_grid[Battleship.a_to_j[self.letters_index+3]][self.number] = 5
					self.battleship_grid[Battleship.a_to_j[self.letters_index+4]][self.number] = 5
					self.battleship_grid[self.letter][self.number] = 5
					return self.battleship_grid

				elif self.direction == "e":
					self.battleship_grid[self.letter][self.number+1] = 5
					self.battleship_grid[self.letter][self.number+2] = 5
					self.battleship_grid[self.letter][self.number+3] = 5
					self.battleship_grid[self.letter][self.number+4] = 5
					self.battleship_grid[self.letter][self.number] = 5
					return self.battleship_grid

				elif self.direction == "w":
					self.battleship_grid[self.letter][self.number-1] = 5
					self.battleship_grid[self.letter][self.number-2] = 5
					self.battleship_grid[self.letter][self.number-3] = 5
					self.battleship_grid[self.letter][self.number-4] = 5
					self.battleship_grid[self.letter][self.number] = 5
			except IndexError:
				print("You can not add a aircraft carrier there!")
				return self.battleship_grid

	def input_game(self):
		'''adds ships to the Battleship board'''
		b1 = Battleship()
		while True:
			ship_type = input("input Ship Type --> ")
			if ship_type == "exit":
				return
			else:
				letter = input("Add Letter --> ")
				number = input("Add Number --> ")
				direction = input("Add Direction   --> ")

				print(f"letter: {letter}\tnumber:{number}\tdirection: {direction}\tinput: {ship_type}")
			out_to_file = input("Output to file? --> ")
			if out_to_file == "y":
				print("Outputting to file...")
				b1.output_battleship_grid_to_json_file()
				b1 = Battleship()
			elif out_to_file == "n":
				b1.Add_Ships.add_ships(self,coordinates=(letter, number, direction), ship_type=ship_type)

	@classmethod
	def from_grid_directions(cls, dir_dict) -> object:
		"""Generates an instance from a direction data
		:param dir_dict:
		:type dict:
		:return self.battleship_grid:
		:rtype dict:
		"""
		b1 = Battleship()
		for key in dir_dict.keys():
			# print(f"Grid_name: {key}")
			for ship_type, coordinates in dir_dict[key].items():
				# print(f"ship type: {ship_type}  letter: {coordinates[0]}  Number: {coordinates[1]}  direction: {coordinates[2]}")
				b1.Add_Ships.add_ships(coordinates=coordinates, ship_type=ship_type)
		return cls(b1.battleship_grid)

	def grid_directions_to_bs_grid(self, dir_dict):
		"""Converts grid  directions to battleship grid
		:param dir_dict:
		:type dict:
		:return self.battleship_grid:
		:rtype dict:
		"""
		for ship_type, coordinates in dir_dict.items():
			Battleship.Add_Ships.add_ships(self, coordinates=coordinates, ship_type=ship_type)
		return self.battleship_grid

	@staticmethod
	def battleship_dict_to_heatmap_data(battleship_grid):
		"""
		Converts a battleship_dict to nested tuple for generating a heatmap
		:param battleship_grid:
		:type dict:
		:return: heatmap_data
		:rtype: tuple
		"""
		heatmap_data = []
		for grid_list in battleship_grid.values():
			heatmap_data.append(tuple(grid_list))
		return tuple(heatmap_data)

	def output_battleship_grid_to_json_file(self, input_file="Battleship.json", add_to_key="_in_book"):
		"""
		Outputs the battleship_grid to a json_file
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
			with open(input_file, "r") as f:
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


class DisplayGrid:
	"""Class for displaying battleship grids"""

	@staticmethod
	def display_specific_ship_heat_grid(ship_type, input_file="book_direction.txt"):
		'''displaying witch ship is most likely to be where in a (Heat map)
		:type input_file: str
		:rtype: tuple
		:return: heatmap data
		'''
		book_dirs = BSD(input_file)
		book_dir_dicts = book_dirs.raw_data_to_dict()
		b2 = Battleship()
		output_bs_grid = Battleship()

		for book_dir_dict in book_dir_dicts.values():
			b2.grid_directions_to_bs_grid(book_dir_dict)
			bs_dict = b2.battleship_grid

			for letter in bs_dict.keys():
				for num in range(len(bs_dict[letter])):
					if bs_dict[letter][num] == Battleship.ship_type_dict[ship_type]:
						bs_dict[letter][num] = 1
					else:
						bs_dict[letter][num] = 0

			output_bs_grid = b2+output_bs_grid
			b2 = Battleship()
		return Battleship.battleship_dict_to_heatmap_data(output_bs_grid.battleship_grid)

	@staticmethod
	def display_total_ship_heat_grid(input_file="book_direction.txt"):
		'''displaying where ships most likely to be
		:type input_file: str
		:return: heatmap data
		'''
		book_dirs = BSD(input_file)
		book_dir_dicts = book_dirs.raw_data_to_dict()
		b2 = Battleship()
		output_bs_grid = Battleship()

		for book_dir_dict in book_dir_dicts.values():
			b2.grid_directions_to_bs_grid(book_dir_dict)
			bs_dict = b2.battleship_grid

			for letter in bs_dict.keys():
				for num in range(len(bs_dict[letter])):
					if bool(bs_dict[letter][num]):
						bs_dict[letter][num] = 1

			output_bs_grid = b2+output_bs_grid
			b2 = Battleship()
		return Battleship.battleship_dict_to_heatmap_data(output_bs_grid.battleship_grid)

	@staticmethod
	def make_heat_graft(input_grid, output_file="Auto", map_color="blue", dark_to_light=True, input_title="title"):
		'''Make a heatmap

		:param input_grid: heatmap grid
		:type input_grid:
		:param output_file:
		:type output_file:
		:param map_color:
		:type map_color:
		:param dark_to_light:
		:type dark_to_light:
		'''

		if map_color == "blue":
			if dark_to_light:
				map_color = "Blues"
			else:
				map_color = "Blues_r"
		elif map_color == "red":
			if dark_to_light:
				map_color = "rocket_r"
			else:
				map_color = "rocket"

		sb.heatmap(input_grid,
		           annot=True,
		           yticklabels=[letter.upper() for letter in Battleship.a_to_j],
		           xticklabels=[num for num in range(1, 11)],
		           cmap=map_color,
		           # linewidth=1,
		           linecolor='lightgray')

		plt.yticks(rotation=0)
		plt.tick_params(which='both',
		                bottom=False,
		                left=False,
		                labelbottom=False,
		                labeltop=True)

		plt.title(input_title)
		plt.tight_layout()

		if output_file == "Auto":
			from datetime import datetime
			dt = datetime.today()
			output_file = f"bs_heatmap_{str(dt.month)}-{str(dt.day)}-{str(dt.year)[2:]}_{str(dt.hour)}:{str(dt.minute)}"
			plt.savefig(output_file+".png")
		elif output_file:
			plt.savefig(output_file)

		plt.show()


def merging_heatmaps(image_files_list, output_image='image.png'):
	import numpy as np
	import cv2
	if len(image_files_list)!=6:
		raise ValueError("image_files_list should only have 6 items")

	file = iter(image_files_list)
	image_1 = cv2.imread(next(file))
	image_2 = cv2.imread(next(file))
	image_3 = cv2.imread(next(file))
	image_4 = cv2.imread(next(file))
	image_5 = cv2.imread(next(file))
	image_6 = cv2.imread(next(file))
	top_image = np.concatenate((image_1, image_2, image_3), axis=0)
	bottom_image = np.concatenate((image_4, image_5, image_6), axis=0)
	final = np.concatenate((top_image, bottom_image), axis=1)
	cv2.imwrite(output_image, final)


display_ship_heatmap = lambda ship_type, output_file=None:DisplayGrid.make_heat_graft(
		DisplayGrid.display_specific_ship_heat_grid(ship_type),
		output_file, input_title=Battleship.ship_abbreviations[ship_type].title())

display_all_ships_heatmap = lambda output_file=None:DisplayGrid.make_heat_graft(
		DisplayGrid.display_total_ship_heat_grid(), output_file, input_title="All Ships")

if __name__ == "__main__":
	display_ship_heatmap(ship_type="p")# , output_file="01_p_heatmap_data.png")
	display_ship_heatmap(ship_type="s")# , output_file="02_s_heatmap_data.png")
	display_ship_heatmap(ship_type="d")# , output_file="03_d_heatmap_data.png")
	display_ship_heatmap(ship_type="b")# , output_file="04_b_heatmap_data.png")
	display_ship_heatmap(ship_type="c")# , output_file="05_c_heatmap_data.png")
	# display_all_ships_heatmap("00_total_heatmap_data.png")
	# merging_heatmaps(["01_p_heatmap_data.png", "01_s_heatmap_data.png", "01_d_heatmap_data.png",
	#                   "01_b_heatmap_data.png", "01_c_heatmap_data.png", "01_total_heatmap_data.png"])

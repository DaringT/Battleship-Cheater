import json
import pprint

class battleship():
    a_to_j = ("a","b","c","d","e","g","h","i","j")

    def __init__(self, battleship_grid=None):
        self.battleship_grid = battleship_grid
        if self.battleship_grid == None:
            self.battleship_grid = {
                "a":[0,0,0,0,0,0,0,0,0,0],
                "b":[0,0,0,0,0,0,0,0,0,0],
                "c":[0,0,0,0,0,0,0,0,0,0],
                "d":[0,0,0,0,0,0,0,0,0,0],
                "e":[0,0,0,0,0,0,0,0,0,0],
                "g":[0,0,0,0,0,0,0,0,0,0],
                "h":[0,0,0,0,0,0,0,0,0,0],
                "i":[0,0,0,0,0,0,0,0,0,0],
                "j":[0,0,0,0,0,0,0,0,0,0]}
    def add_patrol_boat(self):
        if self.direction == "s":
            self.battleship_grid[self.letter][self.number] = 1
            self.battleship_grid[battleship.a_to_j[self.letters_index+1]][self.number] = 1
            return self.battleship_grid

        elif self.direction == "n":
            self.battleship_grid[self.letter][self.number] = 1
            self.battleship_grid[battleship.a_to_j[self.letters_index-1]][self.number] = 1
            return self.battleship_grid

        elif self.direction == "e":
            self.battleship_grid[self.letter][self.number] = 1
            self.battleship_grid[self.letter][self.number+1] = 1
            return self.battleship_grid
        elif self.direction == "w":
            self.battleship_grid[self.letter][self.number] = 1
            self.battleship_grid[self.letter][self.number-1] = 1
            return self.battleship_grid

    def add_submairie(self):
        if self.direction == "s":
            # This is what happens you go South
            self.battleship_grid[self.letter][self.number] = 2
            self.battleship_grid[battleship.a_to_j[self.letters_index+1]][self.number] = 2
            self.battleship_grid[battleship.a_to_j[self.letters_index+2]][self.number] = 2
            return self.battleship_grid

        elif self.direction == "n":
            # This is what happens you go North
            self.battleship_grid[self.letter][self.number] = 2
            self.battleship_grid[battleship.a_to_j[self.letters_index-1]][self.number] = 2
            self.battleship_grid[battleship.a_to_j[self.letters_index-2]][self.number] = 2
            return self.battleship_grid

        elif self.direction == "e":
            # This is what happens you go East
            self.battleship_grid[self.letter][self.number] = 2
            self.battleship_grid[self.letter][self.number+1] = 2
            self.battleship_grid[self.letter][self.number+2] = 2
            return self.battleship_grid

        elif self.direction == "w":
            # This is what happens you go West
            self.battleship_grid[self.letter][self.number] = 2
            self.battleship_grid[self.letter][self.number-1] = 2
            self.battleship_grid[self.letter][self.number-2] = 2
            return self.battleship_grid

    def add_destroyer(self):
        if self.direction == "s":
            self.battleship_grid[self.letter][self.number] = 3
            self.battleship_grid[battleship.a_to_j[self.letters_index+1]][self.number] = 3
            self.battleship_grid[battleship.a_to_j[self.letters_index+2]][self.number] = 3
            return self.battleship_grid
        elif self.direction == "n":
            self.battleship_grid[self.letter][self.number] = 3
            self.battleship_grid[battleship.a_to_j[self.letters_index-1]][self.number] = 3
            self.battleship_grid[battleship.a_to_j[self.letters_index-2]][self.number] = 3
            return self.battleship_grid
        elif self.direction == "w":
            self.battleship_grid[self.letter][self.number] = 3
            self.battleship_grid[battleship.a_to_j[self.letters_index-1]][self.number] = 3
            self.battleship_grid[battleship.a_to_j[self.letters_index-2]][self.number] = 3
            return self.battleship_grid

        elif self.direction == "e":
            print("still needs configed!!")
            self.battleship_grid[self.letter][self.number] = 3
            self.battleship_grid[battleship.a_to_j[self.letters_index-1]][self.number] = 3
            self.battleship_grid[battleship.a_to_j[self.letters_index-2]][self.number] = 3
            return self.battleship_grid

    def add_battleship(self):
        if self.direction == "n":
            self.battleship_grid[self.letter][self.number] = 4
            self.battleship_grid[battleship.a_to_j[self.letters_index+1]][self.number] = 4
            self.battleship_grid[battleship.a_to_j[self.letters_index+2]][self.number] = 4
            self.battleship_grid[battleship.a_to_j[self.letters_index+3]][self.number] = 4
            return self.battleship_grid

        if self.direction == "s":
            self.battleship_grid[self.letter][self.number] = 4
            self.battleship_grid[battleship.a_to_j[self.letters_index+1]][self.number] = 4
            self.battleship_grid[battleship.a_to_j[self.letters_index+2]][self.number] = 4
            self.battleship_grid[battleship.a_to_j[self.letters_index+3]][self.number] = 4
            return self.battleship_grid

        elif self.direction == "e":
            self.battleship_grid[self.letter][self.number] = 4
            self.battleship_grid[self.letter][self.number+1] = 4
            self.battleship_grid[self.letter][self.number+2] = 4
            self.battleship_grid[self.letter][self.number+3] = 4
            return self.battleship_grid

        elif self.direction == "w":
            self.battleship_grid[self.letter][self.number] = 4
            self.battleship_grid[self.letter][self.number-1] = 4
            self.battleship_grid[self.letter][self.number-2] = 4
            self.battleship_grid[self.letter][self.number-3] = 4

    def add_aircraft_carrier(self):
        if self.direction == "n":
            self.battleship_grid[self.letter][self.number] = 5
            self.battleship_grid[battleship.a_to_j[self.letters_index+1]][self.number] = 5
            self.battleship_grid[battleship.a_to_j[self.letters_index+2]][self.number] = 5
            self.battleship_grid[battleship.a_to_j[self.letters_index+3]][self.number] = 5
            self.battleship_grid[battleship.a_to_j[self.letters_index+4]][self.number] = 5
            return self.battleship_grid

        if self.direction == "s":
            self.battleship_grid[self.letter][self.number] = 5
            self.battleship_grid[battleship.a_to_j[self.letters_index+1]][self.number] = 5
            self.battleship_grid[battleship.a_to_j[self.letters_index+2]][self.number] = 5
            self.battleship_grid[battleship.a_to_j[self.letters_index+3]][self.number] = 5
            self.battleship_grid[battleship.a_to_j[self.letters_index+4]][self.number] = 5
            return self.battleship_grid

        elif self.direction == "e":
            self.battleship_grid[self.letter][self.number] = 5
            self.battleship_grid[self.letter][self.number+1] = 5
            self.battleship_grid[self.letter][self.number+2] = 5
            self.battleship_grid[self.letter][self.number+3] = 5
            self.battleship_grid[self.letter][self.number+4] = 5
            return self.battleship_grid

        elif self.direction == "w":
            self.battleship_grid[self.letter][self.number] = 5
            self.battleship_grid[self.letter][self.number-1] = 5
            self.battleship_grid[self.letter][self.number-2] = 5
            self.battleship_grid[self.letter][self.number-3] = 5
            self.battleship_grid[self.letter][self.number-4] = 5


    def add_ships(self, coordinates, ship_type):
        self.letter, self.number, self.direction = coordinates

        self.letter = self.letter[0].lower()
        self.direction = self.direction[0].lower()

        print(f"letter: {self.letter} number:{self.number} direction:{self.direction} ship type: {ship_type}")
        self.number = int(self.number) - 1
        self.letters_index = battleship.a_to_j.index(self.letter)

        if ship_type == "p":
            return self.add_patrol_boat()

        elif ship_type == "s":
            return self.add_submairie()

        elif ship_type == "d":
            return self.add_destroyer()

        elif ship_type == "b":
            return self.add_battleship()

        elif ship_type == "c":
            return self.add_aircraft_carrier()


    def output_board_layout(self, output_file="battleship.json"):
        from datetime import date
        key = str(date.today())
        new_battleship_grid = dict()
        new_battleship_grid[key] = self.battleship_grid

        json_file_data =  json.dumps(pprint.pprint(new_battleship_grid))
        if output_file:
            with open(output_file, "w") as f:
                f.write(json_file_data)
        return json_file_data

# @staticmethod
def read_board_layout(input_file="battleship.json"):
    with open(input_file, "r") as f:
        for line in f:
            print(line)


def input_game():
    while True:
        ship_type = input("input Ship Type --> ")
        if ship_type == "exit":
            exit()

        letter = input("Add Letter --> ")
        number = input("Add Number --> ")
        direction = input("Add Direction   --> ")
        print(f"letter: {letter}\tnumber:{number}\tdirection: {direction}\tship_type: {ship_type}")

        b1 = battleship()
        p = b1.add_ships(coordinates=(letter,  number, direction), ship_type=ship_type)
        print("\n"*2)
        pprint.pprint(p)
        print("\n"*2)

# Letter = "c"
# Number = "2"
# Direction = "s"
# Ship_type = "p"

b1 = battleship()
# b1.add_ships(coordinates=(Letter,  Number, Direction), ship_type=Ship_type)
b1.add_ships(coordinates=("a",  "1", "e"), ship_type="p")
b1.add_ships(coordinates=("b",  "2", "e"), ship_type="s")

b1.add_ships(coordinates=("c",  "3", "e"), ship_type="d")
b1.add_ships(coordinates=("d",  "4", "e"), ship_type="b")
b1.add_ships(coordinates=("e",  "5", "e"), ship_type="c")

p = b1.output_board_layout()

print("reading file...\n")
read_board_layout()

pprint.pprint(p)

                # "b":[0,0,0,0,0,0,0,0,0,0],
                # "c":[0,0,0,0,0,0,0,0,0,0],
                # "d":[0,0,0,0,0,0,0,0,0,0],
                # "e":[0,0,0,0,0,0,0,0,0,0],
                # "g":[0,0,0,0,0,0,0,0,0,0],
                # "h":[0,0,0,0,0,0,0,0,0,0],
                # "i":[0,0,0,0,0,0,0,0,0,0],
                # "j":[0,0,0,0,0,0,0,0,0,0]}
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

    def add_ships(self, coordinates, ship_type):
        self.letter, self.number, self.direction = coordinates
        print(f"letter: {self.letter} number:{self.number} direction:{self.direction} ship type: {ship_type}")
        self.number = int(self.number) - 1
        self.letters_index = battleship.a_to_j.index(self.letter)

        if self.direction in {"s", "south"}:
            # print("south")
            if ship_type == "p":
                self.battleship_grid[self.letter][self.number] = 1
                self.battleship_grid[battleship.a_to_j[self.letters_index+1]][self.number] = 1
                return self.battleship_grid

            elif ship_type == "s":
                self.battleship_grid[self.letter][self.number] = 2
                self.battleship_grid[battleship.a_to_j[self.letters_index+1]][self.number] = 2
                self.battleship_grid[battleship.a_to_j[self.letters_index+2]][self.number] = 2
                return self.battleship_grid

            elif ship_type == "d":
                self.battleship_grid[self.letter][self.number] = 3
                self.battleship_grid[battleship.a_to_j[self.letters_index-1]][self.number] = 3
                self.battleship_grid[battleship.a_to_j[self.letters_index-2]][self.number] = 3
                return self.battleship_grid



        elif self.direction in {"n", "north"}:
            # print("north")
            if ship_type == "p":
                self.battleship_grid[self.letter][self.number] = 1
                self.battleship_grid[battleship.a_to_j[self.letters_index-1]][self.number] = 1
                return self.battleship_grid

            elif ship_type == "s":
                self.battleship_grid[self.letter][self.number] = 2
                self.battleship_grid[battleship.a_to_j[self.letters_index-1]][self.number] = 2
                self.battleship_grid[battleship.a_to_j[self.letters_index-2]][self.number] = 2
                return self.battleship_grid

            elif ship_type == "d":
                self.battleship_grid[self.letter][self.number] = 3
                self.battleship_grid[battleship.a_to_j[self.letters_index-1]][self.number] = 3
                self.battleship_grid[battleship.a_to_j[self.letters_index-2]][self.number] = 3
                return self.battleship_grid



        elif self.direction in {"e", "east"}:
            # print("east")
            if ship_type == "p":
                self.battleship_grid[self.letter][self.number] = 1
                self.battleship_grid[self.letter][self.number+1] = 1
                return self.battleship_grid

            elif ship_type == "s":
                self.battleship_grid[self.letter][self.number] = 2
                self.battleship_grid[self.letter][self.number+1] = 2
                self.battleship_grid[self.letter][self.number+2] = 2
                return self.battleship_grid

            elif ship_type == "d":
                self.battleship_grid[self.letter][self.number] = 3
                self.battleship_grid[battleship.a_to_j[self.letters_index-1]][self.number] = 3
                self.battleship_grid[battleship.a_to_j[self.letters_index-2]][self.number] = 3
                return self.battleship_grid



        elif self.direction in {"w", "west"}:
            # print("west")
            if ship_type == "p":
                self.battleship_grid[self.letter][self.number] = 1
                self.battleship_grid[self.letter][self.number-1] = 1
                return self.battleship_grid

            elif ship_type == "s":
                self.battleship_grid[self.letter][self.number] = 2
                self.battleship_grid[self.letter][self.number-1] = 2
                self.battleship_grid[self.letter][self.number-2] = 2
                return self.battleship_grid

        # print(self.battleship_grid[self.letter][self.number])


b1 = battleship()
p = b1.add_ships(coordinates=("c", "2", "w"), ship_type="s")
pprint.pprint(p)
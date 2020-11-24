import re
from pprint import pprint


class BSD:
    def __init__(self, input_file="book_direction.txt"):
        self.input_file = input_file
        self.bs_dict = dict()

    @staticmethod
    def gird_title(input_bsg_title):
        """
        Returns a found bsg_title using regex else None

        :parameter: input_bsg_title
        :ptype: str

        :return: bsg_title
        :rtype: str
        """
        bsg_title = None

        bsg_regex = r"//(\w\d\d?)"
        bsg_prog = re.compile(bsg_regex)
        bsg_result = bsg_prog.match(input_bsg_title)

        try:
            bsg_title = bsg_result.group(1)
        except AttributeError:
            pass
        return bsg_title

    @staticmethod
    def grid_directions(input_bsg_directions):
        """Returns a found Episode number using regex else None
        Paramiters:
               input_bsg_directions (str)
        Returns:
               "Ep_##" (str) else: None
        """
        bsg_key = letter = number = direction = None

        bsg_regex = r'\s{4}(\w):((\w)(\d\d?)(\w))'
        bsg_prog = re.compile(bsg_regex)
        bsg_result = bsg_prog.match(input_bsg_directions)
        try:
            bsg_key = bsg_result.group(1)

            letter = bsg_result.group(3)
            number = bsg_result.group(4)
            direction = bsg_result.group(5)
        except AttributeError:
            pass

        return bsg_key, letter, number, direction

    @staticmethod
    def input_anything(input_file_line):
        """Returns if the input is a TS. or EP. or neither and cleans it with gird_title() or grid_directions()
               Paramiters:
                       input_file_line (str)
               Returns:
                       State:
                               "EP" (str) or "TS" (str) or None
                       if a TS or EP Returns Result:
                               Result of grid_directions() or gird_title() else None
       """
        bsg_title = BSD.gird_title(input_file_line)
        bsg_directions = BSD.grid_directions(input_file_line)
        if type(bsg_title) == str:
            title = 'bsg_title'
            state = title
            return state, bsg_title
        elif bsg_directions[1] is not None:
            state = 'bsg_directions'
            return state, bsg_directions
        else:
            return None, None

    def raw_data_to_dict(self):
        """
        Converts battleship raw data to dict
        :Example:
            //a1
                p:a1e
                s:b1e
                d:j10n
                b:etc.
                c:etc.
            //a2
                etc..
        :return: self.bs.dict
        :rtype: dict
        """
        with open(self.input_file, 'r') as File:
            for line in File:
                state, temp = BSD.input_anything(line)
                if state == 'bsg_title':
                    grid_title = temp
                    self.bs_dict[grid_title] = dict()
                elif state == 'bsg_directions':
                    self.bs_dict[grid_title][temp[0]] = tuple(temp[1:])
        return self.bs_dict

    def raw_to_json(self, output_json_file="book_directions.json"):
        """
        This func turn raw BSG data into json format
        with raw_to_dict func.
        :param output_json_file:
        :type output_json_file: str
        """
        import json
        with open(output_json_file, "w") as f:
            self.raw_data_to_dict()
            f.write(json.dumps(self.bs_dict, indent=2))


b1 = BSD()
b1.raw_to_json()

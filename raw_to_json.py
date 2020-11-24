import re
from pprint import pprint


class BSD:
    def __init__(self, input_file="book_direction.txt"):
       self.input_file = input_file


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
    def input_anything(Input):
        """Returns if the input is a TS. or EP. or neither and cleans it with gird_title() or grid_directions()
               Paramiters:
                       Input (str)
               Returns:
                       State:
                               "EP" (str) or "TS" (str) or None
                       if a TS or EP Returns Result:
                               Result of grid_directions() or gird_title() else None
       """
        bsg_title = BSD.gird_title(Input)
        bsg_directions = BSD.grid_directions(Input)
        if type(bsg_title) == str:
            State = 'bsg_title'
            return State, bsg_title
        elif bsg_directions[1] != None:
            State = 'bsg_directions'
            return State, bsg_directions
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
        bsg_list = []
        self.bs_dict = dict()
        with open(self.input_file, 'r') as File:
            for line in File:
                State, Temp = BSD.input_anything(line)
                if State == 'bsg_title':
                    grid_title = Temp
                    self.bs_dict[grid_title] = dict()
                elif State == 'bsg_directions':
                    self.bs_dict[grid_title][Temp[0]] = tuple(Temp[1:])
        return self.bs_dict


    def raw_to_json(self, output_json_file="book_directions.json"):
        import json
        with open(output_json_file, "w") as f:
           self.raw_data_to_dict()
           # f.write(json.dumps(self.bs_dict, indent=2))
           f.write(json.dumps(self.bs_dict))

b1 = BSD()
b1.raw_to_json()
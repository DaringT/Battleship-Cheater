import re
class BSD():
   def __init__(self, input_file):
       self.input_file = input_file

   def raw_to_json(self):
        with open(self.input_file) as f:
            file_data = f.readlines()

   def gird_title(input_bsg_title):
       """
       Returns a found bsg_title using regex else None

       Paramiters:
                    :input_bsg_title (str)
       """
       bsg_title = None

       bsg_regex = r"//(\w\d\d?)"
       bsg_prog = re.compile(bsg_regex)
       bsg_result = bsg_prog.match(input_bsg_title)

       try:
           bsg_title = bsg_result.group(1)
       except AttributeError:
           pass

       if bsg_title:
            return bsg_title
       else:
           return None

   def grid_directions(input_bsg_directions):
       """Returns a found Episode number using regex else None
               Paramiters:
                       input_bsg_directions (str)
               Returns:
                       "Ep_##" (str) else: None
       """
       input_bsg_directions = None

       ep_regex = r''
       ep_prog = re.compile(ep_regex)
       ep_result = ep_prog.match(input_bsg_directions)
       try:
           gr_four = ep_result.group(4)
           gr_three = ep_result.group(3)
           gr_six = ep_result.group(6)
       except AttributeError:
           pass

       if gr_four or gr_three or gr_six:
           if gr_four == None:
               pass
           else:
               EP_State = ('Ep_%s' % (gr_four))
           if gr_three == None:
               pass
           else:
               EP_State = ('Ep_%s' % (gr_three))
           if gr_six == None:
               pass
           else:
               EP_State = ('Ep_%s' % (gr_six))
       else:
           EP_State = None
       return EP_State

   def Input_anything(Input):
       """Returns if the input is a TS. or EP. or neither and cleans it with gird_title() or grid_directions()
               Paramiters:
                       Input (str)
               Returns:
                       State:
                               "EP" (str) or "TS" (str) or None
                       if a TS or EP Returns Result:
                               Result of grid_directions() or gird_title() else None
       """
       r_ep = BSD.grid_directions(Input)
       r_ts = BSD.gird_title(Input)
       if type(r_ep) == str:
           State = 'EP'
           return State, r_ep
       elif type(r_ts) == str:
           State = 'TS'
           return State, r_ts
       else:
           return None, None

       # def make_xml(bsg_list, file=None)

   def CoreV2(self):
        """This Function does the created naming of the files"""

        exten = self.chapter_file_type
        self.bsg_list = []
        with open(self.input_file, 'r') as File:
            for line in File:
                State, Temp = BSD.Input_anything(line)
                if State == 'EP':
                    if self.bsg_list > []:
                        print(self.bsg_list)
                        if exten == "txt":
                            BSD.make_txt(self, output_file=ep_f)
                        # elif exten == "xml":
                        #     BSD.make_xml(self, output_file=ep_f)
                        ep_f.close()

                    print(f"Creating: {Temp}.{exten}")
                    ep_f = open(f"{Temp}.{exten}", "w")

                    self.bsg_list = list()
                elif State == 'TS':
                    self.bsg_list.append(Temp)
                else:
                    pass
            print(self.bsg_list)
            if exten == "txt":
                BSD.make_txt(self, output_file=ep_f)
            elif exten == "xml":
                BSD.make_xml(self, output_file=ep_f)
#!/usr/bin/env python

import sys, os
from random import randrange
from pprint import pprint

class Unique_line_repeat(object):

  def __init__(self, file_name, repeat=2):

    self.filename = file_name
    self.repeat   = repeat

  def process_input(self):
   
    str_repeat_dict = dict() 
    f = open(self.filename,'r')
    for each_line in f.readlines():
      three_char_str = each_line.strip()

      try:
        if str_repeat_dict[three_char_str]:
          str_repeat_dict[three_char_str] += 1

      except KeyError as e:
        str_repeat_dict[three_char_str] = 1
        
        

    pprint(str_repeat_dict)

def main():

  if len(sys.argv) < 2 or len(sys.argv) > 4:
    print("Usage: {0} <full_path_of_text_file> [<repeat>]".format(sys.argv[0]))
    print("e.g.: {0} ~/test_input_file.txt 6\n".format(sys.argv[0]))
    sys.exit(1)

  file_name = sys.argv[1]
  repeat    = 0
  if len(sys.argv) == 2:
    pass
  else:
    repeat = sys.argv[2]

  u_obj = Unique_line_repeat(file_name, repeat)
  u_obj.process_input()

if __name__ == '__main__':
  main()  

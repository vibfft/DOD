#!/usr/bin/env python

import sys, os
from random import randrange
from pprint import pprint

class Unique_line_repeat(object):

  def __init__(self, file_name, repeat):

    self.filename = file_name
    self.repeat   = repeat
    self.str_repeat_dict = dict()

  def process_input(self):
   
    f = open(self.filename,'r')
    for each_line in f.readlines():
      three_char_str = each_line.strip()
      try:
        if self.str_repeat_dict[three_char_str]:
          self.str_repeat_dict[three_char_str]['str_ct'] += 1 

      except KeyError as e:
        self.str_repeat_dict[three_char_str] = {'str_ct': 1, 
                                                'rand_repeat': self.map_str_repeat(three_char_str)}
        
    #pprint(self.str_repeat_dict)
    for each_str in sorted(self.str_repeat_dict.items(), key = lambda x: x[1]['str_ct']): 
      list_to_str = ','.join(each_str[1]['rand_repeat'])
      print('{0} {1}'.format(list_to_str, each_str[1]['str_ct']))

  def map_str_repeat(self, three_char_str):
 
    rand_repeat = randrange(1,int(self.repeat) + 1)
    comb_str_after_repeat = [] 
    for i in range(rand_repeat):
      comb_str_after_repeat.append(three_char_str)
    return comb_str_after_repeat

def main():

  if len(sys.argv) < 2 or len(sys.argv) > 4:
    print("Usage: {0} <full_path_of_text_file> [<repeat>]".format(sys.argv[0]))
    print("e.g.: \n\t{0} ~/test_input_file.txt 6".format(sys.argv[0]))
    print("\t{0} ~/test_input_file.txt\n".format(sys.argv[0]))
    sys.exit(1)

  file_name = sys.argv[1]
  repeat    = 2 
  if len(sys.argv) == 2:
    pass
  else:
    repeat = sys.argv[2]

  u_obj = Unique_line_repeat(file_name, repeat)
  u_obj.process_input()

if __name__ == '__main__':
  main()  

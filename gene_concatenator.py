#Arin Gahramanova 08/13/23
#This program concatenates genome sequence alignments per organism from the set of files in the input folder  
import os
import sys

def get_data(fname, size):
  out = []
  with open(fname, "r") as f:
      for line in f.readlines():
        line = line.strip()
        if len(line) > 0 and ( line[0] != '>' ):
          out.append(line)
  if len(out) != size:
    sys.exit('invalid input (mismatching number of organisms)') 
  return out
  
names = []
output = []
path = input("Enter input folder name: ")
dir_list = os.listdir(path)
if len(dir_list) == 0:
  sys.exit('empty input')

#read in the names of organisms based on the first file 
with open(path + '/' + dir_list[0], "r") as f:
  for line in f.readlines():
    line = line.strip()
    if len(line) > 0 and ( line[0] == '>' ):
      names.append(line)
size = len(names)

for i in range(size):
  output.append('')
  
for fname in dir_list:
  align = get_data(path + '/' + fname, size)
  for i in range(size):
    output[i] += align[i]

out_str = ''
for i in range(size):
  out_str += (names[i] + '\n' + output[i] + '\n')
  
with open("output.fas", "w") as f:
  f.write(out_str)
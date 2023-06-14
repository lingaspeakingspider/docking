from pyrosetta import *
from pyrosetta.toolbox import *
from dockstring1 import docking
import os
init()

index_of_mutate_amino=0 #2D Diagram

aminoacid_list=['M', 'P', 'A', 'V', 'G', 'Y', 'T', 'D', 'W', 'I', 'F', 'S', 'K', 'E', 'H', 'L', 'N', 'R', 'C', 'Q']

model = pose_from_pdb("<protein>")
for i in aminoacid_list:
  seq=pose.sequence()
  
  mutate_residue(pose, index_of_mutate_amino, i)
  os.chdir("/home/biocally/Desktop")
  pose.dump_file("output.pdb")
  
  docking("<output>", i, seq[index_of_mutate_amino])






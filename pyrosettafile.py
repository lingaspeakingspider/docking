from pyrosetta import *
from pyrosetta.toolbox import *
from dockstring1 import docking
init()

index_of_mutate_amino=0 #2D Diagram

aminoacid_list=['M', 'P', 'A', 'V', 'G', 'Y', 'T', 'D', 'W', 'I', 'F', 'S', 'K', 'E', 'H', 'L', 'N', 'R', 'C', 'Q']

model = pose_from_pdb("<protein>")
for i in aminoacid_list:
  seq=pose.sequence()
  
  mutate_residue(pose, index_of_mutate_amino, i)
  #Nimm anhand eines Formular, das in VS Code liegt, an, wie wir die Unterlagen in PyRosetta speichern
  
  docking("<output>", i, seq[index_of_mutate_amino])






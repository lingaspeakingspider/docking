from pyrosetta import *
from pyrosetta.toolbox import *
from dock import docking
import random
init()

index_of_mutate_amino=0

aminoacid_list=['M', 'P', 'A', 'V', 'G', 'Y', 'T', 'D', 'W', 'I', 'F', 'S', 'K', 'E', 'H', 'L', 'N', 'R', 'C', 'Q']
random_amino = random.choice(aminoacid_list)

model = pose_from_pdb("<protein>")

seq=pose.sequence()
print(seq)

mutate_residue(pose, index_of_mutate_amino, random_amino)




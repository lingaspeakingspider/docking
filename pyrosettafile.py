from pyrosetta import *
from pyrosetta.toolbox import *

init()

model=pose_from_pdb("<protein>")

seq=pose.sequence()
print(seq)

#1-) specify amino acids
#2-) apply mutations

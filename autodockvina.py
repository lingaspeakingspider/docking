from vina import Vina
import os

v = Vina(sf_name='vina')

v.set_receptor('<protein>')

v.set_ligand_from_file('<ligand>')
v.compute_vina_maps(center=[15.190, 53.903, 16.917], box_size=[20, 20, 20])

# Score the current pose
# energy = v.score()
# print('Score before minimization: %.3f (kcal/mol)' % energy[0])

# Minimized locally the current pose
# energy_minimized = v.optimize()
# print('Score after minimization : %.3f (kcal/mol)' % energy_minimized[0])
# v.write_pose('1iep_ligand_minimized.pdbqt', overwrite=True)

# Dock the ligand
v.dock(exhaustiveness=32, n_poses=20)
os.chdir("/home/biocally/Desktop")
v.write_poses('<output>', n_poses=5, overwrite=True)

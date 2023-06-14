from dockstring import load_target
import os
import rdkit.Chem as Chem

def docking(output):
  smiles = "<smiles of ligand>"
  Chem.MolFromSmiles(smiles)

  target = load_target(output)
  score, aux = target.dock(smiles)
  os.chdir("/home/biocally/Desktop")
  with open("file.txt", "w") as file:
    file.write()

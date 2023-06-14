from dockstring import load_target

import rdkit.Chem as Chem

def docking(output):
  smiles = "<smiles of ligand>"
  Chem.MolFromSmiles(smiles)

  target = load_target(output)
  score, aux = target.dock(smiles)

from dockstring import load_target

import rdkit.Chem as Chem

smiles = "<smiles of ligand>"
Chem.MolFromSmiles(smiles)

target = load_target("<protein file>")
score, aux = target.dock(smiles)

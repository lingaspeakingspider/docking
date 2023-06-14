from dockstring import load_target

import rdkit.Chem as Chem

smiles = 'CC1=C(C(=O)N2CCCCC2=N1)CCN3CCC(CC3)C4=NOC5=C4C=CC(=C5)F'
Chem.MolFromSmiles(smiles)

target = load_target('DRD2')
score, aux = target.dock(smiles)
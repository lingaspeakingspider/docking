from docking import Docking
import time

start=time.perf_counter()
receptor="7da5.pdb"
ligand="lactate.pdbqt"
main_dir="/home/biocally/Desktop/docking"
log_path="/home/biocally/Desktop/docking/log_bey.log"

values_list=[231, 293, 235, 232, 143, 23, 139, 140, 19, 239, 20]
aminoacid_list=['M', 'P', 'A', 'V', 'G', 'Y', 'T', 'D', 'W', 'I', 'F', 'S', 'K', 'E', 'H', 'L', 'N', 'R', 'C', 'Q']
output_dir="/home/biocally/Desktop/docking_outputs"

a=1
for value in values_list:
    dock_variable=Docking(receptor=receptor, ligand=ligand, main_dir=main_dir, index_of_residue=value)

    if a==0:
        dock_variable.cleaning_atom()
        a+=1

    else:
        pass

    for amino_acid_which_will_mutated in aminoacid_list:
        dock_variable.mutation(amino_acid_which_will_mutated, output_dir_path=main_dir, output_file_name_pdb="7da5.pdb")
        dock_variable.converting_receptor_pdb_to_pdbqt(receptor)
        dock_variable.docking_process(receptor_name="7da5", main_dir=main_dir, ligand_smiles='CC(C(=O)[O-])O',
                                       saves="/home/biocally/Desktop/docking_outputs/saves.txt")

finish=time.perf_counter()
minute=round((start-finish)/60, 2)

print("Finished in {} minutes.".format(minute))
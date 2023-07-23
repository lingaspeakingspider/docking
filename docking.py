from pyrosetta import *
from pyrosetta.toolbox import *
from pathlib import Path
from pymol.cgo import *
init()

previous:str
current:str

class Docking:

    def __init__(self, receptor: str, ligand: str, main_dir: Path, index_of_residue: int):
        self.receptor=receptor
        self.ligand=ligand
        self.main_dir=main_dir
        self.index_of_residue=index_of_residue

    def docking_process(self, receptor_name: str, main_dir:str, ligand_smiles: str, saves: Path):
        import dockstring
        import rdkit.Chem as Chem


        #smiles = 'CC(C(=O)[O-])O' -> lactate
        Chem.MolFromSmiles(ligand_smiles)

        target= dockstring.target.Target(name=receptor_name, working_dir=main_dir, targets_dir=main_dir)

        score, aux=target.dock(smiles=ligand_smiles)

        # target._dock_pdbqt(os.path.join(main_dir , self.receptor), log_path=log_path, out_path=docking_output_path, seed=0)
        # aux=[]

        # with open(docking_output_path, "r") as output_file:
        #     for i in range(1,101, 25):
        #         line=output_file.readlines()[i]
        #         affinity=line[25:29]
        #         aux.append(affinity)

        # os.remove(docking_output_path)

        with open(saves, "a") as f:
            f.write(f"Index of mutated amino acid: {self.index_of_residue}  ,  Name of previous amino acid: {previous}  ,  Name of current amino acid: {current}  ,  Affinities: {aux}\n")

        name=self.receptor.replace(".pdb", "_target.pdbqt")
        os.remove(main_dir + "/" + name)


    def cleaning_atom(self):
        os.chdir(self.main_dir)
        pose=(self.receptor)
        cleanATOM(pose)
        clean_name=self.receptor.replace(".pdb", ".clean.pdb")
        os.remove(self.receptor)
        os.rename(clean_name,  self.receptor)

        

    def converting_receptor_pdb_to_pdbqt(self, filename):
        cmd.load(filename)
        cmd.remove('resn HOH')
        cmd.h_add(selection='acceptors or donors')
        cmd.save('protein.pdb')
        os.system('obabel protein.pdb -O temp.pdbqt -xh --partialcharge gasteiger')
        os.system('grep ATOM temp.pdbqt > receptor.pdbqt')
        os.remove('temp.pdbqt')
        os.remove('protein.pdb')
        new_name=(self.receptor.split(".")[0]) + "_target.pdbqt"
        os.rename("receptor.pdbqt", new_name)
        # os.chdir(path=path)
        # # liste=os.listdir(path)
        # # if liste.count(self.receptor)==1:
        # #     os.remove(self.receptor)

    def converting_ligand_mol2_to_pdbqt(self, output_dir_path: Path, output_file: str):
        from openbabel import pybel
        import os

        os.chdir(output_dir_path)

        ligand = [m for m in pybel.readfile(filename=self.ligand, format='mol2')][0]
        out=pybel.Outputfile(filename=output_file ,format='pdbqt',overwrite=True)
        out.write(ligand)
        out.close()


    def mutation(self, amino_acid, output_dir_path: Path, output_file_name_pdb: str):
        global previous
        global current

        os.chdir("/home/biocally/Desktop/docking2")
        pose = pose_from_pdb(self.receptor)

        previous=pose.residue(self.index_of_residue).name()

        mutate_residue(pose, self.index_of_residue, amino_acid)
        
        current=pose.residue(self.index_of_residue).name()

        os.chdir(output_dir_path)
        liste=os.listdir(output_dir_path)
        if liste.count(output_file_name_pdb)!=0:
            os.remove(output_file_name_pdb)
        
        pose.dump_file(output_file_name_pdb)
        
    



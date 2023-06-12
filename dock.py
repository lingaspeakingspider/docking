from ccdc.docking import Docker
from ccdc.io import MoleculeReader, EntryReader
import tempfile
import os

def docking(protein,ligand, output_name):
  docker = Docker()
  settings = docker.settings

  MLL1_protein_file = protein

  settings.add_protein_file(MLL1_protein_file)

  # #*****************************
  # #Binding Site belirleme kısmı (isteğe bağlı)
  # MLL1_native_ligand_file = ""#<proteinde bulunan hazır ligandın dosyası> string olarak yaz

  # MLL1_native_ligand = MoleculeReader(MLL1_native_ligand_file)[0]
  # MLL1_protein = settings.proteins[0]
  # settings.binding_site = settings.BindingSiteFromLigand(MLL1_protein, MLL1_native_ligand, 8.0)
  # #*****************************

  MLL1_ligand_file = ligand
  MLL1_ligand = MoleculeReader(MLL1_ligand_file)[0]
  settings.add_ligand_file(MLL1_ligand_file, 10)

  os.chdir("/home/biocally/Desktop")
  settings.fitness_function = 'plp'
  settings.autoscale = 10.
  settings.early_termination = False
  batch_tempd = tempfile.mkdtemp()
  settings.output_directory = batch_tempd
  settings.output_file = output_name


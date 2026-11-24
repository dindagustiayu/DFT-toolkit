#!/usr/bin/env python
# coding: utf-8
# edit by materials@dindagustiayu.com

# import directories 
from rdkit import Chem
from rdkit.Chem import Draw
from rdkit.Chem import AllChem
from rdkit.Chem.Draw import IPythonConsole
IPythonConsole.drawOptions.addAtomIndices = True


# 3D format from molecule
smiles = "YOUR-SMILES-MOLECULE"
mol = Chem.MolFromSmiles(smiles)
mol = Chem.AddHs(mol)
Chem.AllChem.EmbedMolecule(mol)
Chem.AllChem.MolToXYZFile(mol, "mol.xyz")
Chem.AllChem.MolToFile(mol, "mol.svg", size=(500, 500))
mol
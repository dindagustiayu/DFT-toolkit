#!/usr/bin/env python
# coding: utf-8

# # Constraint Optimization and Torsional Energy Barriers
# 
# Finally perform the dihedral angle scan to get the potential energy surface as shown in figure S1 of the S1.
# 
# **Hint**: Run SCF calculations for different dihedral angle. You can omit optimization of the structure with dihedral [constraints](https://pyscf.org/user/geomopt.html).

# import directories 
from rdkit import Chem
from rdkit.Chem import Draw
from rdkit.Chem import AllChem
from rdkit.Chem.Draw import IPythonConsole
IPythonConsole.drawOptions.addAtomIndices = True


# 3D format from C10H9N3
smiles = "N1=C(C=C(C=C1)N)C1=NC=CC=C1"
mol = Chem.MolFromSmiles(smiles)
mol = Chem.AddHs(mol)
Chem.AllChem.EmbedMolecule(mol)
mol


# ## Constraint for N0C1N8C7 179.51 Degree

# Set the value to 0 for the conformer
Chem.AllChem.SetDihedralDeg(mol.GetConformer(0),0,1,7,8,179.51)

# Save the new conformer
Chem.MolToXYZFile(mol, "AMBPY_1.xyz")

# Looks like it is set to 179.51
mol


# Now, we optimize the structure in gas phase (not solvent effect) and run frequency calculations to confirm convergence.

# SCF Energy (Reference)
from pyscf import gto, scf

mol = gto.M(atom="optimization_file/opt_AMBPY1.xyz")

# set basis set
mol.basis = "6-31+G**"

# set the functional
mf = mol.KS()
mf.xc = 'b3lyp'
mf.disp = 'd3bj'

# Run energy calculations
mf.kernel()


# Constraint at 179.81

with open("AMBPY1.txt", "w") as f:
    f.write("$set\n")
    f.write(f"dihedral 1 2 8 9 179.51\n")

print(open("AMBPY1.txt").read())


# Constraint
from pyscf.geomopt.geometric_solver import optimize

params = {"constraints": "AMBPY1.txt",}
mol_eq = optimize(mf, assert_convergence=True, **params)


# save the optimized geometry for visualization
mol_eq.tofile("const_AMBPY1.xyz")


# SCF energy for specific angle
from pyscf import gto, scf

mol = gto.M(atom="const_AMBPY1.xyz")

# set basis set
mol.basis = "6-31+G**"

# set the functional
mf = mol.KS()
mf.xc = 'b3lyp'
mf.disp = 'd3bj'

# Run energy calculations
neutral_energy = mf.kernel()


# ## Torsional energy barrier for N0C1N8C7 179.51 Degree


# Torsional energy barrier with reference
E_max = -543.86902100527 # SCF Energy theta (angle)
E_min = -543.869022713094 # SCF Energy reference from convergence

Delta_E = (E_max - E_min) * 2625.4996 #from Hartree to kJ/mol
Delta_E


# ## Constraint for N0C1N8C7 170.81 Degree

# Set the value to 0 for the conformer
Chem.AllChem.SetDihedralDeg(mol.GetConformer(0),0,1,7,8,170.81)

# Save the new conformer
Chem.MolToXYZFile(mol, "AMBPY_2.xyz")

# Looks like it is set to 179.51
mol


# SCF Energy
from pyscf import gto, scf

mol = gto.M(atom="AMBPY_2.xyz")

# set basis set
mol.basis = "6-31+G**"

# set the functional
mf = mol.KS()
mf.xc = 'b3lyp'
mf.disp = 'd3bj'


# Constraint at 170.81

with open("AMBPY2.txt", "w") as f:
    f.write("$set\n")
    f.write(f"dihedral 1 2 8 9 170.81\n")

print(open("AMBPY2.txt").read())


# Constraint
from pyscf.geomopt.geometric_solver import optimize

params = {"constraints": "AMBPY2.txt",}
mol_eq = optimize(mf, assert_convergence=True, **params)



# save the optimized geometry for visualization
mol_eq.tofile("const_AMBPY2.xyz")



# SCF Energy
from pyscf import gto, scf

mol = gto.M(atom="const_AMBPY2.xyz")

# set basis set
mol.basis = "6-31+G**"

# set the functional
mf = mol.KS()
mf.xc = 'b3lyp'
mf.disp = 'd3bj'

# Run energy calculations
neutral_energy = mf.kernel()


# ## Torsional energy barrier for N0C1N8C7 170.81 Degree


# Torsional energy barrier with reference
E_max = -543.868832199782 # theta (angle)
E_min = -543.869022713094 # reference from convergence

Delta_E = (E_max - E_min) * 2625.4996 #from Hartree to kJ/mol
Delta_E


# ## Constraint for N0C1N8C7 220.79 Degree


# 3D format from C10H9N3
smiles = "N1=C(C=C(C=C1)N)C1=NC=CC=C1"
mol = Chem.MolFromSmiles(smiles)
mol = Chem.AddHs(mol)
Chem.AllChem.EmbedMolecule(mol)
mol


# Set the value to 0 for the conformer
Chem.AllChem.SetDihedralDeg(mol.GetConformer(0),0,1,7,8,220.79)

# Save the new conformer
Chem.MolToXYZFile(mol, "AMBPY_3.xyz")

# Looks like it is set to 220.79
mol


# SCF Energy
from pyscf import gto, scf

mol = gto.M(atom="AMBPY_1.xyz")

# set basis set
mol.basis = "6-31+G**"

# set the functional
mf = mol.KS()
mf.xc = 'b3lyp'
mf.disp = 'd3bj'


# Constraint at 220.79

with open("AMBPY3.txt", "w") as f:
    f.write("$set\n")
    f.write(f"dihedral 1 2 8 9 220.79\n")

print(open("AMBPY3.txt").read())


# Constraint
from pyscf.geomopt.geometric_solver import optimize

params = {"constraints": "AMBPY3.txt",}
mol_eq = optimize(mf, assert_convergence=True, **params)


# save the constraint for visualization
mol_eq.tofile("const_AMBPY3.xyz")


# SCF Energy
from pyscf import gto, scf

mol = gto.M(atom="const_AMBPY3.xyz")

# set basis set
mol.basis = "6-31+G**"

# set the functional
mf = mol.KS()
mf.xc = 'b3lyp'
mf.disp = 'd3bj'

# Run energy calculations
neutral_energy = mf.kernel()


# ## Torsional energy barrier for N0C1N8C7 220.79 Degree

# Torsional energy barrier with reference
E_max = -543.864663635382 # theta (angle)
E_min = -543.869022713094 # reference from convergence

Delta_E = (E_max - E_min) * 2625.4996 #from Hartree to kJ/mol
Delta_E





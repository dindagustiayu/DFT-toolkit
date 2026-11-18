#!/usr/bin/env python
# coding: utf-8

# ---
# title: Practice 2
# date: "2026-10-17"
# ---
# 
# We will reproduce results from the article [ Spectrochimica Acta Part A: Molecular and Biomolecular Spectroscopy, 2015, 148, 163-174](https://doi.org/10.1016/j.saa.2015.03.105). The article contains results from experiments and computations. The molecule investigated is 2-chloro-3-quinolinecarboxaldehyde. Perform all our calculations with B3LYP and CAM-B3LYP (DFPT-DFT) functional and basis set 6-31G(d, p). See below for graphical abstract.

# import directories 
from rdkit import Chem
from rdkit.Chem import Draw
from rdkit.Chem import AllChem
from rdkit.Chem.Draw import IPythonConsole
IPythonConsole.drawOptions.addAtomIndices = True


# First, we will create the 3D structure of the molecule [4-amino-2,2'bipyridine](https://www.chemspider.com/Chemical-Structure.1039202.html), CAS NUMBER: 73568-25-9.


# 3D format from C10H6ClNO
smiles = "C1=CC=C2C(=C1)C=C(C(=N2)Cl)C=O"
mol = Chem.MolFromSmiles(smiles)
mol = Chem.AddHs(mol)
Chem.AllChem.EmbedMolecule(mol)
Chem.AllChem.MolToXYZFile(mol, "C10H6ClNO.xyz")
mol


# Now, we optimize the structure in gas phase (not solvent effect) and run frequency calculations to confirm convergence.

# Geometry Optimization
from pyscf import gto, scf
from pyscf.geomopt.geometric_solver import optimize

# Create the pyscf molecule
mol = gto.M(atom="C10H6ClNO.xyz")

mol.basis = "6-31+G**"

# set the functional
mf = mol.KS()
mf.xc = 'b3lyp'

# Run optimization calculations
mol_eq = optimize(mf)
mol_eq

# Run convergence
conv_params = {
    'convergence_energy': 1e-6, # Eh
    'convergence_grms': 3e-4,   # Eh/Bohr
    'convergence_gmax': 4.5e-4, # Eh/Bohr
    'convergence_drms': 1.2e-3, # Angstrom
    'convergence_dmax': 1.8e-3, # Angstrom
}

mol_eq = optimize(mf, **conv_params)


# save the optimized geometry for visualization
mol_eq.tofile("opt_C10H6ClNO.xyz")


# Open file
from rdkit import Chem
from rdkit.Chem import Draw, rdDetermineBonds

rd = Chem.MolFromXYZFile("opt_C10H6ClNO.xyz")
rdDetermineBonds.DetermineBonds(rd, charge=0)
rd

# Import bond length (Angstrong) 
from rdkit.Chem import rdMolTransforms as T

rd = Chem.MolFromXYZFile("opt_C10H6ClNO.xyz")  

# calculates the angle
conf = rd.GetConformer()                         
T.GetBondLength(conf, 2, 1) 


# Import angle degree
from rdkit.Chem import rdMolTransforms as T

rd = Chem.MolFromXYZFile("opt_C10H6ClNO.xyz")  

# calculates the angle
conf = rd.GetConformer()                         
T.GetAngleDeg(conf, 1, 2, 3)


# Next, we run frequency to check that the forces (first derivatives) are near zero (stationary point is minimum). A mimimum has no imaginary frequencies and a saddle point has at least one.

# Frequency
from pyscf import gto, scf

# create a molecule object
mol = gto.M(atom = "opt_C10H6ClNO.xyz")

# set the basis set
mol.basis = '6-31+G**'

# set the functional
mf = mol.KS()
mf.xc = 'b3lyp'

# run frequency calculation
mf.run()
hessian = mf.Hessian().kernel()


# compute frequency
from pyscf.hessian import thermo

# getting the frequency data from the calculation
freq_info = thermo.harmonic_analysis(mf.mol, hessian)
freq_info["freq_wavenumber"]

# SCF Energy
from pyscf import gto, scf

mol = gto.M(atom="opt_C10H6ClNO.xyz")

# set basis set
mol.basis = "6-31+G**"

# set the functional
mf = mol.KS()
mf.xc = 'b3lyp'

# Run energy calculations
neutral_energy = mf.kernel()


# Create the MOs (Molecular Orbitals)

# total number of electrons
n = mol.tot_electrons()
n

# display all orbitals
mf.mo_energy


# import the definitions
from pyscf.tools import molden

# We will write the surface to molden files
with open('C10H6ClNO.molden', 'w') as f1:
    molden.header(mol, f1)
    molden.orbital_coeff(mol, f1, mf.mo_coeff, ene=mf.mo_energy, occ=mf.mo_occ)


# Simulated DFT of IR spectra of 2-Chloro-3-quinolinecarboxaldehyde
from pyscf import gto, dft
from pyscf.prop import infrared
from pyscf.hessian import thermo

# Create the pyscf molecule
mol = gto.M(atom ="opt_C10H6ClNO.xyz")

mol.basis = "6-31+G**"

# set the functional
mf = dft.RKS(mol, xc = "b3lyp").run()

# Run infrared calculation, invokes hessian, though calling hessian
mf_ir = infrared.rks.Infrared(mf).run()
mf_ir.summary()

# To perform thermo calculation, use the hessian object inside mf_ir
thermo.dump_thermo(mol, thermo.thermo(mf, mf_ir.vib_dict["freq_au"], 298.15, 101325))

# Plotting figure and save in csv file from tutorial
import matplotlib.pyplot as plt
import numpy as np

fig, ax, ax2 = mf_ir.plot_ir(w=100, scale=0.956)
ax.set_title(r"IR Spectra of 2-Chloro-3-quinolinecarboxaldehyde" "\n" 
             r"B3LYP/631G+G** with scaling factor 0.956 and Lorentz broadening with $\mathrm{FWHM=100 cm^{-1}}$")
fig.tight_layout()
fig.savefig("IR_C10H6ClNO.svg")
fig.show()






#!/usr/bin/env python
# coding: utf-8

# ---
# title: Practice
# date: "2026-09-26"
# ---
# 
# You will reproduce rsults from the article [ J. Mater. Chem. C, 2016,4, 2931-2935](https://doi.org/10.1039/C5TC03188E). The article contains results from experiments and computations. The molecule investigated is 4-amino-2,2'bipyridine. Perform all our calculations with __B3LYP__ functional and basis set __6-31G**__. See below for graphical abstract.
# 
# <img src = "supp_reference/figure_4.png" width = "300">
# 

# ## Install Packages
# 
# ```python
# ! pip install pyscf
# ! pip install rdkit
# ! pip install geometric
# ```

# In[1]:


# import directories 
from rdkit import Chem
from rdkit.Chem import Draw
from rdkit.Chem import AllChem
from rdkit.Chem.Draw import IPythonConsole
IPythonConsole.drawOptions.addAtomIndices = True


# First, we will generate the 3D structure of the molecule [4-amino-2,2'bipyridine](https://www.chemspider.com/Chemical-Structure.1039202.html), CAS NUMBER: 14151-21-4.

# In[2]:


# 3D format from C10H9N3
smiles = "N1=C(C=C(C=C1)N)C1=NC=CC=C1"
mol = Chem.MolFromSmiles(smiles)
mol = Chem.AddHs(mol)
Chem.AllChem.EmbedMolecule(mol)
Chem.AllChem.MolToXYZFile(mol, "C10H9N3.xyz")
mol


# Now, we optimize the structure in gas phase (not solvent effect) and run frequency calculations to confirm convergence.

# In[2]:


# Geometry Optimization
from pyscf import gto, scf
from pyscf.geomopt.geometric_solver import optimize

# Create the pyscf molecule
mol = gto.M(atom="C10H9N3.xyz")

mol.basis = "6-31+G**"

# set the functional
mf = mol.KS()
mf.xc = 'b3lyp'
mf.disp = 'd3bj'

# Run optimization calculations
mol_eq = optimize(mf)
mol_eq


# In[3]:


conv_params = {
    'convergence_energy': 1e-6, # Eh
    'convergence_grms': 3e-4,   # Eh/Bohr
    'convergence_gmax': 4.5e-4, # Eh/Bohr
    'convergence_drms': 1.2e-3, # Angstrom
    'convergence_dmax': 1.8e-3, # Angstrom
}

mol_eq = optimize(mf, **conv_params)


# In[4]:


# save the optimized geometry for visualization
mol_eq.tofile("opt_C10H9N3.xyz")


# In[4]:


# SCF Energy
from pyscf import gto, scf

mol = gto.M(atom="opt_C10H9N3.xyz")

# set basis set
mol.basis = "6-31+G**"

# set the functional
mf = mol.KS()
mf.xc = 'b3lyp'
mf.disp = 'd3bj'

# Run energy calculations
neutral_energy = mf.kernel()


# Create the MOs (Moelcular Orbitals) and compare your results with figure S10 in the SI.

# In[5]:


# total number of electrons
n = mol.tot_electrons()
n


# In[6]:


# display all orbitals
mf.mo_energy


# In[7]:


# HOMO is n/2 orbital. But python index starts from 0
homo = mf.mo_energy[int(n/2) - 1]
homo


# In[8]:


# The unit of energy is Hartree. To convert to eV
homo * 27.2114


# In[9]:


# import the definitions
from pyscf.tools import molden

# We will write the surface to molden files
with open('C10H9N3.molden', 'w') as f1:
    molden.header(mol, f1)
    molden.orbital_coeff(mol, f1, mf.mo_coeff, ene=mf.mo_energy, occ=mf.mo_occ)


# Next, run calculations for charged system.

# In[ ]:


# Run single-point energy for cation of C10H9N3

from pyscf import gto, scf

mol = gto.M(atom="opt_C10H9N3.xyz")

# set basis set
mol.basis = "6-31+G**"

###### SET CHARGE############
# Set charge
mol.charge = 1
mol.spin = 1 # (2*s) where s is the psin. Some code use 2*s + 1
############################

# set the functional
mf = mol.KS()
mf.xc = 'b3lyp'
mf.disp = 'd3bj'

# Run energy calculations
cation_energy = mf.kernel()


# Now that we have total energy of neutral molecule and cationic molecule, we can compute ionization energy.

# In[12]:


# Ionization is the difference in energies
# we convert to eV

(neutral_energy - cation_energy) * 27.2114


# Next, we run frequency to check that the forces (first derivatives) are near zero (stationary point is minimum) or saddle point. A mimimum has no imaginary frequencies and a saddle point has at least one. A structure that fails and can not be used for TD-DFT or other properties.

# In[1]:


# Frequency
from pyscf import gto, scf

# create a molecule object
mol = gto.M(atom = "opt_C10H9N3.xyz")

# set the basis set
mol.basis = '6-31+G**'

# set the functional
mf = mol.KS()
mf.xc = 'b3lyp'

# run frequency calculation
mf.run()
hessian = mf.Hessian().kernel()


# In[3]:


# compute frequency
from pyscf.hessian import thermo

# getting the frequency data from the calculation
freq_info = thermo.harmonic_analysis(mf.mol, hessian)
freq_info["freq_wavenumber"]


# To compare absorption spectrum in Figure S11 of the SI, run TDDFT calculations in chloroform with the optimized structure.

# In[5]:


# Import package
from pyscf import gto, scf, dft, tddft

mol = gto.M(atom="opt_C10H9N3.xyz")

# set basis set
mol.basis = "6-31+G**"

# Set DFT functional
mf = dft.RKS(mol)
mf.xc = 'b3lyp'
mf.disp = 'd3bj'

# initialize the mf object in solvent
mf = mf.DDCOSMO()
mf.with_solvent.eps = 4.8069 # chloroform
mf = mf.run()

# setup TDDFT
td = tddft.TDDFT(mf)

# set type and number of states required
td.singlet = True

# run TDDFT
td.kernel()

# Analyze to show a table of excitations
td.analyze()


# In[6]:


# Plot spectrum
def plot_absorption(td_obj, step = 0.01, sigma = 0.05):
    import scipy.constants as cst
    import numpy as np
    from scipy.stats import norm
    import matplotlib.pyplot as plt

    # get transition can convert to eV
    transitions = td_obj.e * 27.2114

    # get oscilator strengths
    f = td_obj.oscillator_strength()

    # get minimum and miximum x - value for plot
    minval = min([val for val in transitions]) - 5.0 * sigma
    maxval = max([val for val in transitions]) + 5.0 * sigma

    # number of data points in line
    npts = int((maxval - minval) / step) + 1

    # generating the plot
    eneval = np.linspace(minval, maxval, npts)
    lambdaval = [cst.h * cst.c / (val * cst.e) * 1.e9
                for val in eneval] # in nm

    # sum of gaussian functiona
    spectra = np.zeros(npts)
    for i in range(len(transitions)):
        spectra += f[i] * norm.pdf(eneval, transitions[i], sigma)
    spectra /= spectra.max()

    # plot the spectrum
    plt.plot(lambdaval, spectra, linestyle="--", label ="Simulation")
    plt.xlabel("wavelength (nm)")
    plt.ylabel("Absorption (au)")
    plt.legend()
    plt.savefig("C10H9N3.svg", bbox_inches="tight")

    # save CSV file
    np.savetxt("C10H9N3.csv", np.column_stack((lambdaval, spectra)), 
               delimiter = ",", header = "lambda, Intensity", comments="")

# Plot the absorption from td
plot_absorption(td)


# In[ ]:





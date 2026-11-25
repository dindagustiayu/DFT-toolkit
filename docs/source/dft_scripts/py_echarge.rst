calculate ionization
========

This page contains a Python script to calculate the total electronic energies of a molecular system in three charge states (neutal, cationic, and anionic. 

.. note::

   This script require the optimized geometry file (in XYZ format). It perfoms SCF calculation for each charge state with the appropiate total charge and spin multiplicity. The vertical ionization potential and the vertical electron affinity are then evaluated from the energy differences between the charged and neutral species. 

Neutral energy
-------------------

.. code-block:: python

    #!/usr/bin/env python
    # coding: utf-8
    # edit by materials@dindagustiayu.com

    # import directories 
    from pyscf import gto, scf
    
    # create a molecule object
    mol = gto.M(atom = "opt_mol.xyz")
    
    # set the basis set
    mol.basis = '-----'
    
    # set the functional
    mf = mol.KS()
    mf.xc = '-----'

    # neutral energy
    neutral_energy = mf.kernel()


Cation energy
-----------------

.. code-block:: python

    #!/usr/bin/env python
    # coding: utf-8

    # import directories 
    from pyscf import gto, scf
    
    # create a molecule object
    mol = gto.M(atom = "opt_mol.xyz")

    # set the basis set
    mol.basis = '-----'
    
    ######## SET CHARGE #########
    # Set charge
    mol.charge = 1
    mol.spin = 1 # (2*s) where s is the psin. Some code use 2*s + 1
    ############################

    # set the functional
    mf = mol.KS()
    mf.xc = '-----'

    # cation energy
    cation_energy = mf.kernel()

    # Ionization is the difference in energies
    # we convert to eV

    (neutral_energy - cation_energy) * 27.2114


For example the neutral energy, cation energy, and ionization potential output of 2-Chloro-3-quinolinecarboxaldehyde molecule calculated by b3lyp/6-31+g** DFT:

.. rst-class:: script-out

  .. code-block:: text

       Neutral energy = -963.331275090339
       Cation energy = -963.074757349395 
       Ionization potential = -6.9802068559233215
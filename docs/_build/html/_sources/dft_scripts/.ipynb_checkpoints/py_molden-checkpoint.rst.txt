molden.py
===========

This page contains a Python script to calculate molecular orbitals and identify the HOMO and LUMO. 

.. note::

   This script require the optimized geometry file (in XYZ format). It perfoms SCF calculation, determines the orbital energies and occupations, and locates teh frontier orbitals from the occupied-virtual boundary. The orbitals can be exported for visualizations.


.. code-block:: python

    #!/usr/bin/env python
    # coding: utf-8
    # edit by dindagustiayuedu@gmail.com

    # import directories 
    from pyscf import gto, scf
    from pyscf.tools import molden
    
    # create a molecule object
    mol = gto.M(atom = "opt_mol.xyz")
    
    # set the basis set
    mol.basis = '-----'
    
    # set the functional
    mf = mol.KS()
    mf.xc = '-----'

    # total number of electrons
    n = mol.tot_electrons()
    n

    # HOMO is n/2 orbital. But python index starts from 0
    homo = mf.mo_energy[int(n/2) - 1]
    
    # The unit of energy is Hartree. To convert to eV
    homo * 27.2114
    homo

    # display all orbitals
    mf.mo_energy
   
    # We can export the mos into molden file
    with open('mol.molden', 'w') as f1:
        molden.header(mol, f1)
        molden.orbital_coeff(mol, f1, mf.mo_coeff, ene=mf.mo_energy, occ=mf.mo_occ)


For example the calculated HOMO, LUMO energies and HOMO-LUMO energy gap for 2-Chloro-3-quinolinecarboxaldehyde obtained by b3lyp/6+31+g** method.


.. csv-table:: 
   :file: /data/total_energy.csv
   :header-rows: 0
   :align: center
   :widths: auto



.. only:: html

  .. container:: sphx-glr-footer sphx-glr-footer-gallery

    .. container:: sphx-glr-download sphx-glr-download-csv

      :download:`Download output file: total_energy_C10H6ClNO.csv</data/total_energy.csv>`


compute .fchk file
====================

This page contains a Python script to construct local symmetry coordinates and describe its internal motions.


.. note::

   This script require the vibrational frequency results **(normal modes or Hessian)**. It sets up the tranformation matrix between Cartesian displacements and local symmetry coordinates, which are constructed from the internal coodinates (bond stretches, angle bends, and torsion) of the bonded atoms.


locsymt.py
--------------

.. code-block:: python

    #!/usr/bin/env python
    # coding: utf-8
    # edit by materials@dindagustiayu.com

    # Set 3N X 3N matrix
    import numpy as np
    
    N_atom = mol.natm
    H_matrix = hessian.transpose(0, 2, 1, 3).reshape(3*N_atom, 3*N_atom)
    force_const = H_matrix[np.tril_indices(3 * N_atom)]
    
    # Compute fchk file
    Z = [mol.atom_charge(i) for i in range(N_atom)]
    coords = mol.atom_coords().flatten()
    mass = mol.atom_mass_list()
    
    # set block for analysis
    def block(f, name, type, data):
        f.write(f"{name: <40} {type} N={len(data):12d}\n")
        n = 6 if type == 'I' else 5
        for i in range(0, len(data), n):
            row = data[i:i+n]
            f.write("".join(f"{x:12d}" if type == 'I' else f"{x:16.8E}" for x in row) + "\n")
    
    with open("freq_mol.fchk", "w") as f:
        f.write("Hessian calculation \n")
        f.write("Frequency B3LYP/6-31+G** \n")
        f.write(f"{'Number of atoms':<40} I {N_atom: 12d} \n")
        f.write(f"{'Charge':<40} I  {mol.charge:12d} \n")
        f.write(f"{'Multiplicity': <40} I {mol.spin + 1:12d} \n")
        block(f, "Atomic numbers", 'I', Z)
        block(f, "Current cartesian coordinates", 'R', coords)
        block(f, "Real atomic weights", 'R', mass)
        block(f, "Cartesian Force Constants", 'R', force_const)



For example Definition of Local Symmetry Coordinates of 2-Chloro-3-quinolinecarboxaldehyde calculated by b3lyp/6-31+g**** density functional calculations:



.. csv-table:: 
   :file: /data/locsymt_C10H6ClNO.csv
   :header-rows: 0
   :align: center
   :widths: auto


| **Abbreviations**: ν, stretching; β, in plane bending; ω, out of plane bending; τ, torsion. 
| *a These symbols are used for description of the normal modes by PED.
| *b The internal coordinates.

|

.. only:: html

  .. container:: sphx-glr-footer sphx-glr-footer-gallery

   .. container:: sphx-glr-download sphx-glr-download-csv

      :download:`Download inter-coordinates file: locsymt_C10H6ClNO.csv </data/locsymt_C10H6ClNO.csv>`



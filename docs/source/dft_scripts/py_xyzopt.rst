xyzopt.py
============

This page contains a Python script to optimize the molecular geometry and save the XYZ coordinates of the molecule in .xyz format. 

.. note::

   This script requires `geomeTRIC <https://geometric.readthedocs.io/en/latest/>`_ Python library to update the nuclear coordinates in translation-rotation internal coordinates (TRIC) until the convergence criteria for energy change, gradient and atomic displacement successive steps all fall below prescribed convergence threshold (small enough).


.. code-block:: python

  #!/usr/bin/env python
  # coding: utf-8
  # edit by materials@dindagustiayu.com

  # import directories 
  from pyscf import gto, scf
  from pyscf.geomopt.geometric_solver import optimize
    
  # Create the pyscf molecule
  mol = gto.M(atom="mol.xyz")
                
  mol.basis = "------"
    
  # set the functional
  mf = mol.KS()
  mf.xc = '-----'
    
  # Run optimization calculations
  conv_params = {
  'convergence_energy': 1e-6, # Eh
      'convergence_grms': 3e-4,   # Eh/Bohr
      'convergence_gmax': 4.5e-4, # Eh/Bohr
      'convergence_drms': 1.2e-3, # Angstrom
      'convergence_dmax': 1.8e-3, # Angstrom
  }

  mol_eq = optimize(mf, **conv_params)

  # save the optimized geometry in XYZ format
  mol_eq.tofile("opt_mol.xyz")

For example the optimize file OF 2-Chloro-3-quinolinecarboxaldehyde molecule calculated by b3lyp/6-31+g** DFT:

.. code-block:: text

    19
    XYZ from PySCF
    C          -2.79727423       -0.74451918       -0.31643288
    C          -2.97686748        0.63143861        0.04147588
    C          -1.88063394        1.44383712        0.30498036
    C          -0.54827654        0.90755930        0.21995327
    C          -0.36399380       -0.48057952       -0.14105912
    C          -1.52377802       -1.29030275       -0.40660351
    C           0.98148255       -0.98040700       -0.21561828
    C           2.06423627       -0.14594043        0.05304040
    C           1.75376367        1.22769051        0.40441916
    N           0.53521001        1.79609019        0.50301820
    Cl          3.14667558        2.35131815        0.76317674
    C           3.49343981       -0.69001813       -0.02940198
    O           3.75467180       -1.88082294       -0.33199483
    H          -3.67959239       -1.36672372       -0.51988426
    H          -3.99422681        1.04170253        0.10653421
    H          -1.99842190        2.50068966        0.58075164
    H          -1.38086469       -2.34481108       -0.68064679
    H           1.17554678       -2.03051904       -0.48611291
    H           4.27682010        0.07879290        0.20673122


.. container:: download-box

   `Download optimization file: opt_C10H6ClNO.xyz </data/opt_C10H6ClNO.xyz>`_

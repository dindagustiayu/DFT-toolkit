ksscf.py
==========

This page contains a Python script to calculate self-consistent field (SCF) energy based on Kohn-Sham density functional theory (KS-DFT).

.. note::

   This script requires `PySCF <https://pyscf.org/user/index.html>`_ Python library. Input file in XYZ format, and solve electronic structure problem until convergegence is reached. The result is the total electronic energy.


.. code-block:: Python

        #!/usr/bin/env python
        # coding: utf-8
        # edit by materials@dindagustiayu.com
    
        # import directories 
        from pyscf import gto, scf
        
        # Create the pyscf molecule
        mol = gto.M(atom="mol.xyz")
    
        # Setting the basis set
        mol.basis = "#####"
        
        # set the functional
        mf = mol.KS()
        mf.xc = '#####'
        mf.kernel()


For example the SCF energy of 2-Chloro-3-quinolinecarboxaldehyde molecule calculated by b3lyp/6-31+g** DFT:


.. rst-class:: script-out

  .. code-block:: text

      converged SCF energy = -963.284517771947

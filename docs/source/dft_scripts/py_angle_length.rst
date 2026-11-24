calculate interatomic distance
========

This page contains a Python script to measure the bond lengths and bond angles of a molecule from its optimized XYZ geometry using RDKit.

.. note::

   This script requires `RDKit transforms module <https://www.rdkit.org/docs/source/rdkit.Chem.rdMolTransforms.html>`_ Python library. It assigns the bonding connectivity from the atomic coordinates, and evaluate the interatomic distances (bond lengths, in angstrom) and the angles by three bonded atoms (bond angles, in degrees).


.. code_block:: python

    #!/usr/bin/env python
    # coding: utf-8
    # edit by materials@dindagustiayu.com

    # Import package
    from rdkit.Chem import rdMolTransforms as T
    
    rd = Chem.MolFromXYZFile("opt_mol.xyz")  

    # Note: python index starts from 0!
    # calculates the angle
    conf = rd.GetConformer()                         
    T.GetBondLength(conf, 2, 1) # example
 
    # calculates the angle
    conf = rd.GetConformer()                         
    T.GetAngleDeg(conf, 1, 2, 3) # example


For example the optimized geometrical parameters of 2-Chloro-3-quinolinecarboxaldehyde molecule:

.. csv-table:: Bond Lengths and Angles
   :file: data/bond_data.csv
   :header-rows: 2
   :align: center


.. container:: center-btn

   :download: `Download bond data file: geom_C10H6ClNO.csv <data/geom_C10H6ClNO.csv>`_
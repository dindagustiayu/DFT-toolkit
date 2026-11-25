calculate interatomic distance
=====================================

This page contains a Python script to measure the bond lengths and bond angles of a molecule from its optimized XYZ geometry using RDKit.

.. note::

   This script requires `RDKit transforms module <https://www.rdkit.org/docs/source/rdkit.Chem.rdMolTransforms.html>`_ Python library. It assigns the bonding connectivity from the atomic coordinates, and evaluate the interatomic distances (bond lengths, in angstrom) and the angles by three bonded atoms (bond angles, in degrees).


.. code-block:: python

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


For example the Optimized geometrical parameters of 2-Chloro-3-quinolinecarboxaldehyde obtained by B3LYP/6-31+G** densitity functional calculations

.. csv-table:: 
   :file: /data/geom_C10H6ClNO.csv
   :header-rows: 0
   :align: center


| **Abbreviations**: 
| a For numbering of atoms refer to `figure. 1(a) </_static/C10H6ClNO.svg>`__
| b See Ref. ,"(Spectrochimica Acta Part A: Molecular and Biomolecular Spectroscopy, 2015, 148, 163-174)


.. only:: html

  .. container:: sphx-glr-footer sphx-glr-footer-gallery

    .. container:: sphx-glr-download sphx-glr-download-csv

      :download:`Download output file: geom_C10H6ClNO.csv </data/geom_C10H6ClNO.csv>`


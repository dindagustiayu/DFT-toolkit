xyzOPT.py
========

This page contains a Python script to create a 3D format structure of molecule for quantum chemistry calculation.

.. code_block:: python

    #!/usr/bin/env python
    # coding: utf-8

    # import directories 
    from rdkit import Chem
    from rdkit.Chem import Draw
    from rdkit.Chem import AllChem
    from rdkit.Chem.Draw import IPythonConsole
    IPythonConsole.drawOptions.addAtomIndices = True


    # 3D format from molecule
    smiles = "YOUR-SMILES-MOLECULE-"
    mol = Chem.MolFromSmiles(smiles)
    mol = Chem.AddHs(mol)
    Chem.AllChem.EmbedMolecule(mol)
    Chem.AllChem.MolToXYZFile(mol, "mol.xyz")
    mol

.. figure: _static/C10H6ClNO.svg
   :align: center
   :alt: Example molecule output of 2-Chloro-3-quinolinecarboxaldehyde along with numbering of atom.

.. container:: center-btn

   :download: `Download output file: C10H6ClNO.xyz <ETKDG_alg/C10H6ClNO.xyz>`

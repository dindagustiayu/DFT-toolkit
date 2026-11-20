xyz3d.py
========

This page contains a Python script to create a 3D format structure of molecule for quantum chemistry calculation.

.. code_block:: python

    #!/usr/bin/env python
    # coding: utf-8
    # edit by materials@dindagustiayu.com

    # import directories 
    from rdkit import Chem
    from rdkit.Chem import Draw
    from rdkit.Chem import AllChem
    from rdkit.Chem.Draw import IPythonConsole
    IPythonConsole.drawOptions.addAtomIndices = True


    # 3D format from molecule
    smiles = "YOUR-SMILES-MOLECULE"
    mol = Chem.MolFromSmiles(smiles)
    mol = Chem.AddHs(mol)
    Chem.AllChem.EmbedMolecule(mol)
    Chem.AllChem.MolToXYZFile(mol, "mol.xyz")
    mol


For example the file for 2-Chloro-3-quinolinecarboxaldehyde molecule:

.. figure: _static/C10H6ClNO.svg
   :align: center
   :alt: Example molecule output of 2-Chloro-3-quinolinecarboxaldehyde along with numbering of atom.


.. code-block:: text

    19
    
    C     -2.756536   -0.737201   -0.311816
    C     -2.921569    0.588703    0.032300
    C     -1.839979    1.409503    0.295401
    C     -0.551377    0.875991    0.208638
    C     -0.362251   -0.456235   -0.136134
    C     -1.464332   -1.221206   -0.385316
    C      0.938860   -0.919523   -0.203773
    C      2.018995   -0.102111    0.058368
    C      1.780857    1.222321    0.399002
    N      0.510083    1.651600    0.458918
    Cl     3.154446    2.257505    0.731219
    C      3.379265   -0.607402   -0.017893
    O      3.560270   -1.831841   -0.334489
    H     -3.593256   -1.401739   -0.523175
    H     -3.921171    1.004553    0.100134
    H     -1.935858    2.453428    0.567776
    H     -1.293766   -2.266024   -0.654758
    H      1.091371   -1.969854   -0.475451
    H      4.205949    0.049532    0.191047


.. container:: center-btn

   :download: `Download output file: C10H6ClNO.xyz <ETKDG_alg/C10H6ClNO.xyz>`

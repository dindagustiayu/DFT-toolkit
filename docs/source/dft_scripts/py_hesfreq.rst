hesfreq.py
========

This page contains a Python script to calculate vibrational frequency (a stationary point) of a molecular system on the potential energy surface. 

.. important::

   Check that the forces (first derivatives) are near zero (stationary point is minimum). A mimimum has no imaginary frequencies and a saddle point has at least one.


.. code_block:: python

    #!/usr/bin/env python
    # coding: utf-8
    # edit by materials@dindagustiayu.com

    # import directories 
    from pyscf import gto, scf
    from pyscf.hessian import thermo
    
    # create a molecule object
    mol = gto.M(atom = "opt_mol.xyz")
    
    # set the basis set
    mol.basis = '-----'
    
    # set the functional
    mf = mol.KS()
    mf.xc = '-----'
    
    # run frequency calculation
    mf.run()
    hessian = mf.Hessian().kernel()

    # getting the frequency data from the calculation
    freq_info = thermo.harmonic_analysis(mf.mol, hessian)
    freq_info["freq_wavenumber"]


For example the vibrational frequency output of 2-Chloro-3-quinolinecarboxaldehyde molecule calculated by b3lyp/6-31+g** DFT:

.. code-block:: text

    array([  79.90830344,  103.28997959,  140.65498088,  156.24598564,
            214.20037622,  256.58073811,  304.29246766,  352.85442613,
            367.39409411,  415.38440706,  483.81051658,  491.59736461,
            545.53652096,  595.37123   ,  615.62959134,  647.63437088,
            679.03339557,  765.10634878,  797.00372565,  803.4076228 ,
            837.3823609 ,  919.53793303,  939.16583116,  946.05316954,
            998.70804951, 1030.16975861, 1055.69633537, 1081.95866429,
           1094.39900199, 1180.91665989, 1208.8662733 , 1213.13415083,
           1259.69973392, 1301.5737718 , 1367.11453933, 1375.94599304,
           1417.5028449 , 1438.05890277, 1481.68131913, 1551.676353  ,
           1596.05128515, 1643.73546933, 1687.49354182, 1741.12293024,
           1787.03499914, 3234.47254638, 3440.75859809, 3449.59297516,
           3458.70594863, 3470.05523171, 3478.43246007])


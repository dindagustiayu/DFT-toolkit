Simulated FT-IR spectra
========

This page contains a Python script to calculate the harmonic frequencies and IR intensities for FT-IR simulation. 


.. important::

   This script requires the `pyscf properties <https://github.com/pyscf/properties/tree/master>`_.


script
----------

.. code_block:: python

    #!/usr/bin/env python
    # coding: utf-8
    # edit by dindagustiayuedu@gmail.com

    # Import packages
    from pyscf import gto, dft
    from pyscf.prop import infrared
    from pyscf.hessian import thermo
    
    # Create the pyscf molecule
    mol = gto.M(atom ="opt_mol.xyz")
    
    mol.basis = "-----"
    
    # set the functional
    mf = dft.RKS(mol, xc = "----").run()
    
    # Run infrared calculation, invokes hessian, though calling hessian
    mf_ir = infrared.rks.Infrared(mf).run()
    mf_ir.summary()
    
    # To perform thermo calculation, use the hessian object inside mf_ir
    thermo.dump_thermo(mol, thermo.thermo(mf, mf_ir.vib_dict["freq_au"], 298.15, 101325))
    
    # Plotting figure and save in csv file from tutorial
    import matplotlib.pyplot as plt
    import numpy as np
    
    fig, ax, ax2 = mf_ir.plot_ir(w=100, scale=0.956)
    ax.set_title(r"IR Spectra of molecule scaled" "\n" 
                 r"B3LYP/631G+G** with scaling factor 0.956 and Lorentz broadening with $\mathrm{FWHM=100 cm^{-1}}$")
    fig.tight_layout()
    fig.savefig("ftir_simulation.svg")
    fig.show()
    

For example simulated FT-IR spectra of 2-Chloro-3-quinolinecarboxaldehyde molecule obtained by b3lyp/6-31+g** dft calculation:

.. figure:: _static/ir_C10H6ClNO.svg
   :align: center




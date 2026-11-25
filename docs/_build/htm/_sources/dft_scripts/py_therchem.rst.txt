calculate thermodynamics
===========================

This page contains a Python script to calculate the thermodynamic properties using the RRHO and ideal gas approximations.


.. note::

   This script requires the vibrational frequency results (harmonic frequency or Hessian) and performs thermochemistry properties: heat capacity at **constant volume (Cv), and constant pressure (Cp), internal energy (U), entalphy (H), entrophy (S), and Gibbs free energy (G)**. 


therchem.py
--------------

.. code_block:: python

    #!/usr/bin/env python
    # coding: utf-8
    # edit by dindagustiayuedu@gmail.com

    # Run Thermodynamic properties
    from pyscf import gto, dft
    from pyscf.prop import infrared
    from pyscf.hessian import thermo
    
    # Create the pyscf molecule
    mol = gto.M(atom ="opt_C10H6ClNO.xyz")
                
    mol.basis = "-----"
    
    # set the functional
    mf = dft.RKS(mol, xc = "-----").run()
    
    # Run infrared calculation, invokes hessian, though calling hessian
    mf_ir = infrared.rks.Infrared(mf).run()
    
    # Temperature and Pressure
    T = [100, ...,...]
    P = 101325 # 1 atm in Pa
    
    # Results
    thermo_results = {}
    
    # Run thermo calculation
    for temp in T:
        print(f"Thermodynamic at {temp} K")
        res = thermo.thermo(mf, mf_ir.vib_dict["freq_au"], temp, 101325)
        thermo.dump_thermo(mol, res)
        thermo_results[temp] = res

    

For example the thermodynamic properties of 2-Chloro-3-quinolinecarboxaldehyde molecule obtained by b3lyp/6-31+g** dft calculation:

.. rst-class:: script-out

   .. code-block:: text

        converged SCF energy = -963.33127509007
        Thermodynamic at 100 K
        temperature 100.0000 [K]
        pressure 101325.00 [Pa]
        Rotational constants [GHz] 1.23260 0.48062 0.34579
        Symmetry number 1
        Zero-point energy (ZPE) 0.14011 [Eh]   367861.463 [J/mol]
                                   tot       elec      trans        rot        vib
        Entropy [J/mol/K]       295.040      0.000    151.583    119.129     24.328
        Cv [J/mol/K]             64.474      0.000     12.472     12.472     39.530
        Cp [J/mol/K]             72.788      0.000     20.786     12.472     39.530
        Internal energy [J/mol]                      1247.169   1247.169 369469.346
        Internal energy [Eh]   -963.18960  -963.33128
        Enthalpy [J/mol]                             2078.615   1247.169 369469.346
        Enthalpy [Eh]          -963.18928
        Gibbs free energy [J/mol]                  -13079.708 -10665.726 367036.534
        Gibbs free energy [Eh] -963.20052





.. only:: html

  .. container:: sphx-glr-footer sphx-glr-footer-gallery

    .. container:: sphx-glr-download sphx-glr-download-csv

      :download:`Download Thermodynamic properties data: ther_C10H6ClNO.csv </data/ther_C10H6ClNO.csv>`




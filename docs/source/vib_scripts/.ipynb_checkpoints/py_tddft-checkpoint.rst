TD-DFT
========

This page contains a Python script to calculate the electronic excitation energies using time-dependent density functional theory (TDDFT).


.. note::

   This script requires the `tdscf module <https://pyscf.org/user/tddft.html>`_ (frequency domain), it performs a ground-state Kohn Sham calculation to obtain the occupied and virtual orbitals. The results are reported as vertical excitation energies (in eV), corresponding wavelengths (nm) and oscillator strengths.


tddft.py
----------

.. code-block:: python

    #!/usr/bin/env python
    # coding: utf-8
    # edit by dindagustiayuedu@gmail.com

    # Import package
    from pyscf import gto, scf, dft, tddft
    
    mol = gto.M(atom="opt_mol.xyz")
    
    # set basis set
    mol.basis = "-----"
    
    # Set DFT functional
    mf = dft.RKS(mol)
    mf.xc = '-----'
    
    # initialize the mf object in solvent
    mf = mf.DDCOSMO()
    mf.with_solvent.eps = 4.8069 # example: chloroform
    mf = mf.run()
    
    # setup TDDFT
    td = tddft.TDDFT(mf)
    
    # set type and number of states required
    td.singlet = True
    
    # run TDDFT
    td.kernel()
    
    # Analyze to show a table of excitations
    td.analyze()

    # Plot spectrum
    def plot_absorption(td_obj, step = 0.01, sigma = 0.05):
        import scipy.constants as cst
        import numpy as np
        from scipy.stats import norm
        import matplotlib.pyplot as plt
    
        # get transition can convert to eV
        transitions = td_obj.e * 27.2114
    
        # get oscilator strengths
        f = td_obj.oscillator_strength()
    
        # get minimum and miximum x - value for plot
        minval = min([val for val in transitions]) - 5.0 * sigma
        maxval = max([val for val in transitions]) + 5.0 * sigma
    
        # number of data points in line
        npts = int((maxval - minval) / step) + 1
    
        # generating the plot
        eneval = np.linspace(minval, maxval, npts)
        lambdaval = [cst.h * cst.c / (val * cst.e) * 1.e9
                    for val in eneval] # in nm
    
        # sum of gaussian functiona
        spectra = np.zeros(npts)
        for i in range(len(transitions)):
            spectra += f[i] * norm.pdf(eneval, transitions[i], sigma)
        spectra /= spectra.max()
    
        # plot the spectrum
        plt.plot(lambdaval, spectra, linestyle="--", label ="Simulation")
        plt.xlabel("wavelength (nm)")
        plt.ylabel("Absorption (au)")
        plt.legend()
        plt.savefig("tddft.svg", bbox_inches="tight")

    # Plot the absorption from td
    plot_absorption(td)


For example the UV-visible spectra of 2-Chloro-3-quinolinecarboxaldehyde molecule obtained by b3lyp/6-31+g** dft calculation:

.. rst-class:: script-out

  .. figure:: /_static/tddft_C10H6ClNO.svg
     :align: center

|

Table summary of UV-vis excitation energy and oscillator strength for 2-Chloro-3-quinolinecarboxaldehyde calculated by B3LYP/6-31+G** method.


.. csv-table:: 
   :file: /data/tddft_summary.csv
   :header-rows: 0
   :class: no-header
   :align: center
   :widths: auto


.. only:: html

  .. container:: sphx-glr-footer sphx-glr-footer-gallery

    .. container:: sphx-glr-download sphx-glr-download-csv

      :download:`Download output file: Abs_C10H6ClNO.csv </data/Abs10ns_C10H6ClNO.csv>`



|
|

discussion
--------------

.. figure:: /_static/uv_vis.png
   :align: center
   :alt:
   

   Python packages vs Gaussian software simulations of 2-Chloro-3-quinolinecarboxaldehyde UV-vis spectra.
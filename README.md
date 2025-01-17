run_model.py: This can be used to apply the energy+force computation.  It defaults to using the 'input.xyz' molecule.
              This will compute the energies and forces on that molecule using the trained NN.
              This can then be fed to a molecular dynamics program to adjust coordinates until the system converges.

422 test molecules were held out from training and used in analysis. The respective geometries are defined as:

422_mmff.xyz: a very fast optimization that might be a typical starting point for optimization 
              (the default 'input.xyz' is the first molecule in this set as an example)
422_xd.xyz:   an expensive optmimization (wB97XD) which was the target for the NN training.
422_nn.xyz:   the trained neural-network optimization that converges quite close to the geometries of 422_xd.xyz.

The idea is to take a low level theory (eg mmff) to get a rough optimized geometry, and then progressively pass 
it through the NN using the method of the sample program.  When it converges, the end geometry should approximate 
that of a much higher level of theory at a computation cost comparable to the level theory.


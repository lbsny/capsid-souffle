# virus souffle

## Install and run instructions on BigRed2
* First, git clone the project:
```git clone https://github.com/softmaterialslab/capsid-souffle.git```
* Then, load the required modules using following command:
```module swap PrgEnv-cray PrgEnv-gnu && module load boost/1.65.0 && module load gsl```
* Next, go to the root directory:
 ```cd capsid-souffle```
* Then, install the project:
```make cluster-install```
* Next, submit a test job:
```make cluster-test-submit```
* Then, clean the datafiles from the test job:
```make dataclean```
* Fianlly, submit the job:
```make cluster-submit```
* All outputs from the simulation will be stored in the bin folder when the simulation is completed.
* Check and compare files (ex: energy.out) inside the ```bin/outfiles``` directory; model.parameters.out contains info on the system.
* If you want to clean everything and create a new build, use:
```make clean```

## Install and run instructions on Local computer
* Load the necessary modules:
```module load gsl && module load openmpi/3.0.1 && module load boost/1_67_0```
* Make sure to export BOOST_LIBDIR environment variable with location to the lib directory:
```export BOOST_LIBDIR=/opt/boost/gnu/openmpi_ib/lib/```
* Also make sure to export OMP_NUM_THREADS environment variable with maximum threads available in your CPU:
```export OMP_NUM_THREADS=16```
* Next, go to the root directory:
 ```cd capsid-souffle```
* Then, install the project:
```make all```
* Next, go to the bin directory:
 ```cd bin```
* Next, run a test job:
```time mpirun -np 2 -N 16 ./capsid-souffle -D m -f 41part_c -C 75 -c 200 -s 50 -b 20 -T 100 -t 0.001```
* All outputs from the simulation will be stored in the bin folder when the simulation is completed.
* Check and compare files (ex: energy.out) inside the ```bin/outfiles``` directory; model.parameters.out contains info on the system.
* If you want to clean everything and create a new build, use:
```make clean```

## Aditional information about different input parameter settings

* if testing on a separate folder, copy 41part and/or 41part_c and/or 41part_cu
* run the code for the following set of parameters for nose-hoover controlled md (engine selection, filename, capsomere conc (microM), salt conc (mM), stretching constant (kBT), bending constant (kBT), total time (MD units), timestep (MD units)
```time mpirun -np 1 -N 10 ./capsid-souffle -D m -f 41part -C 931 -c 0 -s 100 -b 20 -T 100 -t 0.002```
* test the results by comparing energies in outfiles/energy.out (column1 is kinetic, col7 is total, col8 is potential)
* To run with electrostatics w/o salt screening, use:
```time mpirun -np 1 -N 10 ./capsid-souffle -D m -f 41part_c -C 75 -c 1 -s 50 -b 20 -T 100 -t 0.001```
* To run with electrostatics w/ moderate salt screening, use:
```time mpirun -np 2 -N 10 ./capsid-souffle -D m -f 41part_c -C 75 -c 200 -s 50 -b 20 -T 100 -t 0.001```
* To run with brownian dynamics w/ moderate salt screening, use:
```time mpirun -np 1 -N 10 ./capsid-souffle -D m -f 41part_c -C 75 -c 200 -s 50 -b 20 -T 100 -t 0.001 -r 1```

## Additional information about changing the number of particles in the simulation

*Currently the simulation is hard coded to 8 particles with constant initial velocities. To change to 27 particles:
1) modify the number of particles on line 108 in md.cpp
2) Uncomment line 307 in initialize.cpp
3) Comment lines 306 & 312 in initialize.cpp 

## Additional information about generating a mass spectrum file

* Mass spectrum file will be generated automatically in outfiles/ms.out, this will contain the number of clusters of each size for all time steps. Equilibrium is identified manually and the ms.out file can be used to generate a histogram for this range.

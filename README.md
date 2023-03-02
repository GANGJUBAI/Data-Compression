**AMP** is a statistical-based median estimation algorithm that is designed to accelerate the preconditioning phase of lossless compression. The goal of AMP is to decrease the total variation of **3D datasets**, increasing the overall compression ratio of floating-point.

# Get Started
## Dataset
| Dataset | Description         | Dimensions    | Type   |
| :-----: | :----------------:  | :--------:    |:------:|
| Miranda |Turbulence simulations | 256x384x384 | double |
| Hurricane ISABEL | Weather simulation | 100x500x500 | float |
| NYX| Hydrodynamics and cosmological simulation | 512x512x512 | float |
| SCALE-LETKF| Climate simulation | 1200x1200x98 | float |
| CESM | Climate simulation | 1800x3600x26 | float |
| astro_pt| Transport simulation | 512x256x640 | double | float |
| wave | Wave propagation simulation | 512x512x512 |d ouble |

The first five datasets can be found at Scientific Data Reduction Benchmarks suite (https://sdrbench.github.io/) and the other can be found at Datasets for Benchmarking Floating-Point Compressors suite (https://dps.uibk.ac.at/~fabian/datasets/)
## Compressor
### 1.FPC

  **FPC** is a fast and effective lossless compressor/decompressor for IEEE 754 64-bit double-precision floating-point data. 
  
  The raw source code can be found at https://userweb.cs.txstate.edu/~burtscher/research/FPC/, and adapted FPC could be found at AMP/src/fpc.h
  
### 2.FPZIP

  **FPZIP** is a library and command-line utility for lossless and optionally lossy compression of 2D and 3D floating-point arrays.
  
  The source code and installation can be found at https://github.com/llnl/fpzip. It should be installed to AMP/Compressor.
### 3.SZ

  **SZ** is error-bounded lossy compressor for HPC data.
  
   Although SZ is not used in paper, the function for reading 3D data is used. The source code and installation can be found at https://github.com/szcompressor/SZ. Similarly， it should be installed to AMP/Compressor.
  
## Set Makefile

Instruction for AMP:

1. Get the scientific applications, loseless compressors (including FPZIP, FPC) at https://sdrbench.github.io/ and https://dps.uibk.ac.at/fabian/datasets/.<br> 
2. Set the compressors and set the Makefile in AMP/src/.<br>
3. Follow the scripts in AMP/src/ for the results of MAC, CR, time overhead, etc.<br>
4. We also provide the python scripts to plot the result figures. 

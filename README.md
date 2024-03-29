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
| wave | Wave propagation simulation | 512x512x512 |double |

The first five datasets can be found at Scientific Data Reduction Benchmarks suite (https://sdrbench.github.io/) and the other can be found at Datasets for Benchmarking Floating-Point Compressors suite (https://dps.uibk.ac.at/~fabian/datasets/)

All datasets should be downloaded to AMP/inputData.
## Compressor
### 1.FPC

  **FPC** is a fast and effective lossless compressor/decompressor for IEEE 754 64-bit double-precision floating-point data. 
  
  The raw source code can be found at https://userweb.cs.txstate.edu/~burtscher/research/FPC/, and adapted FPC could be found at AMP/src/fpc.h
  
### 2.FPZIP

  **FPZIP** is a library and command-line utility for lossless and optionally lossy compression of 2D and 3D floating-point arrays.
  
  The source code and installation can be found at https://github.com/llnl/fpzip. It should be installed to AMP/Compressor.
### 3.SZ

  **SZ** is error-bounded lossy compressor for HPC data.
  
   Although SZ is not used in paper, the function for reading 3D data is used. The source code and installation can be found at https://github.com/szcompressor/SZ. Similarly, it should be installed to AMP/Compressor.
  
## Set Makefile

 1.Open Makefile and modify "to/path" in **Tareget** according to the actual path.
 
 2.AMP can be built using [GNU make](https://www.gnu.org/software/make/):
 ```    
     cd AMP
     make
 ```
 ## Run script
 1. Open all shell script files and modify "to/path" in **Path** according to the actual path.
 
 2. Build a folder **results** to save results. It should be AMP/src/results.
 
 3. Run all shell script files to obtain the results of CR and time overhead.
  ```    
     cd AMP
     sh runCompress.sh
     sh runCompress_float.sh
     sh runapproxMD.sh
     sh runapproxMD_float.sh
     sh runqselect.sh
     sh runqselect_float.sh
     sh runBFPRTrand.sh
     sh runBFPRTrand_float.sh
 ```

 4. If you would like to view the results by figures, we also provide the python scripts. 
 
    Note that you should modify **"nama_hat"** in python files according to the actual path.

## Documentation
More information and experimental results can be found in the following paper:
* Fenfang Li, Huizhang Luo, Junqi Wang, Yida Li, Zhuo Tang, and Kenli Li. AMP: Total Variation Reduction for Lossless Compression via Approximate Median-based Preconditioning [J]. ACM Transactions on Embedded Computing Systems (TEPS). Just Accepted, 2023. 

**If you use AMP in your work, please cite the paper above.**

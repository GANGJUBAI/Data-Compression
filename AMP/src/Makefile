#Author: Fenfang Li
#@Time: 2022/12

GFORTRAN    = gfortran -Wall
CC          = g++ -O3 -g 
#CC          = gcc -O2 -wall
MPI_FORTRAN = mpif90 -Wall
MPI_CC      = mpicc
LD = -lm

.SUFFIXES : .o .c
Target:=Compress Compress_float Compress_approxiMedian Compress_float_approxiMedian  

all: $(Target)


$(Target): %:%.o
	$(CC) $(LD) $< -o $@  -L /to/path/Compressor/SZ/lib/ -lSZ  -L /to/path/Compressor/SZ/lib/ -lzstd -L /to/path/Compressor/SZ/lib -lzlib -lm -L /to/path/Compressor/fpzip/lib/ -lfpzip -L /to/path/Compressor/zfp/lib/ -lzfp -lpthread  -L /to/path/Compressor/ndzip/build/ -lndzip 
%.o : %.c
	$(CC) -c $(*F).c  -I /to/path/Compressor/SZ/sz/include/ -I /to/path/Compressor/zfp/include/ -I /to/path/Compressor/fpzip/include/ 

clean :
	/bin/rm -f *.o $(Target) 


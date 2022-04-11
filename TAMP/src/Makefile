GFORTRAN    = gfortran -Wall
CC          = g++ -O0 -g 
#CC1          = gcc -O2 -Wall
MPI_FORTRAN = mpif90 -Wall
MPI_CC      = mpicc
LD = -lm

.SUFFIXES : .o .c
Target:=Compress Compress_float Compress_TAMP Compress_TAMP_pthreads Compress_MedianOdd Compress_MedianOdd_Pthread Compress_pthreads CompresspFPC Compress_float opt3d opt3d_float opt3d_zordering SPC_test SPC_testfloat SPC_analysic SPC_analysicfloat 

all: $(Target)


$(Target): %:%.o
	$(CC) $(LD) $< -o $@  -L /home/lifenfang/Compressor/SZ/lib/ -lSZ  -L /home/lifenfang/Compressor/SZ/lib/ -lzstd -L /home/lifenfang/Compressor/SZ/lib -lzlib -lm -L /home/lifenfang/Compressor/fpzip/lib/ -lfpzip -L /home/lifenfang/Compressor/zfp/lib/ -lzfp -lpthread
%.o : %.c
	$(CC) -c $(*F).c -I /home/lifenfang/Compressor/SZ/sz/include/ -I /home/lifenfang/Compressor/zfp/include/ -I /home/lifenfang/Compressor/fpzip/include/ 

clean :
	/bin/rm -f *.o $(Target) 


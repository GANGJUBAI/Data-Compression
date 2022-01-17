GFORTRAN    = gfortran -Wall
CC          = g++ -O0 -g 
#CC          = gcc -O2 -wall
MPI_FORTRAN = mpif90 -Wall
MPI_CC      = mpicc
LD = -lm

.SUFFIXES : .o .c
Target:=SPC_analysic SPC_count

all: $(Target)


$(Target): %:%.o
	$(CC) $(LD) $< -o $@  -L /home/lifenfang/Compressor/zfp/lib/ -lzfp  -L /home/lifenfang/Compressor/SZ/lib/ -lSZ -L /home/lifenfang/Compressor/SZ/lib/ -lzstd -L /home/lifenfang/Compressor/SZ/lib -lzlib -lm -L /home/lifenfang/Compressor/fpzip/lib/ -lfpzip 
%.o : %.c
	$(CC) -c $(*F).c -I /home/lifenfang/Compressor/zfp/include/ -I /home/lifenfang/Compressor/SZ/sz/include/ -I /home/lifenfang/Compressor/fpzip/include/

clean :
	/bin/rm -f *.o $(Target) 


GFORTRAN    = gfortran -Wall
CC          = g++ -O0 -g 
#CC          = gcc -O2 -wall
MPI_FORTRAN = mpif90 -Wall
MPI_CC      = mpicc
LD = -lm

.SUFFIXES : .o .c
Target:=SPC_count SPC_count_float Compress_float

all: $(Target)


$(Target): %:%.o
	$(CC) $(LD) $< -o $@   -L /home/lff/Compressor/SZ/lib/ -lSZ  -L /home/lff/Compressor/SZ/lib/ -lzstd -L /home/lff/Compressor/SZ/lib -lzlib -lm  -L /home/lff/Compressor/fpzip/lib/ -lfpzip -L /home/lff/Compressor/zfp/lib/ -lzfp -lpthread  -L /home/lff/Compressor/ndzip/build/ -lndzip
%.o : %.c
	$(CC) -c $(*F).c -I /home/lff/Compressor/SZ/sz/include/ -I /home/lff/Compressor/zfp/include/ -I /home/lff/Compressor/fpzip/include/

clean :
	/bin/rm -f *.o $(Target) 


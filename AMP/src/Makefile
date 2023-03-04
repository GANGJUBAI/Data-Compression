#Author: Fenfang Li
#Time: 2023/3

CPP = g++ -O3 -g 
CPPFLAGS =-fPIC
LDFLAGS =-lstdc++
LD = -lm

LIBS = -L /to/path/Compressor/SZ/lib/ -lSZ  -L /to/path/Compressor/SZ/lib/ -lzstd -L /to/path/Compressor/SZ/lib -lzlib -lm -L /home/lff/Compressor/fpzip/lib/ -lfpzip
INCLUDES = -I /to/path/Compressor/SZ/sz/include/ -I /to/path/Compressor/fpzip/include/


.SUFFIXES : .c .cpp
Target1:=Compress Compress_float Compress_approxiMedian Compress_float_approxiMedian
Target2:=Compress_qselect Compress_float_qselect Compress_BFPRTrand Compress_float_BFPRTrand
Target=$(Target1) $(Target2)

all: $(Target)

$(Target): %:%.o
	@echo "############################  Compile is starting!  ###############################"
	$(CPP) $(LD) $< -o $@ $(LIBS)
	@echo "############################  Compile is completed!  ##############################"
%.o : %.c
	$(CPP) -c $(*F).c  $(INCLUDES) $(CPPFLAGS) $(LDFLAGS)
%.o : %.cpp
	$(CPP) -c $(*F).cpp $(INCLUDES) $(CPPFLAGS) $(LDFLAGS)
clean :
	/bin/rm -f *.o $(Target) 


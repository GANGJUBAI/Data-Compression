


<<COMMENT
./SPC_test ../inputData/Heat3d.dat.b 192 192 192

#density.d64      pressure.d64   velocityy.d64  viscocity.d64 diffusivity.d64  velocityx.d64  velocityz.d64

./SPC_test /home/luo/Benchmark/SDRBENCH-Miranda-256x384x384/density.d64 256 384 384
./SPC_test /home/luo/Benchmark/SDRBENCH-Miranda-256x384x384/pressure.d64 256 384 384
./SPC_test /home/luo/Benchmark/SDRBENCH-Miranda-256x384x384/velocityy.d64 256 384 384
./SPC_test /home/luo/Benchmark/SDRBENCH-Miranda-256x384x384/viscocity.d64 256 384 384
./SPC_test /home/luo/Benchmark/SDRBENCH-Miranda-256x384x384/diffusivity.d64 256 384 384
./SPC_test /home/luo/Benchmark/SDRBENCH-Miranda-256x384x384/velocityx.d64 256 384 384
./SPC_test /home/luo/Benchmark/SDRBENCH-Miranda-256x384x384/velocityz.d64 256 384 384


./SPC_test /home/luo/Benchmark/SDRBENCH-Miranda-256x384x384/density.d64 384 384 256
./SPC_test /home/luo/Benchmark/SDRBENCH-Miranda-256x384x384/pressure.d64 384 384 256
./SPC_test /home/luo/Benchmark/SDRBENCH-Miranda-256x384x384/velocityy.d64 384 384 256
./SPC_test /home/luo/Benchmark/SDRBENCH-Miranda-256x384x384/viscocity.d64 384 384 256
./SPC_test /home/luo/Benchmark/SDRBENCH-Miranda-256x384x384/diffusivity.d64 384 384 256
./SPC_test /home/luo/Benchmark/SDRBENCH-Miranda-256x384x384/velocityx.d64 384 384 256
./SPC_test /home/luo/Benchmark/SDRBENCH-Miranda-256x384x384/velocityz.d64 384 384 256


CLOUDf48.bin.f32         PRECIPf48.bin.f32        QCLOUDf48.log10.bin.f32  QICEf48.bin.f32          QRAINf48.log10.bin.f32   QVAPORf48.bin.f32        Vf48.bin.f32             
CLOUDf48.log10.bin.f32   PRECIPf48.log10.bin.f32  QGRAUPf48.bin.f32        QICEf48.log10.bin.f32    QSNOWf48.bin.f32         TCf48.bin.f32            Wf48.bin.f32             
Pf48.bin.f32             QCLOUDf48.bin.f32        QGRAUPf48.log10.bin.f32  QRAINf48.bin.f32         QSNOWf48.log10.bin.f32   Uf48.bin.f32   

COMMENT
./SPC_testfloat /home/luo/Benchmark/100x500x500/CLOUDf48.bin.f32 500 500 100 
./SPC_testfloat /home/luo/Benchmark/100x500x500/Pf48.bin.f32 500 500 100 
./SPC_testfloat /home/luo/Benchmark/100x500x500/PRECIPf48.bin.f32 500 500 100 
./SPC_testfloat /home/luo/Benchmark/100x500x500/QCLOUDf48.bin.f32 500 500 100 
./SPC_testfloat /home/luo/Benchmark/100x500x500/QGRAUPf48.bin.f32 500 500 100 
./SPC_testfloat /home/luo/Benchmark/100x500x500/QICEf48.bin.f32 500 500 100 
./SPC_testfloat /home/luo/Benchmark/100x500x500/QRAINf48.bin.f32 500 500 100 
./SPC_testfloat /home/luo/Benchmark/100x500x500/QSNOWf48.bin.f32 500 500 100 
./SPC_testfloat /home/luo/Benchmark/100x500x500/QVAPORf48.bin.f32 500 500 100 
./SPC_testfloat /home/luo/Benchmark/100x500x500/TCf48.bin.f32 500 500 100 
./SPC_testfloat /home/luo/Benchmark/100x500x500/Uf48.bin.f32 500 500 100 
./SPC_testfloat /home/luo/Benchmark/100x500x500/Vf48.bin.f32 500 500 100 
./SPC_testfloat /home/luo/Benchmark/100x500x500/Wf48.bin.f32 500 500 100 
./SPC_testfloat /home/luo/Benchmark/100x500x500/CLOUDf48.log10.bin.f32 500 500 100 
./SPC_testfloat /home/luo/Benchmark/100x500x500/PRECIPf48.log10.bin.f32 500 500 100 
./SPC_testfloat /home/luo/Benchmark/100x500x500/QCLOUDf48.log10.bin.f32 500 500 100 
./SPC_testfloat /home/luo/Benchmark/100x500x500/QGRAUPf48.log10.bin.f32 500 500 100 
./SPC_testfloat /home/luo/Benchmark/100x500x500/QICEf48.log10.bin.f32 500 500 100 
./SPC_testfloat /home/luo/Benchmark/100x500x500/QRAINf48.log10.bin.f32 500 500 100 
./SPC_testfloat /home/luo/Benchmark/100x500x500/QSNOWf48.log10.bin.f32 500 500 100 


#baryon_density.dat       dark_matter_density.dat  temperature.dat          template_data.txt        velocity_x.dat           velocity_y.dat           velocity_z.dat

./SPC_testfloat /home/luo/Benchmark/512x512x512/baryon_density.dat 512 512 512
./SPC_testfloat /home/luo/Benchmark/512x512x512/dark_matter_density.dat 512 512 512
./SPC_testfloat /home/luo/Benchmark/512x512x512/temperature.dat 512 512 512
./SPC_testfloat /home/luo/Benchmark/512x512x512/velocity_x.dat 512 512 512
./SPC_testfloat /home/luo/Benchmark/512x512x512/velocity_y.dat 512 512 512
./SPC_testfloat /home/luo/Benchmark/512x512x512/velocity_z.dat 512 512 512



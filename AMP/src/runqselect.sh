#runqselect.sh
#Author: Fenfang Li
#@Time: 2023/3

DataSet1="diffusivity pressure velocityx velocityy velocityz viscocity"
DataSet2="astro_pt wave"

set -- $DataSet1
for i
do
       echo $err
       echo "##########  $i is being compressed  with qselect ##########"

       Path=" /to/path/inputData/Miranda/"$i".d64"
       Source="/to/path/src/results/TCPS/qselect_Compress.result1"
       ./Compress_qselect  $Path 256 384 384 >> $Source

       echo "##########  compress $i is done  ##########"
done
python3 find.py $Source


set -- $DataSet1
for i
do
       echo $err
       echo "##########  $i is being compressed  with qselect ##########"

       Path=" /to/path/inputData/Miranda/"$i".d64"
       Source="/to/path/src/results/TCPS/qselect_Compress.result1"
       ./Compress_qselect  $Path 384 384 256 >> $Source

       echo "##########  compress $i is done  ##########"
done
python3 find.py $Source


echo $err
echo "##########  astro_pt is being compressed  with qselect ##########"

Path="/to/path/inputData/astro_pt.f64"
Source="/to/path/src/results/TCPS/qselect_Compress.result2"
./Compress_qselect $Path 256 512 640 >> $Source

echo "##########  compress astro_pt is done  ##########"
python3 find.py $Source


echo $err
echo "##########  wave is being compressed  with qselect ############"

Path="/to/path/inputData/wave.f64"
Source="/to/path/src/results/TCPS/qselect_Compress.result2"
./Compress_qselect $Path 512 512 512 >> $Source

echo "##########  compress wave is done  #############"
python3 find.py $Source

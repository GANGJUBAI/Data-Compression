#runBFPRTrand_float.sh
#Author: Fenfang Li
#@Time: 2023/3

DataSet1="CLOUDf48 Pf48 PRECIPf48 QCLOUDf48 QGRAUPf48
          QICEf48 QRAINf48 QSNOWf48 QVAPORf48 TCf48
          Uf48 Vf48 Wf48 CLOUDf48_lg PRECIPf48_lg 
          QCLOUDf48_lg QGRAUPf48_lg QICEf48_lg QRAINf48_lg QSNOWf48_lg"

DataSet2="baryon_density dark_matter_density temperature velocity_x velocity_y velocity_z"

DataSet3="PRES-98x1200x1200 QG-98x1200x1200 QR-98x1200x1200 QV-98x1200x1200
        T-98x1200x1200 V-98x1200x1200 QC-98x1200x1200 QI-98x1200x1200
        QS-98x1200x1200 RH-98x1200x1200 U-98x1200x1200 W-98x1200x1200"

DataSet4="CLDICE_1_26_1800_3600 CONCLD_1_26_1800_3600 ICIMR_1_26_1800_3600 Q_1_26_1800_3600 U_1_26_1800_3600
        VU_1_26_1800_3600 CLDLIQ_1_26_1800_3600 DCQ_1_26_1800_3600 ICLDIWP_1_26_1800_3600 QC_1_26_1800_3600
        UU_1_26_1800_3600 VV_1_26_1800_3600 CLOUD_1_26_1800_3600 DTCOND_1_26_1800_3600 ICLDTWP_1_26_1800_3600
        QRL_1_26_1800_3600 V_1_26_1800_3600 Z3_1_26_1800_3600 CMFDQ_1_26_1800_3600 DTV_1_26_1800_3600
        ICWMR_1_26_1800_3600 QRS_1_26_1800_3600 VD01_1_26_1800_3600 CMFDQR_1_26_1800_3600 FICE_1_26_1800_3600
        OMEGA_1_26_1800_3600 RELHUM_1_26_1800_3600 VQ_1_26_1800_3600 CMFDT_1_26_1800_3600 GCLDLWP_1_26_1800_3600
        OMEGAT_1_26_1800_3600 T_1_26_1800_3600 VT_1_26_1800_3600"


set -- $DataSet1
for i
do     
       echo $err 
       echo " ******************** $i is being compressed with BFPRTrand ***********************************"
       
       Path=" /to/path/inputData/Hurricane-ISABEL/100x500x500/"$i".bin.f32" 
       Source="/to/path/src/results/TCPS/BFPRTrand_float.result1"
       ./Compress_float_BFPRTrand $Path 500 500 100 >> $Source

       echo "**************************** compress $i is done *******************************"
done
python3 find.py $Source


set -- $DataSet2
for i
do     
       echo $err 
       echo " ******************** $i is being compressed with BFPRTrand ***********************************"
      
       Path=" /to/path/inputData/EXASKY-NYX/"$i".f32" 
       Source="/to/path/src/results/TCPS/BFPRTrand_float.result2"
       ./Compress_float_BFPRTrand $Path 512 512 512 >> $Source

       echo "**************************** compress $i is done *******************************"
done
python3 find.py $Source 


set -- $DataSet3
for i
do     
       echo $err 
       echo " ******************** $i is being compressed with BFPRTrand ***********************************"
       
       Path=" /to/path/inputData/SCALE/"$i".f32"
       Source="/to/path/src/results/TCPS/BFPRTrand_float.result3"
       ./Compress_float_BFPRTrand $Path 1200 1200 98 >> $Source

       echo "**************************** compress $i is done *******************************"
done
python3 find.py $Source


set -- $DataSet4
for i
do     
       echo $err 
       echo " ******************** $i is being compressed with BFPRTrand ***********************************"
       
       Path=" /to/path/inputData/CESM-ATM/"$i".f32"
       Source="/to/path/src/results/TCPS/BFPRTrand_float.result4"
       ./Compress_float_BFPRTrand $Path 3600 1800 26 >> $Source

       echo "**************************** compress $i is done *******************************"
done
python3 find.py $Source

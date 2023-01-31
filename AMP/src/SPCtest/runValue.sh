#Author: Fenfang Li
#@Time: 2022/12

List="ori temp_h temp_z"


set -- $List
for i
do
        #    echo $err

        echo "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
        Source=$i"_FICE"
        echo $Source
        echo "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"

        python3 value_plot.py $Source 
done


set -- $List
for i
do
        #    echo $err

        echo "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
        Source=$i"_QCLOUD"
        echo $Source
        echo "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"

        python3 value_plot.py $Source
done


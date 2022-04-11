List="ori temp_h temp_z"

set -- $List
for i
do
	#    echo $err

	echo "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
	echo $i
	echo "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"

	python3 value_mac.py $i>>MAC.txt
done

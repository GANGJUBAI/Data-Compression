
sh TAMP.sh >TAMP.result

sh socc_float.sh >socc_float.result


python3 find.py TAMP.result
python3 find.py socc_float.result
python3 CR_plot.py
python3 CR_float_plot.py


sh Compress_TAMP_pthreads.sh >> ./Timeresult/overhead_pTAMP128.result
sh Compress_MedianOdd_Pthreads.sh >> ./Timeresult/overhead_pmedianOdd128.result
sh Compress_pFPC.sh >> ./Timeresult/overhead_pfpc128.result


python3 find.py ./Timeresult/overhead_pTAMP128.result 
python3 find.py ./Timeresult/overhead_pmedianOdd128.result
python3 find.py ./Timeresult/overhead_pfpc128.result

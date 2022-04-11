from pyecharts import options as opts
from pyecharts.charts import Bar,Grid
from pyecharts.render import make_snapshot
from snapshot_phantomjs import snapshot
from pyecharts.globals import ThemeType
import numpy as np

data1 = np.loadtxt("./parallel_result/compress_fuzzyMedian_overhead_server32_data6.result.dat")
pfpc_data1 = np.loadtxt("./parallel_result/overhead_pfpc_pthreads2.result.dat")
pfpc_data2 = np.loadtxt("./parallel_result/overhead_pfpc_pthreads4.result.dat")
pfpc_data3 = np.loadtxt("./parallel_result/overhead_pfpc_pthreads8.result.dat")
pfpc_data4 = np.loadtxt("./parallel_result/overhead_pfpc_pthreads16.result.dat")
pfpc_data5 = np.loadtxt("./parallel_result/overhead_pfpc_pthreads32.result.dat")
pfpc_data6 = np.loadtxt("./parallel_result/overhead_pfpc_pthreads64.result.dat")
pfpc_data7 = np.loadtxt("./parallel_result/overhead_pfpc_pthreads128.result.dat")

fuzzyMedian_data1 = np.loadtxt("./parallel_result/overhead_fuzzyMedian_pthreads2.result.dat")
fuzzyMedian_data2 = np.loadtxt("./parallel_result/overhead_fuzzyMedian_pthreads4.result.dat")
fuzzyMedian_data3 = np.loadtxt("./parallel_result/overhead_fuzzyMedian_pthreads8.result.dat")
fuzzyMedian_data4 = np.loadtxt("./parallel_result/overhead_fuzzyMedian_pthreads16.result.dat")
fuzzyMedian_data5 = np.loadtxt("./parallel_result/overhead_fuzzyMedian_pthreads32.result.dat")
fuzzyMedian_data6 = np.loadtxt("./parallel_result/overhead_fuzzyMedian_pthreads64.result.dat")
fuzzyMedian_data7 = np.loadtxt("./parallel_result/overhead_fuzzyMedian_pthreads128.result.dat")

medianOdd_data1 = np.loadtxt("./parallel_result/overhead_medianOdd_phreads2.result.dat")
medianOdd_data2 = np.loadtxt("./parallel_result/overhead_medianOdd_phreads4.result.dat")
medianOdd_data3 = np.loadtxt("./parallel_result/overhead_medianOdd_phreads8.result.dat")
medianOdd_data4 = np.loadtxt("./parallel_result/overhead_medianOdd_phreads16.result.dat")
medianOdd_data5 = np.loadtxt("./parallel_result/overhead_medianOdd_phreads32.result.dat")
medianOdd_data6 = np.loadtxt("./parallel_result/overhead_medianOdd_phreads64.result.dat")
medianOdd_data7 = np.loadtxt("./parallel_result/overhead_medianOdd_phreads128.result.dat")


data1=data1.reshape(6,-1)

pfpc_data1 = pfpc_data1.reshape(6,-1)
pfpc_data2 = pfpc_data2.reshape(6,-1)
pfpc_data3 = pfpc_data3.reshape(6,-1)
pfpc_data4 = pfpc_data4.reshape(6,-1)
pfpc_data5 = pfpc_data5.reshape(6,-1)
pfpc_data6 = pfpc_data6.reshape(6,-1)
pfpc_data7 = pfpc_data7.reshape(6,-1)

fuzzyMedian_data1 = fuzzyMedian_data1.reshape(6,-1)
fuzzyMedian_data2 = fuzzyMedian_data2.reshape(6,-1)
fuzzyMedian_data3 = fuzzyMedian_data3.reshape(6,-1)
fuzzyMedian_data4 = fuzzyMedian_data4.reshape(6,-1)
fuzzyMedian_data5 = fuzzyMedian_data5.reshape(6,-1)
fuzzyMedian_data6 = fuzzyMedian_data6.reshape(6,-1)
fuzzyMedian_data7 = fuzzyMedian_data7.reshape(6,-1)

medianOdd_data1 = medianOdd_data1.reshape(6,-1)
medianOdd_data2 = medianOdd_data2.reshape(6,-1)
medianOdd_data3 = medianOdd_data3.reshape(6,-1)
medianOdd_data4 = medianOdd_data4.reshape(6,-1)
medianOdd_data5 = medianOdd_data5.reshape(6,-1)
medianOdd_data6 = medianOdd_data6.reshape(6,-1)
medianOdd_data7 = medianOdd_data7.reshape(6,-1)



datalist=["2","4","8","16","32","64","128"]

fuzzyMedianOri_time=[data1[0,0],data1[0,0],data1[0,0],data1[0,0],data1[0,0],data1[0,0],data1[0,0]]

pfpc_time2 = pfpc_data1[0,0]
pfpc_time4 = pfpc_data2[0,0]
pfpc_time8 = pfpc_data3[0,0]
pfpc_time16 = pfpc_data4[0,0]
pfpc_time32 = pfpc_data5[0,0]
pfpc_time64 = pfpc_data6[0,0]
pfpc_time128 = pfpc_data7[0,0]
pfpc_time = [pfpc_time2,pfpc_time4,pfpc_time8,pfpc_time16,pfpc_time32,pfpc_time64,pfpc_time128]

fuzzyMedian_time2 = fuzzyMedian_data1[0,0]
fuzzyMedian_time4 = fuzzyMedian_data2[0,0]
fuzzyMedian_time8 = fuzzyMedian_data3[0,0]
fuzzyMedian_time16 = fuzzyMedian_data4[0,0]
fuzzyMedian_time32 = fuzzyMedian_data5[0,0]
fuzzyMedian_time64 = fuzzyMedian_data6[0,0]
fuzzyMedian_time128 = fuzzyMedian_data7[0,0]
fuzzyMedian_time = [fuzzyMedian_time2,fuzzyMedian_time4,fuzzyMedian_time8,fuzzyMedian_time16,fuzzyMedian_time32,fuzzyMedian_time64,fuzzyMedian_time128]

fuzzyMedian_newCubeTime2 = fuzzyMedian_data1[0,1]
fuzzyMedian_newCubeTime4 = fuzzyMedian_data2[0,1]
fuzzyMedian_newCubeTime8 = fuzzyMedian_data3[0,1]
fuzzyMedian_newCubeTime16 = fuzzyMedian_data4[0,1]
fuzzyMedian_newCubeTime32 = fuzzyMedian_data5[0,1]
fuzzyMedian_newCubeTime64 = fuzzyMedian_data6[0,1]
fuzzyMedian_newCubeTime128 = fuzzyMedian_data7[0,1]
fuzzyMedian_newCubeTime = [fuzzyMedian_newCubeTime2,fuzzyMedian_newCubeTime4,fuzzyMedian_newCubeTime8,fuzzyMedian_newCubeTime16,fuzzyMedian_newCubeTime32,fuzzyMedian_newCubeTime64,fuzzyMedian_newCubeTime128]

fuzzyMedian_compressTime2 = fuzzyMedian_data1[0,2]
fuzzyMedian_compressTime4 = fuzzyMedian_data2[0,2]
fuzzyMedian_compressTime8 = fuzzyMedian_data3[0,2]
fuzzyMedian_compressTime16 = fuzzyMedian_data4[0,2]
fuzzyMedian_compressTime32 = fuzzyMedian_data5[0,2]
fuzzyMedian_compressTime64 = fuzzyMedian_data6[0,2]
fuzzyMedian_compressTime128 = fuzzyMedian_data7[0,2]
fuzzyMedian_compressTime = [fuzzyMedian_compressTime2,fuzzyMedian_compressTime4,fuzzyMedian_compressTime8,fuzzyMedian_compressTime16,fuzzyMedian_compressTime32,fuzzyMedian_compressTime64,fuzzyMedian_compressTime128]

medianOdd_time2 = medianOdd_data1[0,0]
medianOdd_time4 = medianOdd_data2[0,0]
medianOdd_time8 = medianOdd_data3[0,0]
medianOdd_time16 = medianOdd_data4[0,0]
medianOdd_time32 = medianOdd_data5[0,0]
medianOdd_time64 = medianOdd_data6[0,0]
medianOdd_time128 = medianOdd_data7[0,0]
medianOdd_time =[medianOdd_time2,medianOdd_time4,medianOdd_time8,medianOdd_time16,medianOdd_time32,medianOdd_time64,medianOdd_time128]

medianOdd_newCubeTime2 = medianOdd_data1[0,1]
medianOdd_newCubeTime4 = medianOdd_data2[0,1]
medianOdd_newCubeTime8 = medianOdd_data3[0,1]
medianOdd_newCubeTime16 = medianOdd_data4[0,1]
medianOdd_newCubeTime32 = medianOdd_data5[0,1]
medianOdd_newCubeTime64 = medianOdd_data6[0,1]
medianOdd_newCubeTime128 = medianOdd_data7[0,1]
medianOdd_newCubeTime =[medianOdd_newCubeTime2,medianOdd_newCubeTime4,medianOdd_newCubeTime8,medianOdd_newCubeTime16,medianOdd_newCubeTime32,medianOdd_newCubeTime64,medianOdd_newCubeTime128]

medianOdd_compressTime2 = medianOdd_data1[0,2]
medianOdd_compressTime4 = medianOdd_data2[0,2]
medianOdd_compressTime8 = medianOdd_data3[0,2]
medianOdd_compressTime16 = medianOdd_data4[0,2]
medianOdd_compressTime32 = medianOdd_data5[0,2]
medianOdd_compressTime64 = medianOdd_data6[0,2]
medianOdd_compressTime128 = medianOdd_data7[0,2]
medianOdd_compressTime =[medianOdd_compressTime2,medianOdd_compressTime4,medianOdd_compressTime8,medianOdd_compressTime16,medianOdd_compressTime32,medianOdd_compressTime64,medianOdd_compressTime128]


def getBar():
    c=(
      Bar()#init_opts=opts.InitOpts(theme=ThemeType.WALDEN,))
                                 # width='1500px',height='1000px'))
      .add_xaxis(datalist)
      .add_yaxis("PFPC",pfpc_time,category_gap='15%',gap='10%',itemstyle_opts=opts.ItemStyleOpts(color="#c23531"))
      .add_yaxis("AM",fuzzyMedianOri_time,category_gap='15%',gap='10%',itemstyle_opts=opts.ItemStyleOpts(color="#61a0a8"))
      
      .add_yaxis("AM_median",fuzzyMedian_time,category_gap='15%',gap='10%',stack="stack1",itemstyle_opts=opts.ItemStyleOpts(color="#d48265"))
      .add_yaxis("AM_newCube",fuzzyMedian_newCubeTime,category_gap='15%',gap='10%',stack="stack1",itemstyle_opts=opts.ItemStyleOpts(color="#749f83"))
      .add_yaxis("",fuzzyMedian_compressTime,category_gap='15%',gap='10%',stack="stack1",itemstyle_opts=opts.ItemStyleOpts(color="#c23531"))

      .add_yaxis("MedianOdd_median",medianOdd_time,category_gap='15%',gap='10%',stack="stack2",itemstyle_opts=opts.ItemStyleOpts(color="#FFDEAD"))
      .add_yaxis("MedianOdd_newCube",medianOdd_newCubeTime,category_gap='15%',gap='10%',stack="stack2",itemstyle_opts=opts.ItemStyleOpts(color="#2f4554"))
      .add_yaxis("",medianOdd_compressTime,category_gap='15%',gap='10%',stack="stack2",itemstyle_opts=opts.ItemStyleOpts(color="#c23531"))
      
      .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
      .set_global_opts(

         xaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(font_size=20,
                font_family='Times New Roman',font_weight='bolder')),
         yaxis_opts=opts.AxisOpts(name='Time Overhead',
            name_location='middle',
            name_gap=50,
            axislabel_opts=opts.LabelOpts(font_size = 15),
            name_textstyle_opts=opts.TextStyleOpts(
                font_family= 'Times New Roman',
                font_size=20,
                color='black',
                font_weight='bolder',
            )),
         legend_opts=opts.LegendOpts(orient="horizontal",      #"vertical",
                                     pos_top="5%",
                                     pos_right="10%",
                                     textstyle_opts=opts.TextStyleOpts(font_size=14))
          )
      )
    return c
grid = Grid()
grid.add(getBar(),grid_opts=opts.GridOpts(pos_bottom="25%"))
if __name__=="__main__":
    print(getBar().options['color'])
    make_snapshot(snapshot, grid.render(), "./fig/parallel_Scalability_diffusivity.png",is_remove_html=True,pixel_ratio=1.5)

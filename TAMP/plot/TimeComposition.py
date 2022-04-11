from pyecharts import options as opts
from pyecharts.charts import Bar,Grid
from pyecharts.render import make_snapshot
from pyecharts.globals import ThemeType
from snapshot_phantomjs import snapshot
import numpy as np

data1 = np.loadtxt("./Timeresult/overhead_FPC.result.dat")
data2 = np.loadtxt("./Timeresult/overhead_FPC+.result.dat")
data3 = np.loadtxt("./Timeresult/overhead_TAMP.result.dat")


data1=data1.reshape(12,-1)
data2=data2.reshape(12,-1)
data3=data3.reshape(12,-1)


datalist=["diffusivity","pressure","velocityx","velocityy","velocityz","viscocity","diffusivity\'","pressure\'","velocityx\'","velocityy\'","velocityz\'","viscocity\'"]


FPC_time=data1[:,0]
oriMedian_medianTime=data2[:,0]
oriMedian_newCubeTime=data2[:,1]
oriMedian_compressTime=data2[:,2]

approxiMedian_medianTime=data3[:,0]
approxiMedian_newCubeTime=data3[:,1]
approxiMedian_compressTime=data3[:,2]



def getBar():
    c=(
      Bar(init_opts=opts.InitOpts(width='1500px'))#init_opts=opts.InitOpts(theme=ThemeType.LIGHT,
           #                       width='1500px',height='1000px'))
      .add_xaxis(datalist)
      .add_yaxis("FPC",FPC_time.tolist(),category_gap='30%',gap='10%',itemstyle_opts=opts.ItemStyleOpts(color="#2f4554"))
      
      .add_yaxis("",oriMedian_compressTime.tolist(),category_gap='30%',gap='10%',stack="stack1",itemstyle_opts=opts.ItemStyleOpts(color="#2f4554"))
      .add_yaxis("FPC+_precondition",oriMedian_newCubeTime.tolist(),category_gap='30%',gap='10%',stack="stack1",itemstyle_opts=opts.ItemStyleOpts(color="#61a0a8"))
      .add_yaxis("FPC+_construction",oriMedian_medianTime.tolist(),category_gap='30%',gap='10%',stack="stack1",itemstyle_opts=opts.ItemStyleOpts(color="#c23531"))
         
      .add_yaxis("",approxiMedian_compressTime.tolist(),category_gap='30%',gap='10%',stack="stack2",itemstyle_opts=opts.ItemStyleOpts(color="#2f4554")) 
      .add_yaxis("TAMP_precondition",approxiMedian_newCubeTime.tolist(),category_gap='30%',gap='10%',stack="stack2",itemstyle_opts=opts.ItemStyleOpts(color="#749f83")) 
      .add_yaxis("TAMP_construction",approxiMedian_medianTime.tolist(),category_gap='30%',gap='10%',stack="stack2",itemstyle_opts=opts.ItemStyleOpts(color="#d48265")) 
      
     
      .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
      .set_global_opts(

         xaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(rotate=90,font_size=20,
                font_family='Times New Roman',font_weight='bolder')),
         yaxis_opts=opts.AxisOpts(name='Time Overhead(ms)',
            name_location='middle',
            name_gap=50,
            name_textstyle_opts=opts.TextStyleOpts(
                font_family= 'Times New Roman',
                font_size=20,
                color='black',
                font_weight='bolder',
            )),
         legend_opts=opts.LegendOpts(orient="horizontal", #"vertical",
                                     pos_top="0%",
                                     pos_right="5%",
                                     item_gap = 10,
                                     textstyle_opts=opts.TextStyleOpts(font_size=18))
          )
      )
    return c
grid = Grid()
grid.add(getBar(),grid_opts=opts.GridOpts(pos_bottom="25%"))
if __name__=="__main__":
    make_snapshot(snapshot, grid.render(), "./fig/TimeComposition.pdf",is_remove_html=True,pixel_ratio=1.5)

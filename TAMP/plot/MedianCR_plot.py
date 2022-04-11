from pyecharts import options as opts
from pyecharts.charts import Bar,Grid
from pyecharts.render import make_snapshot
from snapshot_phantomjs import snapshot
import numpy as np

data1 = np.loadtxt("compressOri.result.dat")
data2 = np.loadtxt("compress_fuzzyMedian.result.dat")
data1=data1.reshape(12,-1)
data2=data2.reshape(12,-1)

datalist=["diffusivity","pressure","velocityx","velocityy","velocityz","viscocity","diffusivity\'","pressure\'","velocityx\'","velocityy\'","velocityz\'","viscocity\'"]

ori_time=data1[:,0]
ori_CR=data1[:,1]

median_time=data2[:,0]
median_CR=data2[:,1]



def getBar():
    c=(
      Bar(init_opts=opts.InitOpts(height='500px',width=800))
      .add_xaxis(datalist)
      .add_yaxis("FPC+",ori_CR.tolist(),category_gap='30%',gap='10%',label_opts=opts.LabelOpts(is_show=False))
      .add_yaxis("TAMP",median_CR.tolist(),category_gap='30%',gap='5%',label_opts=opts.LabelOpts(is_show=False))
      .set_global_opts(

         xaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(rotate=90,font_size=20,
                font_family='Times New Roman',font_weight='bolder')),
         yaxis_opts=opts.AxisOpts(name='Compress Ratio',
            name_location='middle',
            name_gap=50,
            name_textstyle_opts=opts.TextStyleOpts(
                font_family= 'Times New Roman',
                font_size=20,
                color='black',
                font_weight='bolder',
            )),
         legend_opts=opts.LegendOpts(orient="horizontal", #"vertical",
                                     pos_top="15%",
                                     pos_right="15%",
                                     textstyle_opts=opts.TextStyleOpts(font_size=20))
          )
      )
    return c
grid = Grid()
grid.add(getBar(),grid_opts=opts.GridOpts(pos_bottom="25%"))
if __name__=="__main__":
    make_snapshot(snapshot, grid.render(), "./fig/MedianCR.pdf",is_remove_html=True,pixel_ratio=1.5)

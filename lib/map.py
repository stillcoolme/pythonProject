

from pyecharts.faker import Faker
from pyecharts import options as opts
from pyecharts.charts import Geo
from pyecharts.globals import ChartType, SymbolType

# https://mp.weixin.qq.com/s/6W1hofmsiUBP0innFtCRlQ   使用 pyecharts 绘制交互式动态地图
if __name__ == '__main__':
    c = (
        Geo()
            .add_schema(maptype="china")  # maptype="北京"
            .add("geo", [list(z) for z in zip(Faker.provinces, Faker.values())])
            .set_series_opts(label_opts=opts.LabelOpts(is_show=False))  # 系列配置项，可配置图元样式、文字样式、标签样式、点线样式等
            .set_global_opts( # 全局配置项，可配置标题、动画、坐标轴、图例等
            visualmap_opts=opts.VisualMapOpts(),
            title_opts=opts.TitleOpts(title="Geo-基本示例"),
            )
    )
    # 图表完成制作后通过render()函数输出为html文件，你可以在render()中传递输出地址参数，将html文件保存到自定义的位置。
    c.render()
    # c.render_notebook()  # 显示地图 python notebook
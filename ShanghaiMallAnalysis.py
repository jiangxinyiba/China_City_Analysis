import xlrd
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.basemap import Basemap

# 导入数据
head = "F:\Code\PycharmProjects\小项目\中国城市分布分析\上海_美甲.xls"
xls_file = xlrd.open_workbook(head)
SHMall = xls_file.sheets()[0]
SHMall_Addr_lon = SHMall.col_values(0)   # 经度信息
SHMall_Addr_lat = SHMall.col_values(1)   # 纬度信息
SHMall_cost = SHMall.col_values(2)       # 费用信息
SHMall_district = SHMall.col_values(4)   # 区信息
# 去除表头
SHMall_Addr_lon = SHMall_Addr_lon[1:]
SHMall_Addr_lat = SHMall_Addr_lat[1:]
SHMall_cost     = SHMall_cost[1:]
SHMall_district = SHMall_district[1:]
# 数值信息 str转int
SHMall_Addr_lon = list(map(eval, SHMall_Addr_lon))
SHMall_Addr_lat = list(map(eval, SHMall_Addr_lat))
#SHMall_cost = list(map(eval, SHMall_cost))

# 地图——上海
m = Basemap(projection='merc', llcrnrlat=30, urcrnrlat=32, llcrnrlon=120, urcrnrlon=123) # 实例化一个map
# m = Basemap(llcrnrlon=30, llcrnrlat=35, urcrnrlon=120, urcrnrlat=90, projection='lcc')
#m.drawcoastlines()  # 画海岸线
m.drawcountries()
m.readshapefile("F:\Code\PycharmProjects\小项目\中国城市分布分析\CHN_SHP\gadm36_CHN_3", 'states', drawbounds=True) #中国省份细分

# parallels = np.arange(-90., 90., 10.)  # 这两行画纬度，范围为[-90,90]间隔为10
# m.drawparallels(parallels, labels=[False, True, True, False])
# meridians = np.arange(-180., 180., 20.)  # 这两行画经度，范围为[-180,180]间隔为10
# m.drawmeridians(meridians, labels=[True, False, False, True])

# 根据区绘制不同颜色点
Areas = ['黄浦区','卢湾区','徐汇区','长宁区','静安区','普陀区','闸北区',"虹口区","杨浦区",
         "闵行区","宝山区","嘉定区","浦东新区","金山区","松江区","青浦区","奉贤区","崇明县"]
for ii in range(len(SHMall_Addr_lon)):
    if SHMall_district[ii] == "黄浦区":
        r, g, b = 0, 191, 255
    if SHMall_district[ii] == "卢湾区":
        r, g, b = 70, 130, 188
    if SHMall_district[ii] == "徐汇区":
        r, g, b = 205, 92, 92
    if SHMall_district[ii] == "长宁区":
        r, g, b = 205, 133, 63
    if SHMall_district[ii] == "静安区":
        r, g, b = 245, 22, 179
    if SHMall_district[ii] == "普陀区":
        r, g, b = 221, 160, 221
    if SHMall_district[ii] == "闸北区":
        r, g, b = 135, 200, 250
    if SHMall_district[ii] == "虹口区":
        r, g, b = 132, 112, 255
    if SHMall_district[ii] == "杨浦区":
        r, g, b = 255, 165, 0
    if SHMall_district[ii] == "闵行区":
        r, g, b = 255, 7, 0
    if SHMall_district[ii] == "宝山区":
        r, g, b = 112, 138, 144
    if SHMall_district[ii] == "浦东新区":
        r, g, b = 255, 20, 147
    if SHMall_district[ii] == "金山区":
        r, g, b = 255, 255, 0
    if SHMall_district[ii] == "松江区":
        r, g, b = 107, 142, 35
    if SHMall_district[ii] == "青浦区":
        r, g, b = 0, 100, 0
    if SHMall_district[ii] == "奉贤区":
        r, g, b = 0, 255, 255
    if SHMall_district[ii] == "崇明县":
        r, g, b = 0, 0, 0
    color = [[r/255, g/255, b/255]]
    lon, lat = m(SHMall_Addr_lon[ii], SHMall_Addr_lat[ii])
    m.scatter(lon, lat, s=5, c=color)
plt.show()
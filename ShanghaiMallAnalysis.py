import xlrd
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.basemap import Basemap

import xlwt
import time
import os
import math
from datetime import datetime
from xlrd import xldate_as_tuple
# from xlutils.copy import copy

# 导入数据
head = "F:\Code\PycharmProjects\小项目\中国城市分布分析\上海_商场.xls"
xls_file = xlrd.open_workbook(head)
SHMall = xls_file.sheets()[0]
SHMall_Addr_lon = SHMall.col_values(0)   # 经度信息
SHMall_Addr_lat = SHMall.col_values(1)   # 纬度信息
# 去除表头
SHMall_Addr_lon = SHMall_Addr_lon[1:]
SHMall_Addr_lat = SHMall_Addr_lat[1:]
SHMall_Addr_lon = list(map(eval, SHMall_Addr_lon))
SHMall_Addr_lat = list(map(eval, SHMall_Addr_lat))

# 地图——上海
m = Basemap(projection='merc', llcrnrlat=30, urcrnrlat=35, llcrnrlon=120, urcrnrlon=125) # 实例化一个map
m.drawcoastlines()  # 画海岸线
m.drawcountries()

parallels = np.arange(-90., 90., 10.)  # 这两行画纬度，范围为[-90,90]间隔为10
m.drawparallels(parallels, labels=[False, True, True, False])
meridians = np.arange(-180., 180., 20.)  # 这两行画经度，范围为[-180,180]间隔为10
m.drawmeridians(meridians, labels=[True, False, False, True])

lon, lat = m(SHMall_Addr_lon, SHMall_Addr_lat)
m.scatter(lon, lat, s=10, c="red")
plt.show()
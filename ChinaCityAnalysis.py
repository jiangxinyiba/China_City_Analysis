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
head = "F:\Code\PycharmProjects\小项目\中国城市分布分析\China_City.xlsx"
xls_file = xlrd.open_workbook(head)
ChinaCity = xls_file.sheets()[0]
ChinaCity_name = ChinaCity.col_values(0)   # 中国城市名字
ChinaCity_Addr = ChinaCity.col_values(1)   # 中国经纬度信息
ChinaCity_QuNum = ChinaCity.col_values(2)  # 区号
# 去除表头
ChinaCity_name = ChinaCity_name[1:]
ChinaCity_Addr = ChinaCity_Addr[1:]
ChinaCity_QuNum = ChinaCity_QuNum[1:]

ChinaCity_X = []
ChinaCity_Y = []
ChinaCity_Q = []
color = []
print(ChinaCity_name[0] , ChinaCity_Addr[0])

for i in range(len(ChinaCity_name)):
    Addr = ChinaCity_Addr[i].split(",")
    ChinaCity_X.append(float(Addr[0]))
    ChinaCity_Y.append(float(Addr[1]))
    ChinaCity_Q.append(int(ChinaCity_QuNum[i]))

# ChinaCity_QArray = np.array(ChinaCity_Q)
# ChinaCity_XArray = np.array(ChinaCity_X)
# ChinaCity_YArray = np.array(ChinaCity_Y)
# ChinaCity_XArraysort = ChinaCity_XArray[ChinaCity_QArray.argsort()]
# ChinaCity_YArraysort = ChinaCity_YArray[ChinaCity_QArray.argsort()]
# ChinaCity_QArraysort = ChinaCity_QArray[ChinaCity_QArray.argsort()]
# ChinaCity_Xsort = ChinaCity_XArraysort.tolist()
# ChinaCity_Ysort = ChinaCity_YArraysort.tolist()
# ChinaCity_Qsort = ChinaCity_QArraysort.tolist()

# 随便画一个中国城市分布
m = Basemap(llcrnrlon=77, llcrnrlat=14, urcrnrlon=140, urcrnrlat=51, projection='lcc', lat_1=33, lat_2=45, lon_0=100) # 实例化一个map
m.drawcoastlines()  # 画海岸线
m.drawcountries()
m.readshapefile("F:\Code\PycharmProjects\小项目\中国城市分布分析\CHN_SHP\gadm36_CHN_3", 'states', drawbounds=True) #中国省份细分

parallels = np.arange(-90., 90., 10.)  # 这两行画纬度，范围为[-90,90]间隔为10
m.drawparallels(parallels, labels=[False, True, True, False])
meridians = np.arange(-180., 180., 20.)  # 这两行画经度，范围为[-180,180]间隔为10
m.drawmeridians(meridians, labels=[True, False, False, True])

for ii in range(len(ChinaCity_name)):
    # 根据区号确定颜色
    QNUM = ChinaCity_Q[ii]
    if QNUM<=255 and QNUM>0:
        r, g, b = (255-QNUM)/255, 0, 0
    elif QNUM<=510 and QNUM>255:
        r, g, b = (510-QNUM)/255, 255/255, 0
    elif QNUM<=765 and QNUM>510:
        r, g, b = 0, (QNUM-510)/255, 255/255
    else:
        r, g, b = (QNUM-765)/255, 0, 255 / 255
    color = [[r, g, b]]
    lon, lat = m(ChinaCity_Y[ii], ChinaCity_X[ii])
    m.scatter(lon, lat, s=10, c=color)
plt.show()

# for i in range(len(ChinaCity_name)):
#     # 根据区号确定颜色
#     QNUM = ChinaCity_Q[i]
#     if QNUM<1000 and QNUM>=800:
#         r, g, b = (QNUM-700)/1000, 350/1000, 350/1000
#     elif QNUM<800 and QNUM>=600:
#         r, g, b = (QNUM-500)/800, 250/800, 250/800
#     elif QNUM<600 and QNUM>=400:
#         r, g, b = (QNUM-300)/600, 150/600, 150/600
#     elif QNUM<400 and QNUM>=200:
#         r, g, b = (QNUM-160)/400, 80/400, 80/400
#     elif QNUM<200 and QNUM>=100:
#         r, g, b = (QNUM-80)/200, 40/200, 40/200
#     elif QNUM<100 and QNUM>=50:
#         r, g, b = (QNUM-40)/100, 20/100, 20/100
#     elif QNUM<50 and QNUM>=0:
#         r, g, b = (QNUM-2)/50, 1/50, 1/50
#     # if QNUM == 21:
#     #     r, g, b = 1, 0, 0
#     color = [[r, g, b]]
#
#     lon, lat = m(ChinaCity_Y[i], ChinaCity_X[i])
#     m.scatter(lon, lat, s=10, c=color)
# plt.show()
from geopandas import GeoDataFrame
import shapely
from shapely.geometry import Point
import pandas as pd
import sys

# print ('arcpy'in sys)
df= pd.read_csv('absence_2016.csv')

df.columns=['Date','Point_X','Point_Y','P_A']
GPS= [Point(xy) for xy in zip(df.Point_X,df.Point_Y)]
df= df.drop(['Point_X','Point_Y'],axis=1)

crs= {'init':'epsg:4326'}
geo_df = GeoDataFrame(df, crs=crs, geometry=GPS)
# print geo_df
## 2017 data
# geo_df.to_file('all_2017.shp')
# 2017-02-10
# df20170210 = geo_df[:3]
# df20170210.to_file('data20170210/data20170210.shp')
# df20170217= geo_df[4:6]
# df20170210.to_file('data20170217/data20170217.shp')
# df20170303=geo_df[6:8]
# df20170303.to_file('data20170303/data20170303.shp')
# print df20170303
# df20170306=geo_df[8:10]
# df20170306.to_file('data20170306/data20170306.shp')
# print df20170306
# df20170324=geo_df[10:16]
# df20170324.to_file('data20170324/data20170324.shp')
# print df20170324
# df20170412=geo_df[16:18]
# df20170412.to_file('data20170412/data20170412.shp')
# print df20170412
# df20170503=geo_df[18:23]
# df20170503.to_file('data20170503/data20170503.shp')
# print df20170503
# df20170512=geo_df[23:26]
# df20170512.to_file('data20170512/data20170512.shp')
# print df20170512
# df20170517=geo_df[26:30]
# df20170517.to_file('data20170517/data20170517.shp')
# print df20170517
# df20170518=geo_df[30:34]
# df20170518.to_file('data20170518/data20170518.shp')
# print df20170518

## 2016 data



df20160415= geo_df[:1]
df20160415.to_file("data20160415.shp")
df20160419= geo_df[1:2]
df20160419.to_file("data20160419.shp")
df20160508 = geo_df[2:3]
df20160508.to_file("data20160508.shp")
df20160517= geo_df[3:4]
df20160517.to_file("data20160517.shp")
df20160520 = geo_df[4:5]
df20160520.to_file("data20160520.shp")
df20160524= geo_df[5:6]
df20160524.to_file("data20160524.shp")
df20160612 = geo_df[6:7]
df20160612.to_file("data20160612.shp")
df20160628 = geo_df[7:10]
df20160628.to_file("data20160628.shp")
df20160711=geo_df[10:11]
df20160711.to_file("data20160711.shp")
df20160713=geo_df[11:12]
df20160713.to_file("data20160713.shp")
df20160715=geo_df[12:13]
df20160715.to_file("data20160715.shp")
df20160717=geo_df[13:14]
df20160717.to_file("data20160717.shp")
df20160725=geo_df[14:15]
df20160725.to_file("data20160725.shp")
df20160808=geo_df[15:16]
df20160808.to_file("data20160808.shp")
df20160811=geo_df[16:18]
df20160811.to_file("data20160811.shp")
df20160822=geo_df[18:19]
df20160822.to_file("data20160822.shp")
df20160906=geo_df[19:20]
df20160906.to_file("data20160906.shp")
df20161006=geo_df[20:21]
df20161006.to_file("data20161006.shp")
df20161124=geo_df[21:22]
df20161124.to_file("data20161124.shp")
df20161125=geo_df[22:23]
df20161125.to_file("data20161125.shp")


    # i.to_file(path)
# df20170210.to_file('data20170217/data20170217.shp')
# df20170303=geo_df[6:8]
# df20170303.to_file('data20170303/data20170303.shp')
# print df20170303
# df20170306=geo_df[8:10]
# df20170306.to_file('data20170306/data20170306.shp')
# print df20170306
# df20170324=geo_df[10:16]
# df20170324.to_file('data20170324/data20170324.shp')
# print df20170324
# df20170412=geo_df[16:18]
# df20170412.to_file('data20170412/data20170412.shp')
# print df20170412
# df20170503=geo_df[18:23]
# df20170503.to_file('data20170503/data20170503.shp')
# print df20170503
# df20170512=geo_df[23:26]
# df20170512.to_file('data20170512/data20170512.shp')
# print df20170512
# df20170517=geo_df[26:30]
# df20170517.to_file('data20170517/data20170517.shp')
# print df20170517
# df20170518=geo_df[30:34]
# df20170518.to_file('data20170518/data20170518.shp')
# print df20170518

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import csv

#https://towardsdatascience.com/5-quick-and-easy-data-visualizations-in-python-with-code-a2284bae952f
#https://www.kaggle.com/datasets/alexandrepetit881234/korean-demographics-20002022?resource=download
#https://stackoverflow.com/questions/26147180/convert-row-to-column-header-for-pandas-dataframe

col = ['Date', 'Region', 'Birth','Birth_rate', 
'Death',
'Death_rate',
'Natural_growth',
'Growth_rate',
'Marriage',
'Marriage_rate',
'Divorce',
'Divorce_rate']

data = pd.read_csv("C:/Users/user/Documents/Korean_demographics_2000-2022.csv",names=col)
data.drop(data.index[0], inplace = True)
data = data.replace("",np.NaN)
#print(data.isnull().any().any())

#Get the plot of avg birthrate for each year by year(2000-2022)
#access multiple columns with only date,region,birthrate
date = data.loc[:,["Date","Region","Birth","Death"]]
newdate = []
newdate = date.loc[date['Region'] == 'Whole country']
print(newdate)

#get the avg value for death and birth rate
#https://www.geeksforgeeks.org/python-column-average-in-record-list/
avgbirthrate= []
avgdeathrate = []
count = 0
sum = 0
for i in range(1,len(newdate)+1):
    count+=1
    sum += float(newdate.loc[18*i,'Birth'])
    if count == 12:
        sum = round(sum/12,3)
        avgbirthrate.append(sum)
        sum = 0
        count = 0
        pass
    if i == 270:
        sum = round(sum/6,3)
        avgbirthrate.append(sum)
        pass    
    else:
        pass

count= 0
sum = 0 
for i in range(1,len(newdate)+1):
    count+=1
    sum += float(newdate.loc[18*i,'Death'])
    if count == 12:
        sum = round(sum/12,3)
        avgdeathrate.append(sum)
        sum = 0
        count = 0
        pass
    if i == 270:
        sum = round(sum/6,3)
        avgdeathrate.append(sum)
        pass    
    else:
        pass

years = ['2000','2001','2002','2003','2004','2005','2006','2007','2008','2009','2010','2011','2012','2013','2014','2015','2016','2017','2018','2019','2020','2021','2022']

#visualize the birthrate and deathrate by date and regions

# plt.plot(years,avgbirthrate,color = "#539caf",label = "Birth")
# plt.plot(years, avgdeathrate,label = "Death",color='maroon')
# plt.title("Birth Rate VS Death Rate In South Korea By Year(2000-2022)")
# plt.xlabel('Year')
# plt.ylabel('Birth and Death')
# plt.grid()
# plt.legend()
# plt.show()

#Get the Birth rate of Regions In South Korea By Year(2000-2022)
db = data.loc[:,["Date","Region","Birth"]]

avgbr_Busan = []
avgbr_Chungcheongbukdo = []
avgbr_Chungcheongnamdo = []
avgbr_Daegu = []
avgbr_Daejeon = []
avgbr_Gangwondo = []
avgbr_Gwangju = []
avgbr_Gyeonggido = []
avgbr_Gyeongsangbukdo = []
avgbr_Gyeongsangnamdo = []
avgbr_Incheon = []
avgbr_Jeju = []
avgbr_Jeollabukdo = []
avgbr_Jeollanamdo =[]
avgbr_Sejong = []
avgbr_Seoul = []
avgbr_Ulsan = []
years = ['2000','2001','2002','2003','2004','2005','2006','2007','2008','2009','2010','2011','2012','2013','2014','2015','2016','2017','2018','2019','2020','2021','2022']

Busan_db = db.loc[db['Region'] == 'Busan']
count = 0
sum = 0
for i in range(1,18*len(Busan_db),18):
    count+=1
    sum += float(Busan_db.loc[i,'Birth'])
    if count == 12:
        sum = round(sum/12,3)
        avgbr_Busan.append(sum)
        sum = 0
        count = 0
        pass
        
    if i == 4843:
        sum = round(sum/6,3)
        avgbr_Busan.append(sum)
        pass

Chungcheongbukdo_db = db.loc[db['Region'] == 'Chungcheongbuk-do']
count = 0
sum = 0
for i in range(2,18*len(Chungcheongbukdo_db),18):
    count+=1
    sum += float(Chungcheongbukdo_db.loc[i,'Birth'])
    if count == 12:
        sum = round(sum/12,3)
        avgbr_Chungcheongbukdo.append(sum)
        sum = 0
        count = 0
        pass
        
    if i == 4844:
        sum = round(sum/6,3)
        avgbr_Chungcheongbukdo.append(sum)
        pass

Chungcheongnamdo_db = db.loc[db['Region'] == 'Chungcheongnam-do']
count = 0
sum = 0
for i in range(3,18*len(Chungcheongnamdo_db)+1,18):
    count+=1
    sum += float(Chungcheongnamdo_db.loc[i,'Birth'])
    if count == 12:
        sum = round(sum/12,3)
        avgbr_Chungcheongnamdo.append(sum)
        sum = 0
        count = 0
        pass
        
    if i == 4845:
        sum = round(sum/6,3)
        avgbr_Chungcheongnamdo.append(sum)
        pass

Daegu_db = db.loc[db['Region'] == 'Daegu']
count = 0
sum = 0
for i in range(4,18*len(Daegu_db)+1,18):
    count+=1
    sum += float(Daegu_db.loc[i,'Birth'])
    if count == 12:
        sum = round(sum/12,3)
        avgbr_Daegu.append(sum)
        sum = 0
        count = 0
        pass
        
    if i == 4846:
        sum = round(sum/6,3)
        avgbr_Daegu.append(sum)
        pass

Daejeon_db = db.loc[db['Region'] == 'Daejeon']
count = 0
sum = 0
for i in range(5,18*len(Daejeon_db)+1,18):
    count+=1
    sum += float(Daejeon_db.loc[i,'Birth'])
    if count == 12:
        sum = round(sum/12,3)
        avgbr_Daejeon.append(sum)
        sum = 0
        count = 0
        pass
        
    if i == 4847:
        sum = round(sum/6,3)
        avgbr_Daejeon.append(sum)
        pass

Gangwondo_db = db.loc[db['Region'] == 'Gangwon-do']
count = 0
sum = 0
for i in range(6,18*len(Gangwondo_db),18):
    count+=1
    sum += float(Gangwondo_db.loc[i,'Birth'])
    if count == 12:
        sum = round(sum/12,3)
        avgbr_Gangwondo.append(sum)
        sum = 0
        count = 0
        pass
        
    if i == 4848:
        sum = round(sum/6,3)
        avgbr_Gangwondo.append(sum)
        pass

Gwangju_db = db.loc[db['Region'] == 'Gwangju']
count = 0
sum = 0
for i in range(7,18*len(Gwangju_db)+1,18):
    count+=1
    sum += float(Gwangju_db.loc[i,'Birth'])
    if count == 12:
        sum = round(sum/12,3)
        avgbr_Gwangju.append(sum)
        sum = 0
        count = 0
        pass
        
    if i == 4849:
        sum = round(sum/6,3)
        avgbr_Gwangju.append(sum)
        pass

Gyeonggido_db = db.loc[db['Region'] == 'Gyeonggi-do']
count = 0
sum = 0
for i in range(8,18*len(Gyeonggido_db)+1,18):
    count+=1
    sum += float(Gyeonggido_db.loc[i,'Birth'])
    if count == 12:
        sum = round(sum/12,3)
        avgbr_Gyeonggido.append(sum)
        sum = 0
        count = 0
        pass
        
    if i == 4850:
        sum = round(sum/6,3)
        avgbr_Gyeonggido.append(sum)
        pass

Gyeongsangbukdo_db = db.loc[db['Region'] == 'Gyeongsangbuk-do']
count = 0
sum = 0
for i in range(9,18*len(Gyeongsangbukdo_db)+1,18):
    count+=1
    sum += float(Gyeongsangbukdo_db.loc[i,'Birth'])
    if count == 12:
        sum = round(sum/12,3)
        avgbr_Gyeongsangbukdo.append(sum)
        sum = 0
        count = 0
        pass
        
    if i == 4851:
        sum = round(sum/6,3)
        avgbr_Gyeongsangbukdo.append(sum)
        pass

Gyeongsangnamdo_db = db.loc[db['Region'] == 'Gyeongsangnam-do']
count = 0
sum = 0
for i in range(10,18*len(Gyeongsangnamdo_db)+1,18):
    count+=1
    sum += float(Gyeongsangnamdo_db.loc[i,'Birth'])
    if count == 12:
        sum = round(sum/12,3)
        avgbr_Gyeongsangnamdo.append(sum)
        sum = 0
        count = 0
        pass
        
    if i == 4852:
        sum = round(sum/6,3)
        avgbr_Gyeongsangnamdo.append(sum)
        pass

Incheon_db = db.loc[db['Region'] == 'Incheon']
count = 0
sum = 0
for i in range(11,18*len(Incheon_db)+1,18):
    count+=1
    sum += float(Incheon_db.loc[i,'Birth'])
    if count == 12:
        sum = round(sum/12,3)
        avgbr_Incheon.append(sum)
        sum = 0
        count = 0
        pass
        
    if i == 4853:
        sum = round(sum/6,3)
        avgbr_Incheon.append(sum)
        pass

Jeju_db = db.loc[db['Region'] == 'Jeju']
count = 0
sum = 0
for i in range(12,18*len(Jeju_db)+1,18):
    count+=1
    sum += float(Jeju_db.loc[i,'Birth'])
    if count == 12:
        sum = round(sum/12,3)
        avgbr_Jeju.append(sum)
        sum = 0
        count = 0
        pass
        
    if i == 4854:
        sum = round(sum/6,3)
        avgbr_Jeju.append(sum)
        pass

Jeollabukdo_db = db.loc[db['Region'] == 'Jeollabuk-do']
count = 0
sum = 0
for i in range(13,18*len(Jeollabukdo_db)+1,18):
    count+=1
    sum += float(Jeollabukdo_db.loc[i,'Birth'])
    if count == 12:
        sum = round(sum/12,3)
        avgbr_Jeollabukdo.append(sum)
        sum = 0
        count = 0
        pass
        
    if i == 4855:
        sum = round(sum/6,3)
        avgbr_Jeollabukdo.append(sum)
        pass

Jeollanamdo_db = db.loc[db['Region'] == 'Jeollanam-do']
count = 0
sum = 0
for i in range(14,18*len(Jeollanamdo_db)+1,18):
    count+=1
    sum += float(Jeollanamdo_db.loc[i,'Birth'])
    if count == 12:
        sum = round(sum/12,3)
        avgbr_Jeollanamdo.append(sum)
        sum = 0
        count = 0
        pass
        
    if i == 4856:
        sum = round(sum/6,3)
        avgbr_Jeollanamdo.append(sum)
        pass

Sejong_db = db.loc[db['Region'] == 'Sejong']
count = 0
sum = 0
print(Sejong_db)
for i in range(15,18*len(Sejong_db)+1,18):
    count+=1
    sum += float(Sejong_db.loc[i,'Birth'])
    if count == 12:
        sum = round(sum/12,3)
        avgbr_Sejong.append(sum)
        sum = 0
        count = 0
        pass
        
    if i == 4857:
        sum = round(sum/6,3)
        avgbr_Sejong.append(sum)
        pass
print(avgbr_Sejong)

Seoul_db = db.loc[db['Region'] == 'Seoul']
count = 0
sum = 0
for i in range(16,18*len(Seoul_db)+1,18):
    count+=1
    sum += float(Seoul_db.loc[i,'Birth'])
    if count == 12:
        sum = round(sum/12,3)
        avgbr_Seoul.append(sum)
        sum = 0
        count = 0
        pass
        
    if i == 4858:
        sum = round(sum/6,3)
        avgbr_Seoul.append(sum)
        pass

Ulsan_db = db.loc[db['Region'] == 'Ulsan']
count = 0
sum = 0
for i in range(17,18*len(Ulsan_db)+1,18):
    count+=1
    sum += float(Ulsan_db.loc[i,'Birth'])
    if count == 12:
        sum = round(sum/12,3)
        avgbr_Ulsan.append(sum)
        sum = 0
        count = 0
        pass
        
    if i == 4859:
        sum = round(sum/6,3)
        avgbr_Ulsan.append(sum)
        pass

#visualize the birthrate by regions
plt.plot(years,avgbr_Busan,color = "dodgerblue",label = "Busan")
plt.plot(years, avgbr_Chungcheongbukdo,label = "Chungcheongbukdo",color='saddlebrown')
plt.plot(years,avgbr_Chungcheongnamdo,color = "darkkhaki",label = "Chungcheongnamdo")
plt.plot(years,avgbr_Daegu,color = "darkslategrey",label = "Daegu")
plt.plot(years,avgbr_Daejeon,color = "darkgoldenrod",label = "Daejeon")
plt.plot(years,avgbr_Gangwondo,color = "seagreen",label = "Gangwondo")
plt.plot(years,avgbr_Gwangju,color = "crimson",label = "Gwangju")
plt.plot(years,avgbr_Gyeonggido,color = "dimgray",label = "Gyeonggido")

plt.plot(years,avgbr_Gyeongsangbukdo,color = "blueviolet",label = "Gyeongsangbukdo")
plt.plot(years,avgbr_Gyeongsangnamdo,color = "midnightblue",label = "Gyeongsangnamdo")

plt.plot(years,avgbr_Incheon,color = "deepskyblue",label = "Incheon")
plt.plot(years,avgbr_Jeju,color = "mediumblue",label = "Jeju")

plt.plot(years,avgbr_Jeollabukdo,color = "olivedrab",label = "Jeollabukdo")
plt.plot(years,avgbr_Jeollanamdo,color = "darkmagenta",label = "Jeollanamdo")

plt.plot(years,avgbr_Sejong,color = "orange",label = "Sejong")
plt.plot(years,avgbr_Seoul,color = "rebeccapurple",label = "Seoul")
plt.plot(years,avgbr_Ulsan,color = "orangered",label = "Ulsan")



plt.title("Birth Rate Of Regions In South Korea By Year(2000-2022)")
plt.xlabel('Year')
plt.ylabel('Birth Rate ')
plt.grid()
plt.legend()
plt.show()


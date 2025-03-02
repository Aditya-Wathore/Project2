import pandas as pd
import numpy as np
data = pd.read_csv("D:\exal_data\googleplaystore.csv")
print(data)
print("===============================================================")
# 1. Find Total Number Apps in Google Play Store
print("Total number of Apps",data.shape[0])
print("===============================================================")
# 2. Find the Total Number of Columns in Each app of Google Play Store
print("total number of app",data.shape[1])
print("===============================================================")
# 1. Display Top 5 Rows of The Dataset
# two ways to write here
print(data.head())
print(data.head(5))
print("===============================================================")
# 2. Check the Last 3 Rows of The Dataset
print(data.tail(3))
print("===============================================================")
# 3. Find Shape of Our Dataset (Number of Rows & Number of Columns)
print("number of rows",data.shape[0])
print("number of columns",data.shape[1])
print("===============================================================")
# 4. Get Information About Our Dataset Like Total Number Rows, Total Number of Columns, Datatypes of Each Column
#    And  Memory Requirement
print(data.describe(include="all"))
print(data.describe())
print("===============================================================")
# 5. Get Overall Statistics About The Dataframe OR Get the Descriptive Statistics about Google Play Store
print(data.describe())
print("===============================================================")
# 6 Obtain Total Number of App Titles Contain Astrology
print(data.columns)
print(data[data['App'].str.contains('Astrology')])
print("===============================================================")
# 7. Find Average App Rating
print("Average App Rating",data["Rating"].mean())
print("===============================================================")
# 8.  Find Total Number of Unique Category
d = len(data.groupby('Category').nunique())
print("Total number of unique category",d)
print("===============================================================")
# 9. Which Category Getting The Highest Average Rating?
print(data.columns)
# to find the group of the data in category wise
print(data.groupby("Category").size())
print(data.groupby("Category")["Rating"].mean().max())
print("===============================================================")
#10. Find Total Number of App having 5 Star Rating
print("Total Number of App having 5 Star Rating",data[data["Rating"]==5].shape[0])
print("===============================================================")
# 11.Find Average Value of Reviews

print(data.columns)
print(data[data['Reviews']=='3.0M'])
print(data['Reviews'].replace("3.0M",3.0*1000000))
p = data['Reviews'] = data['Reviews'].replace("3.0M",3.0)
print(data[data['Reviews']==3.0])
data['Reviews']=data['Reviews'].astype("float")
print("Average Value of Reviews",data["Reviews"].mean())
print("==================================================")
#12. Find Total Number of Free and Paid Apps
print(data.columns)
print("Count the Paid Apps")
print(len(data[data["Type"]=="Paid"]))
print("Count the Free Apps")
print(len(data[data["Type"]=="Free"]))
print("====================================================")
# 13.  Which App Has Maximum Reviews?
print(data.columns)
d = data[data["Reviews"]== data["Reviews"].max()]["App"][2544 ]
print("Name of the Application",d)
print("================================================")
# 14. Display Top 5 Apps Having Highest Reviews
print(data['Reviews'].sort_values(ascending=False))
indices=data['Reviews'].sort_values(ascending=False).head().index
indices=data['Reviews'].sort_values(ascending=False).head().index
print(indices)
data.iloc[indices]
print(data.iloc[indices]["App"])
print(data.iloc[indices]["App"].value_counts())
print("============================================================")
#15. Find Average Rating of Free and Paid Apps
print(data.columns)
print(data.groupby("Type")["Rating"].mean())
print(data.groupby("Type")["Rating"].agg(["mean"]))
print("Average Rating of Free Apps=",data.groupby("Type")["Rating"].mean()["Free"])
print("Average Rating of Paid Apps=",data.groupby("Type")["Rating"].mean()["Paid"])
print("Average Rating of 0 Apps=",data.groupby("Type")["Rating"].mean()["0"])
print("=====================================================================")
#16. Display Top  5 Apps Having Maximum Installs
print(data['Installs'])
print(data['Installs'].dtype)
#Replace "," with empty string
data["Installs-1"]=data['Installs'].str.replace(",","")
print(data["Installs-1"])
data["Installs-1"]=data["Installs-1"].str.replace("+","")
print(data["Installs-1"])
print(data[data["Installs-1"]=='Free'])
data["Installs-1"]=data["Installs-1"].str.replace("Free","0")

print(data[data["Installs-1"]=="0"])
#Top  5 Apps Having Maximum Installs
data["Installs-1"].sort_values(ascending=False).head()
print(data["Installs-1"])
indices=data["Installs-1"].sort_values(ascending=False).head().index
print(data.iloc[indices])
indices=data["Installs-1"].sort_values(ascending=False).head().index
print(data.iloc[indices]["App"])

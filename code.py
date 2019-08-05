# --------------
#Importing header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Path of the file
path
data=pd.read_csv(path)
data.rename(columns={"Total": "Total_Medals"},inplace= True)
data.head(10)

#Code starts here



# --------------
#Code starts here

#Creating new column 'Better_Event'
data['Better_Event'] = np.where(data['Total_Summer'] > data['Total_Winter'] , 'Summer', 'Winter')
data['Better_Event'] = np.where(data['Total_Summer'] == data['Total_Winter'] , 'Both', data['Better_Event'])

#Finding the value with max count in 'Better_Event' column
better_event=data['Better_Event'].value_counts().index.values[0]

#Printing the better event
print('Better_Event=', better_event)

    
#Code ends here    


# --------------
#Code starts here






top_countries=data[['Country_Name','Total_Summer', 'Total_Winter','Total_Medals']]
top_countries=top_countries[:-1]
def top_ten(data,c):
    country_list=[]
    country_list= list((data.nlargest(10,c)['Country_Name']))
    return country_list
  
top_10_summer=top_ten(top_countries,"Total_Summer")
print(top_10_summer)
top_10_winter=top_ten(top_countries,"Total_Winter")
print(top_10_winter)
top_10=top_ten(top_countries,"Total_Medals")
print(top_10)
common=list(set(top_10_summer) & set(top_10_winter) & set(top_10))
print(common)



# --------------
#Code starts here
summer_df=data[data["Country_Name"].isin(top_10_summer)]
winter_df=data[data["Country_Name"].isin(top_10_winter)]
top_df=data[data["Country_Name"].isin(top_10)]
summer_df.plot(kind="bar")
winter_df.plot(kind="bar")
top_df.plot(kind="bar")


# --------------
#Code starts here




summer_df['Golden_Ratio'] = summer_df['Gold_Summer'] / summer_df['Total_Summer']
summer_max_ratio = summer_df['Golden_Ratio'].max()
summer_country_gold = summer_df[summer_df['Golden_Ratio']==summer_df['Golden_Ratio'].max()].iloc[0,0]

winter_df['Golden_Ratio'] = winter_df['Gold_Winter'] / winter_df['Total_Winter']
winter_max_ratio = winter_df['Golden_Ratio'].max()
winter_country_gold = winter_df[winter_df['Golden_Ratio']==winter_df['Golden_Ratio'].max()].iloc[0,0]

top_df['Golden_Ratio'] = top_df['Gold_Total'] / top_df['Total_Medals']
top_max_ratio = top_df['Golden_Ratio'].max()
top_country_gold = top_df[top_df['Golden_Ratio']==top_df['Golden_Ratio'].max()].iloc[0,0]


# --------------
#Code starts here





data_1=data[:-1]
data_1["Total_Points"]=data["Gold_Total"]*3+data["Silver_Total"]*2+data["Bronze_Total"]
most_points=data_1["Total_Points"].max()
best_country=data_1[data_1['Total_Points']==data_1['Total_Points'].max()].iloc[0,0]


# --------------
#Code starts here
best=data[data["Country_Name"]==best_country]
best=best[['Gold_Total','Silver_Total','Bronze_Total']]
best.plot(kind="bar",stacked=True,figsize=(15,10))
plt.xlabel("United States")
plt.ylabel("Medals Tally")
plt.xticks(rotation=45)






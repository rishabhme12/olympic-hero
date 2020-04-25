# --------------
#Importing header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Code starts here
data = pd.read_csv(path)
data.rename(columns={'Total':'Total_Medals'}, inplace = True)
print(data.head(10))


# --------------
#Code starts here
data['Better_Event'] = np.where(data['Total_Summer']>data['Total_Winter'], 'Summer', np.where(data['Total_Summer']<data['Total_Winter'], 'Winter', 'Both'))
better_event = data['Better_Event'].value_counts().idxmax()
print(better_event)


# --------------
#Code starts here
top_countries = data[['Country_Name', 'Total_Summer', 'Total_Winter', 'Total_Medals']]
print(top_countries.tail(1))
top_countries.drop(top_countries.tail(1).index, inplace = True)
print(top_countries.tail(1))
top_countries.set_index('Country_Name', inplace = True)
def top_ten(df, c):
    country_list = []
    country_list = list(df.nlargest(10, c).index)
    return country_list
top_10_summer = top_ten(top_countries, 'Total_Summer')
top_10_winter = top_ten(top_countries, 'Total_Winter')
top_10 = top_ten(top_countries, 'Total_Medals')
print(top_10_summer, top_10_winter, top_10, sep = '\n')
common = list(set(top_10) & set(top_10_summer) & set(top_10_winter))
top_countries.reset_index(inplace = True)


# --------------
#Code starts here
summer_df = data[data['Country_Name'].isin(top_10_summer)]
winter_df = data[data['Country_Name'].isin(top_10_winter)]
top_df = data[data['Country_Name'].isin(top_10)]
fig, (ax_1,ax_2, ax_3) = plt.subplots(1,3, figsize = (15,5))
summer_df.plot('Country_Name', 'Total_Summer', kind = 'bar', ax = ax_1)
plt.xlabel('Countries Name')
plt.ylabel('Medals in Summer Olympic')
plt.title('Top 10 Summer Olympic Countries Data')
winter_df.plot('Country_Name', 'Total_Winter', kind = 'bar', ax = ax_2)
plt.xlabel('Countries Name')
plt.ylabel('Medals in Winter Olympic')
plt.title('Top 10 Winter Olympic Countries Data')
top_df.plot('Country_Name', 'Total_Medals', kind = 'bar', ax = ax_3)
plt.xlabel('Countries Name')
plt.ylabel('Medals in Olympic')
plt.title('Top 10 Olympic Countries Data')


# --------------
#Code starts here
summer_df['Golden_Ratio'] = summer_df['Gold_Summer']/summer_df['Total_Summer']
idx = summer_df['Golden_Ratio'].idxmax()
summer_max_ratio = summer_df['Golden_Ratio'][idx]
summer_country_gold = summer_df['Country_Name'][idx]
print(summer_country_gold, summer_max_ratio)

winter_df['Golden_Ratio'] = winter_df['Gold_Winter']/winter_df['Total_Winter']
idx = winter_df['Golden_Ratio'].idxmax()
winter_max_ratio = winter_df['Golden_Ratio'][idx]
winter_country_gold = winter_df['Country_Name'][idx]
print(winter_country_gold, winter_max_ratio)

top_df['Golden_Ratio'] = top_df['Gold_Total']/top_df['Total_Medals']
idx = top_df['Golden_Ratio'].idxmax()
top_max_ratio = top_df['Golden_Ratio'][idx]
top_country_gold = top_df['Country_Name'][idx]
print(top_country_gold, top_max_ratio)


# --------------
#Code starts here
data_1 = data[:-1]



data_1['Total_Points'] = 3*data_1['Gold_Total'] + 2*data_1['Silver_Total'] + data_1['Bronze_Total']

id_ = data_1['Total_Points'].idxmax()
most_points = data_1['Total_Points'][id_]
best_country = data_1['Country_Name'][id_]
print(most_points, best_country)


# --------------
#Code starts here
best = data[data['Country_Name'] == best_country]
best = best[['Gold_Total', 'Silver_Total', 'Bronze_Total']]
best.plot.bar()
plt.xlabel('United States')
plt.ylabel('Medals Tally')
plt.xticks(rotation = 45)



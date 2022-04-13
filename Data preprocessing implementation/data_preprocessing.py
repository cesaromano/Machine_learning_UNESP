import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns



filepath = 'C:/Users/guazo/Documents/WORK/UNESP/First semester 2022/Machine Learning - Denis/Practical examples/Data preprocessing implementation/russia_losses_equipment.csv'

#Save the filepath information
data = pd.read_csv(filepath)

#Print columns headers
#print(data.columns)

#delete the desired column
#data = data.drop(['helicopter'], axis=1)

#Show the data shape, 0 for instances, 1 for atributes
#print(f"{(data.shape[0])} Instances x {(data.shape[1])} Atributes")

#Show 5 first instances of atributes
#print(data.head())

"""
print("Number of missing values")
for col in data.columns:
    print(f"{col}: {data[col].isna().sum()} --- {data[col].isna().sum()/len(data)*100}%")

print(data[col].isna().sum()/len(data)*100)
"""

#Replace missing data
"""
data2 = data['mobile SRBM system']
print('Before filling')
print(data2[0:29])

data2 = data2.fillna(data2.median())
print('After filling')
print(data2)
"""

#Second filling missing data method

"""
data3 = data.copy()
data3['mobile SRBM system'].fillna(data3['mobile SRBM system'].median(), inplace=True)
print(data[0:29]['mobile SRBM system'])
print(data3[0:29]['mobile SRBM system'])
"""

#Drop missing data method
#Drop the rows where at least one element is missing.
#axis='columns' parameter Drop the columns where at least one element is missing
#how='all' parameter Drop the rows where all elements are missing
#subset=['name', 'toy'] parameter Define in which columns to look for missing values

"""
print('Number of rows in original data = %d' % (data.shape[0]))

data2 = data.dropna()
print('Number of rows after discarding missing values = %d' % (data2.shape[0]))
"""

"""
#Drop column with missing data
data2 = data.drop(['special equipment'], axis=1)
#Converting to numeric values
data2['mobile SRBM system'] = pd.to_numeric(data2['mobile SRBM system'])
#plot a boxplot size parameter (width, height)
data2.boxplot(figsize=(10, 5))

plt.show()
"""
#droping date column
data2 = data.drop(['date'], axis=1)
#filling missing values columns with median
data2['mobile SRBM system'] = data2['mobile SRBM system'].fillna(data2['mobile SRBM system'].median())
data2['special equipment'] = data2['special equipment'].fillna(data2['special equipment'].median())
#z-score generating
Z = (data2-data2.mean())/data2.std()
print(Z[0:6])
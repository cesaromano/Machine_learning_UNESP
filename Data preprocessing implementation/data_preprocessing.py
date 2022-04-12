import pandas as pd


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

print("Number of missing values")
for col in data.columns:
    print(f"{col}: {data[col].isna().sum()} --- {data[col].isna().sum()/len(data)*100}%")
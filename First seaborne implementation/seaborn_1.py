import seaborn as sns
import matplotlib.pyplot as plt

dados = sns.load_dataset('tips')

#Show 5 rows for 5 columns
#print(dados.head())

#Show some information about the dataset
#print(dados.info())

#Show some basic statistical information
#print(dados.describe())

#Show median of 'size' column
#print(dados['size'].median())

#Show dataset median
#print(dados.mode())

#Plot a histogram
#sns.displot(dados, x = 'tip')

#Show quantity each binary category
#print(dados['sex'].value_counts())

#Plot colum quantity
#sns.countplot(dados['sex'])

#Plot relationships betwen two variables
#sns.relplot(
#    data = dados,
#    x = "total_bill", y = "tip", col = "time",
#    hue = "sex"
#)

#Plot histogram and scatter
#sns.jointplot(data=dados, x="total_bill", y='tip')

#Plot histogram and scatter density
#sns.jointplot(data=dados, x="total_bill", y='tip', kind='kde')

#Plot matrix by numeric data of one category
#sns.pairplot(data=dados, hue="sex")

#Plot a boxplot
#sns.boxplot(x='sex', y='tip', data=dados)

#Plot a boxplot
#sns.boxplot(x='size', y='tip', data=dados)

#Plot a boxplot
#sns.boxplot(x='size', y='total_bill', data=dados)

#Plot a headmap corelations betwen attributes
#sns.heatmap(dados.corr(), vmin=0, vmax=1, annot=True)

#Show data correlation
print(dados.corr())

plt.show()
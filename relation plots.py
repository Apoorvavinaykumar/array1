import seaborn as sns
import matplotlib.pyplot as plt

# Example dataset
df = sns.load_dataset('iris')

# Scatter plot
plt.figure(figsize=(8, 6))
sns.scatterplot(data=df, x='sepal_length', y='sepal_width', hue='species')
plt.title('Scatter Plot of Sepal Length vs Sepal Width')
plt.show()
plt.figure(figsize=(8, 6))
plt.hexbin(df['petal_length'], df['petal_width'], gridsize=30, cmap='Blues')
plt.colorbar(label='Count')
plt.title('Hexbin Plot of Petal Length vs Petal Width')
plt.xlabel('Petal Length')
plt.ylabel('Petal Width')
plt.show()
plt.figure(figsize=(8, 6))
sns.regplot(data=df, x='sepal_length', y='sepal_width', scatter_kws={'s':50}, line_kws={'color':'red'})
plt.title('Regression Plot of Sepal Length vs Sepal Width')
plt.show()
g = sns.FacetGrid(df, col='species', hue='species')
g.map(sns.scatterplot, 'sepal_length', 'sepal_width')
plt.show()

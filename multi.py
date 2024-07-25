import seaborn as sns
import matplotlib.pyplot as plt
iris=sns.load_dataset('iris')
sns.pairplot(iris,hue='species')
plt.show()
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import seaborn as sns
data=sns.load_dataset('iris')
x=data['sepal_length']
y=data['sepal_width']
z=data['petal_length']
fig=plt.figure(figsize=(10,6))
ax=fig.add_subplot(111,projection='3d')
ax.scatter(x,y,z,c='r',marker='3')
ax.set_xlabel('sepal length')
ax.set_ylabel('sepal width')
ax.set_zlabel('petal length')
plt.title('3D scatter plot')
plt.show()
from pandas.plotting import scatter_matrix
scatter_matrix(data,alpha=0.2,figsize=(10,10),diagonal='kde')
plt.suptitle('scatter plot matrix')
plt.show()
import seaborn as sns
import matplotlib.pyplot as plt
iris=sns.load_dataset('iris')
variables=['sepal_length','sepal_width','petal_length']
sns.pairplot(iris, vars=variables,hue='species')
plt.show()
plt.figure(figsize=(8,6))
sns.heatmap(iris[variables].corr(),annot=True,cmap='coolwarm',square=True)
plt.show()
data=sns.load_dataset('iris')
sns.jointplot(data=data,x='sepal_length',y='sepal_width',kind='scatter')
plt.show()

import pandas as pd
from sklearn.decomposition import PCA
from sklearn.ensemble import ExtraTreesClassifier

path = 'pima-indians-diabetes.csv'
names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
dataframe = pd.read_csv(path, names=names)
array = dataframe.values

X = array[:,0:8]
Y = array[:,8]

pca = PCA(n_components=3)
fit = pca.fit(X)
print("Explained Variance: %s",fit.explained_variance_ratio_)
print(fit.components_)

model = ExtraTreesClassifier()
model.fit(X, Y)
print("Scores for each attribute")
print(model.feature_importances_)
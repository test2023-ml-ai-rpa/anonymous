
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
raw_data = pd.read_csv('kyphosis-data.csv')
raw_data.columns
raw_data.info()
sns.pairplot(raw_data, hue = 'Kyphosis')
plt.show()
from sklearn.model_selection import train_test_split
x = raw_data.drop('Kyphosis', axis = 1)
y = raw_data['Kyphosis']
x_training_data, x_test_data, y_training_data, y_test_data = train_test_split(x, y, test_size =
0.3)
from sklearn.tree import DecisionTreeClassifier
model = DecisionTreeClassifier()
model.fit(x_training_data, y_training_data)
predictions = model.predict(x_test_data)
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
print('Performance of decision tree model:')
print(classification_report(y_test_data, predictions))
print('Confusion matrix of decision tree model:')
print(confusion_matrix(y_test_data, predictions))
from sklearn.ensemble import RandomForestClassifier
random_forest_model = RandomForestClassifier()
random_forest_model.fit(x_training_data, y_training_data)
random_forest_predictions = random_forest_model.predict(x_test_data)
print('Performance of random forest model:')
print(classification_report(y_test_data, random_forest_predictions))
print('Confusion matrix of random forest model:')
print(confusion_matrix(y_test_data, random_forest_predictions))

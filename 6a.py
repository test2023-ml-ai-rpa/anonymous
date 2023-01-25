from math import sqrt
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report

def euclidean_distance(a , b) :
    return sqrt(sum((e1-e2)**2 for e1, e2 in zip(a,b)))

def manhattan_distance(a , b):
    return sum(abs(e1-e2) for e1, e2 in zip(a,b))

def minkowski_distance(a , b, p):
    return sum(abs(e1-e2)**p for e1, e2 in zip(a,b))**(1/p)

actual = [1 ,0 ,0, 1, 0, 0, 1, 0, 0, 1]

predicted = [1, 0, 0, 1, 0, 0, 0, 1, 0, 0]

dist1= euclidean_distance(actual , predicted)

dist2 = manhattan_distance(actual, predicted)

dist3 = minkowski_distance(actual, predicted, 1)
print(dist3)

dist3 = minkowski_distance(actual, predicted, 2)
print(dist3)

matrix = confusion_matrix(actual, predicted, labels=[1,0])
print("Confusion matrix : \n" ,matrix)

tp , fn , fp ,tn = confusion_matrix(actual, predicted, labels=[1,0]).reshape(-1)
print('Outcome values : \n',tp ,fn, fp,tn)

matrix = classification_report(actual, predicted, labels=[1,0])
print('Classification report : \n',matrix)
 

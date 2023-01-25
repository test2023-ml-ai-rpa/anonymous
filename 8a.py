import numpy as np
import pandas as pd
from pgmpy.estimators import MaximumLikelihoodEstimator
from pgmpy.models import BayesianModel
from pgmpy.inference import VariableElimination

heartDisease = pd.read_csv('hearts.csv')
heartDisease= heartDisease.replace('?',np.nan)

print('Sample Instance from datset are given below')
print(heartDisease.dtypes)

model = BayesianModel([('age','heartdisease'),('gender','heartdisease'),('exang','heartdisease'),('cp','heartdisease'),()])

print('\nLearning CPD using likelihood estimators')
model.fit(heartDisease,estimator=MaximumLikelihoodEstimator)

print('\n Inferencing with Bayesian Network :')
HeartDiseasetest_infer= VariableElimination(model)

print('\n 1. Probaility of HeartDisease given') 
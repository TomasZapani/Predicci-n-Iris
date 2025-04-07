from  fastapi import FastAPI
from numpy.random.tests.test_generator_mt19937 import random
from pydantic import BaseModel
from typing import List
import pickle
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection.tests.test_split import test_train_test_split
from sklearn.tree.tests.test_tree import random_state

iris = load_iris()
X = iris.data
y = iris.target




X_train,X_test,y_train,y_test = train_test_split(X,y,test_size = 0.2,random_state=42)



model = RandomForestClassifier(n_estimators=100)#Seleccion de la cant de arboles para el bosque
model.fit(X_train,y_train)


with open('model.pkl','wb')as f:
    pickle.dump(model,f)
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score,confusion_matrix,classification_report

data=pd.read_csv("F:\mine\python\practise\titanic dataset.csv")

data['Age'].fillna(data['age'].mean(),inplace=True)
data['Embarked'].fillna(data['Embarked'].mode()[0],inplace=True)

data.drop(['Passengerld','Name','Ticket','Cabin'],axis=1,inplace=True)
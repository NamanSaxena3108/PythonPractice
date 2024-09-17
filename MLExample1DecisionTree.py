import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score,confusion_matrix,classification_report
from sklearn.model_selection import train_test_split

data={'A':[1,1,2,2],'B':[2,1,2,3],'C':[1,2,2,1],'Y':['NO','NO','YES','YES']}
df=pd.DataFrame(data)

#feature and target
X=df[['A','B','C']]
y=df['Y']

Xtrain,Xtest,ytrain,ytest=train_test_split(X,y,test_size=0.2,random_state=42)

model=DecisionTreeClassifier()
model.fit(Xtrain,ytrain)

ypred=model.predict(Xtest)

accuracy=accuracy_score(ytest,ypred)
conf_matrix=confusion_matrix(ytest,ypred)
class_report=classification_report(ytest,ypred)

print(f"Accuracy:{accuracy}")
print(conf_matrix)
print(class_report)
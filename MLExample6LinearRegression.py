import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error as mse,mean_absolute_error as mae,r2_score as r2
import matplotlib.pyplot as plt

data=pd.DataFrame({
    'experience':[0,1,2,5,7,8,10],
    'salary':[15000,25000,35000,43250,55000,65000,80000]
})

x=data[['experience']]
y=data['salary']
xtrain,xtest,ytrain,ytest=train_test_split(x,y,test_size=0.3,random_state=42)

model=LinearRegression()
model.fit(xtrain,ytrain)

y_pred=model.predict(xtest)
abso=mae(ytest,y_pred)
squa=mse(ytest,y_pred)
rsqua=r2(ytest,y_pred)

print(f"MAE:{abso},MSE:{squa},R2:{rsqua}")

newdata=[[4]]
predictedscore=model.predict(newdata)
print(f"predicted Score:{predictedscore}")

plt.scatter(x,y,color='red')
plt.plot(x,model.predict(x),color='blue')
plt.scatter(newdata,predictedscore,color='green')
plt.xlabel("Experience")
plt.ylabel("Salary")
plt.title("Experience VS Salary")
plt.show()
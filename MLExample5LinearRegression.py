import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error as mae, mean_squared_error as mse,r2_score as r2
import matplotlib.pyplot as plt

data=pd.DataFrame({
    "House Size":[100,150,200,250,300],
    "Price":[250000,350000,450000,550000,650000]
})

x=data[["House Size"]]
y=data["Price"]
xtrain,xtest,ytrain,ytest=train_test_split(x,y,test_size=0.2,random_state=42)

model=LinearRegression()
model.fit(xtrain,ytrain)

y_pred=model.predict(xtest)
abso=mae(ytest,y_pred)
squar=mse(ytest,y_pred)
rsquar=r2(ytest,y_pred)

print(abso,squar,rsquar)

newdata=[[400]]
predicted_score=model.predict(newdata)
print(f"predicted score={predicted_score}")

plt.scatter(x,y,color='red')
plt.plot(x,model.predict(x),color='blue')
plt.scatter(newdata,predicted_score,color='green')
plt.xlabel("House Size")
plt.ylabel("Price")
plt.title("House Size VS Price")
plt.show()
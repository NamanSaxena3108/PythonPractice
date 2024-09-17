import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

x=np.array([100,150,200,250,300]).reshape(-1,1)#house size in sq.feet
y=np.array([250000,350000,450000,550000,650000])#price

model=LinearRegression()
model.fit(x,y)

new_house_size=np.array([175,225]).reshape(-1,1)
predicted_price=model.predict(new_house_size)

print("intercept=",model.intercept_)
print("slope=",model.coef_[0])

plt.scatter(x,y,color="blue",label="Data")
plt.plot(x,model.predict(x),color="red",label="Regression Line")
plt.scatter(new_house_size,predicted_price,color="green",label="Prediction")
plt.xlabel("house size")
plt.ylabel("Price")
plt.title("simple example for linear progression")
plt.show()
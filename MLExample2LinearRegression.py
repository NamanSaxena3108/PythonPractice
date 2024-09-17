import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

x=np.array([1.5,2.5,3.5,4.5,5.5,6.5]).reshape(-1,1)
y=np.array([55,65,75,85,95,100])

model=LinearRegression()
model.fit(x,y)

new_hour_studied=np.array([3,5]).reshape(-1,1)
predicted_marks=model.predict(new_hour_studied)

print("Intercept=",model.intercept_)
print("slope=",model.coef_[0])

plt.scatter(x,y,color="blue",label="Data")
plt.plot(x,model.predict(x),color="red",label="Regression Line")
plt.scatter(new_hour_studied,predicted_marks,color="green",label="Prediction")
plt.xlabel("hours studied")
plt.ylabel("marks obtained")
plt.title("simple example for linear progression")
plt.show()

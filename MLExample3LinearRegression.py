import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as pl

pre_sales=int(input("enter the total no. of previous sales data"))
l1=[]
for i in range(0,pre_sales):
    b=int(input("enter the data"))
    l1.append(b)

new_sales=int(input("enter the total no. of new sales data"))
l2=[]
for i in range(0,new_sales):
    c=int(input("enter the data"))
    l2.append(c)

x=np.array([l1]).reshape(-1,1)
y=np.array([l2]).reshape(-1,1)

model=LinearRegression()
model.fit(x,y)

total_data=int(input("enter the total amount of data to be predicted"))
l=[]
for i in range(0,total_data):
    a=int(input("enter the data"))
    l.append(a)

new_sale=np.array([l]).reshape(-1,1)
predicted_sales=model.predict(new_sale)

print("Intercept=",model.intercept_)
print("slope=",model.coef_[0])

plt.scatter(x,y,color="blue",label="Data")
plt.plot(x,model.predict(x),color="red",label="Regression Line")
plt.scatter(new_sale,predicted_sales,color="green",label="Prediction")
plt.xlabel("Previous sales")
plt.ylabel("New sales")
plt.title("simple example for linear progression")
plt.show()

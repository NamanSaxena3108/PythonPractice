import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier,plot_tree
from sklearn.metrics import accuracy_score

from sklearn.datasets import load_iris

iris=load_iris()
X=iris.data
y=iris.target

xtrain,xtest,ytrain,ytest=train_test_split(X,y,test_size=0.3,random_state=42)

#without pruning
tree_clf=DecisionTreeClassifier(random_state=42)
tree_clf.fit(xtrain,ytrain)

y_pred_train=tree_clf.predict(xtrain)
y_pred_test=tree_clf.predict(xtest)

train_accuracy=accuracy_score(ytrain,y_pred_train)
test_accuracy=accuracy_score(ytest,y_pred_test)

print(f'Train Accuracy:{train_accuracy:0.2f}')
print(f'Test Accuracy:{test_accuracy:0.2f}')

#visualization
import matplotlib.pyplot as plt
plt.figure(figsize=(10,10))
plot_tree(tree_clf,filled=True,feature_names=iris.feature_names,class_names=iris.target_names)
plt.show()

#after pruning
pruned_tree_clf=DecisionTreeClassifier(max_depth=3,random_state=42)
pruned_tree_clf.fit(xtrain,ytrain)

y_pred_train_pruned=pruned_tree_clf.predict(xtrain)
y_pred_test_pruned=pruned_tree_clf.predict(xtest)

train_accuracy_pruned=accuracy_score(ytrain,y_pred_train_pruned)
test_accuracy_pruned=accuracy_score(ytest,y_pred_test_pruned)

print(f'Train Accuracy Pruned:{train_accuracy_pruned:0.2f}')
print(f'Test Accuracy Pruned:{test_accuracy_pruned:0.2f}')

#visualization
import matplotlib.pyplot as plt
plt.figure(figsize=(10,10))
plot_tree(tree_clf,filled=True,feature_names=iris.feature_names,class_names=iris.target_names)
plt.show()
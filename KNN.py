import pandas as pd
import numpy as np
from sklearn import preprocessing,cross_validation,neighbors

df = pd.read_csv("cancer.txt")
df.replace("?", -99999, inplace=True)
df.drop(["id"] ,1 , inplace=True)

X = np.array(df.drop(["class"], 1))
Y = np.array(df["class"])

X_train, X_test, Y_train, Y_test = cross_validation.train_test_split(X,Y,test_size=0.2)

clf = neighbors.KNeighborsClassifier()
clf.fit(X_train,Y_train)
accu = clf.score(X_test,Y_test)
print(accu)

print("\n\n\n\n")

example = np.array([1,1,1,1,2,10,3,1,1])
example = example.reshape(1, -1)

prediction = clf.predict(example)

print(prediction)
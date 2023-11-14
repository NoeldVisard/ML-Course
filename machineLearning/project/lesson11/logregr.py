from sklearn.linear_model import LogisticRegression
import random
import matplotlib.pyplot as plt
import numpy as np
from sklearn.model_selection import train_test_split

n = 50
X = np.array([[
    random.uniform(10, 99),
    random.uniform(10, 99),
    random.uniform(10, 99)
] for _ in range(n)])
Y = [random.randint(0, 1) for _ in range(n)]
plt.scatter(X[:,0], X[:,1], c = Y)
plt.show()

model = LogisticRegression()
model.fit(X, Y)
xTrain, yTrain, xTest, yTest = train_test_split(X, Y, train_size=0.5)
model.score(np.array(xTest).reshape(-1, 1), yTest)
x0, y0 = 25, 87
print(model.predict([[x0, y0]]))
plt.scatter(x0, y0)
plt.show()

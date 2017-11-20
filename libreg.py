import numpy as np

class LinearModel():
    def __init__(self):
        self.X = None
        self.y = None
        self.coefs = None
        self.sse = None
        self.sst = None

    def train(self, X, y):
        a = (np.linalg.inv(np.transpose(X).dot(X)).dot(np.transpose(X)).dot(y))
        self.coefs = np.append([sum(y) / len(y)], a)
        self.X = X
        self.y = y
        Xc = np.dot(X,self.coefs[1:])
        self.sse = sum(((self.coefs[0] + Xc) - y)**2)
        self.sst = sum((y-[sum(y) / len(y)])**2)

    def predict(self, X1):
        k = sum(X1*self.coefs[1:])
        return(self.coefs[0]+k)

    def r2(self, X, y):
        Xc = np.dot(X, self.coefs[1:])
        self.sse = sum(((np.mean(y) + Xc) - self.y) ** 2)
        self.sst = sum((self.y - np.mean(y)) ** 2)
        return(1-(self.sse/self.sst))

X = np.array([[1, 1], [-1, 1], [-1, -1], [1, -1]])
y = np.array([0.8, 1.2, 1.1, 1.4])

lm = LinearModel()
lm.train(X, y)

print("sst: ",round(lm.sst,2))
print("sse: ",round(lm.sse,2))
print("Predict: ",lm.predict(np.array([4,1])))
print("Coefficient: ",lm.coefs)
print("R2: ",round(lm.r2(X,y),2))
print("R2 on test",round(lm.r2(X,y+0.1),2))


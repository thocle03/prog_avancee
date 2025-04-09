#Importer les dependencies
import numpy as np
import pandas as pd


# Function Logistic

def sigmoid(x):
    return 1/(1+np.exp(-x))


# Méthode de prédiction

def predict(omega,x):
    res = sigmoid(np.dot(x,omega))
    return np.array([1 if x>=0.5 else 0 for x in res]).reshape(res.shape)

#   Fonction Coût

def cost(omega,x,y):
    first = -y * np.log(sigmoid(np.dot(x,omega)))
    second = (1-y) * np.log(1 - sigmoid(np.dot(x,omega)))
    return np.sum(first-second) / len(x)

#Importer les données
data = pd.read_csv('data.txt', header=None)
x = data.iloc[:,:2]
x = (x - x.mean()) / x.std()
x.insert(loc=0, column=None, value=1)
x = np.array(x).reshape(data.shape[0],3)
y = np.array(data.iloc[:,2]).reshape(data.shape[0],1)


#Initialiser l' Omega contient les poids (weight vector)

omega = np.array([[0],[0],[0]])

# Hyperparameters

alpha = 5e-5
iters = 1

# Gradient Descent

init_cost = str(cost(omega,x,y));

for i in range(iters):
    omega = omega - (((alpha)/(len(x))) * ( np.dot(x.T, sigmoid(np.dot(x,omega)) - y)))

print("Poids finaux:")
print(omega)
print("Coût initial:" + str(init_cost))
print("Coût final:" + str(cost(omega,x,y)))


# Evaluation du modèle

prediction = predict(omega,x)
correct = [1 if a==b else 0 for (a,b) in zip(prediction,y)]
print("Training set accuracy:" + str((sum(correct)/len(x))*100))
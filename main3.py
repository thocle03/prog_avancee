import numpy as np



v1 = [1, 2]
v2 = [3, 2]
v3 = [1, 4]


def fonction(omega,y,b):
    print(np.dot(omega, y)+b)
    return np.dot(omega, y)+b

#print(fonction(v1, v2, 0))

def loss(X, y, omega, b):
    predictions = np.array([fonction(omega, x, b) for x in X]) 
    err = (predictions - y) ** 2  
    return np.mean(err)
    

X = np.array([[1, 2], [2, 3], [3, 3], [6, 5], [7, 8], [8, 9]])
y = np.array([1, 0, 1, 0, 0, 0])

omega = np.array([0, 0])
b = 0

mse = loss(X, y, omega, b)
print("Loss : {mse}")


def delta_loss_omega(alpha, omega, X, b, Y):
    for i in range(len(X)):
        erreur = loss(X, Y, omega, b)
        for j in range(len(omega)):
            omega[j] = omega[j] - alpha * erreur
    return omega

print(delta_loss_omega(0.5, omega, X, 0, y))


def loss2(X, y, omega, b):
    predictions = np.array([fonction(omega, x, b) for x in X]) 
    err = (predictions - y)
    return np.mean(err)
learning_rate = 0.001


def yolo(X1,y1,omega1, b1, learning_rate1):
    for i in range (len(X1)):
        loss(X1, y1, omega1, b1)
        for j in range (len(omega1)):
            omega1[j]= (
                omega1[j]- (learning_rate1 / 2) * (y1[i]- loss2(X1, y1, omega1, b1) - b1) * X1[i][j]
            )
           
    return omega

yolo(X,y,omega, b, learning_rate)


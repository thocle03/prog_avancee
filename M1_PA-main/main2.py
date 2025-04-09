import numpy as np

class SVM:
    def __init__(self, C=1.0, sigma=1.0):
        self.C = C
        self.sigma = sigma

    def rbf_kernel(self, x1, x2):
        return np.exp(-np.linalg.norm(x1 - x2) ** 2 / (2 * self.sigma ** 2))

    def fit(self, X, y, max_iter=1000, tol=1e-5):
        m, n = X.shape
        self.alpha = np.zeros(m)
        self.b = 0
        self.K = np.array([[self.rbf_kernel(X[i], X[j]) for j in range(m)] for i in range(m)])

        def objective_function():
            return 0.5 * np.sum(self.alpha[:, None] * self.alpha * self.K) - np.sum(self.alpha)

        for _ in range(max_iter):
            grad = np.zeros(m)
            for i in range(m):
                grad[i] = 1 - y[i] * (np.sum(self.alpha * y * self.K[i]) + self.b)
                if self.alpha[i] > 0: 
                    grad[i] += self.C * self.alpha[i]

            self.alpha = self.alpha - 0.01 * grad
            self.alpha = np.clip(self.alpha, 0, self.C)

            self.b = np.mean(y - np.sum(self.alpha * y * self.K, axis=1))

            if np.linalg.norm(grad) < tol:
                break

    def predict(self, X):
        predictions = []
        for i in range(X.shape[0]):
            decision_function = np.sum(self.alpha * self.K[i]) + self.b
            predictions.append(np.sign(decision_function))
        return np.array(predictions)

if __name__ == "__main__":
    X = np.array([[1, 2], [2, 3], [3, 3], [6, 5], [7, 8], [8, 9]])
    y = np.array([1, 3, 2, -1, -3, -2])

    svm = SVM(C=1.0, sigma=1.0)
    svm.fit(X, y)

    predictions = svm.predict(X)
    print("Prédictions:", predictions)

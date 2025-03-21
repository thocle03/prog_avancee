from svm_model import load_data, train_svm, evaluate_model
from svm_plot import plot_decision_boundary

# Charger les données
X_train, X_test, y_train, y_test = load_data()

# Entraîner un SVM
model = train_svm(X_train, y_train, kernel="linear")

# Évaluer le modèle
accuracy = evaluate_model(model, X_test, y_test)
print(f"Précision du modèle SVM : {accuracy:.2f}")

# Visualiser la frontière de décision
plot_decision_boundary(model, X_train, y_train)

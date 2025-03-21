# **Travaux Pratiques : SVM et Algorithmes Génétiques**

## **1️ Présentation**
Ce projet contient deux Travaux Pratiques (TP) pour l'apprentissage et l'application des **Support Vector Machines (SVM)** et des **Algorithmes Génétiques (GA)**.

- **TP 1 : SVM** - Implémentation d'un modèle SVM pour classer des données et visualiser la frontière de décision.

## **2️ Structure du Dossier**
```
TD_SVM/
│
├── svm_main.py         # Fichier principal pour exécuter le SVM
├── svm_model.py        # Chargement des données et entraînement du modèle
├── svm_utils.py        # Fonctions utilitaires
├── svm_plot.py         # Visualisation de la frontière de décision
            # Documentation du projet
```

## **3️ Dépendances Nécessaires**
Assurez-vous d'avoir installé **Python 3.x** et les bibliothèques suivantes :
```bash
pip install numpy scikit-learn matplotlib
```

---

# ** TP 1 : Support Vector Machines (SVM)**

## ** Problème**
Nous avons un dataset contenant des points appartenant à **trois classes différentes**. L'objectif est d'entraîner un **SVM** pour classifier ces points et **visualiser la frontière de décision**.

## ** Solution**
- Charger le dataset **Iris**
- Séparer les données en **entraînement et test**
- Normaliser les données pour améliorer la classification
- Entraîner un **SVM linéaire** et un **SVM avec noyau non linéaire** (RBF, polynomial)
- Évaluer la précision et afficher la **matrice de confusion**
- **Tracer la frontière de décision** pour voir comment le modèle classe les points

## ** Étapes pour exécuter le code**
```bash
cd svm
python svm_main.py
```

## ** Résultats attendus**
- Affichage de la **précision du modèle** :
  ```bash
  Précision du modèle SVM : 0.91
  ```
- **Visualisation de la frontière de décision** montrant comment le modèle sépare les classes.





# ** Conclusion**
 **TP SVM** : Classification avec un **modèle SVM**, comparaison entre **SVM linéaire et non linéaire**.  
 **TP GA** : Optimisation d’une fonction avec un **algorithme génétique** utilisant **sélection, croisement et mutation**.  




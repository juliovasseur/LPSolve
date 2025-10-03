# 🎯 **LPSolve** - *Moteur d'Optimisation Linéaire*
## Solveur de Programmation Linéaire de Niveau Industriel

[![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)](https://python.org)
[![PuLP](https://img.shields.io/badge/PuLP-2.7+-green.svg)](https://pypi.org/project/PuLP/)
[![CBC](https://img.shields.io/badge/CBC-COIN--OR-orange.svg)](https://github.com/coin-or/Cbc)
[![License](https://img.shields.io/badge/License-MIT-red.svg)](LICENSE)

> **Des Données aux Décisions** : Transformez vos jeux de données CSV en **solutions d'optimisation concrètes** via la programmation linéaire. Du parsing de données à l'**analyse des contraintes saturées** et **calculs de prix duaux**.

---

## 🎯 **Vue d'Ensemble du Projet**

Ce projet implémente un **moteur d'optimisation linéaire de niveau industriel** qui transforme les données CSV en modèles mathématiques, résolus via le solveur CBC (COIN-OR). Le système couvre trois niveaux de complexité, des exemples éducatifs aux applications de gestion de portefeuille avec **calculs de valeurs marginales** et **analyse des contraintes saturées**.

### 🚀 **Outil Universel & Puissant**
Avant tout, c'est un **moteur d'optimisation généraliste** : vous pouvez **cloner ce repo**, remplacer les fichiers CSV par vos données normalisées, et résoudre **n'importe quel problème de programmation linéaire sous contraintes** !

### 📊 **Pipeline Complet**
```
Données CSV → Modélisation Mathématique → Optimisation → Décisions Concrètes
```

---

## 🚀 **Accès Rapide aux Cas d'Usage**

| Niveau | Cas d'Usage | Description | Accès Direct |
|--------|-------------|-------------|--------------|
| 🟢 **Débutant** | **[Exemples Éducatifs](./data/basic_linear_examples/README_FR.md)** | Optimisation simple chaises/tables avec contraintes marché | `make run-basic` |
| 🟡 **Intermédiaire** | **[Production Industrielle](./data/furniture_production/README_FR.md)** | Planification multi-sites avec supply chain (87 contraintes, ESG, transferts) | `make run-furniture` |
| 🔴 **Expert** | **[Finance Quantitative](./data/portfolio_optimization/README_FR.md)** | Portefeuille 16 actifs, contraintes réglementaires, logique type ALM | `make run-portfolio` |

## 📊 **Résultats de Performance**

| Niveau | Cas d'Usage | Variables | Contraintes | Temps | Profit |
|--------|-------------|-----------|-------------|-------|--------|
| 1 | Exemples de Base | 2 | 4 | <0.01s | 3,150€ |
| 2 | Production Multi-Sites | 155 | 87 | <0.05s | 6,985,500€ |
| 3 | Portefeuille Quantitatif | 33 | 40 | <0.02s | 2.46 bp/jour |

---

## 🚀 **Installation & Utilisation**

### 📦 **Installation des Dépendances**

```bash
cd lp_solver_engine
pip install -r requirements.txt
```

### ⚡ **Exécution Rapide**

```bash
# Exemples éducatifs - 3,150€ de profit optimal
make run-basic

# Production industrielle - 6,985,500€ de profit optimal
make run-furniture  

# Optimisation de portefeuille - 2.46 bp/jour d'utilité espérée
make run-portfolio
```

---

## 📚 **Documentation Détaillée**

### 🎓 **Guides par Niveau**
- **[🟢 Guide Débutant](./data/basic_linear_examples/README_FR.md)** : Concepts fondamentaux
- **[🟡 Guide Intermédiaire](./data/furniture_production/README_FR.md)** : Applications industrielles
- **[🔴 Guide Expert](./data/portfolio_optimization/README_FR.md)** : Finance quantitative

### 🔧 **Documentation Technique**
- **[🎛️ Moteur de Résolution](./lp_solver_engine/README_FR.md)** : Architecture technique
- **[📊 Formats de Données](./data/README_FR.md)** : Spécifications CSV

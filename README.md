# 🎯 **LPSolve** - *Moteur d'Optimisation Linéaire*
## Outil de Résolution d'Optimisation via Programmation Linéaire

[![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)](https://python.org)
[![PuLP](https://img.shields.io/badge/PuLP-2.7+-green.svg)](https://pypi.org/project/PuLP/)
[![CBC](https://img.shields.io/badge/CBC-COIN--OR-orange.svg)](https://github.com/coin-or/Cbc)
[![License](https://img.shields.io/badge/License-MIT-red.svg)](LICENSE)

> **Exemple d'un projet data → decision** : Transformation de données CSV en **décisions d'optimisation** via programmation linéaire. Du parsing des données à l'analyse des **contraintes saturées** et calcul des **coûts marginaux**.

---

## 🎯 **Vue d'ensemble du Projet**

Ce projet implémente un **moteur d'optimisation linéaire** qui transforme des données CSV en modèles mathématiques, résolus avec le solveur CBC (COIN-OR). Le système couvre trois niveaux de complexité, des exemples éducatifs aux applications de gestion de portefeuille avec calcul des **valeurs marginales** et analyse des **contraintes saturées**.

### 🚀 **Outil Puissant & Universel**
Avant tout, c'est un **moteur d'optimisation généraliste** : vous pouvez **cloner ce repo**, remplacer les CSV par vos données normalisées, et résoudre **n'importe quel problème d'optimisation linéaire sous contraintes** ! 

### 📊 **Pipeline Complet**
```
Données CSV → Modélisation Mathématique → Optimisation → Décisions Actionables
```

---

## 🏗️ **Architecture du Système**

### 🎯 **Approche Modulaire par Niveaux de Complexité**

### 🚀 **Accès Rapide aux Cas d'Usage**

| Niveau | Cas d'Usage | Description | Accès Direct |
|--------|-------------|-------------|--------------|
| 🟢 **Débutant** | **[Exemples Éducatifs](./data/basic_linear_examples/README.md)** | Optimisation simple chaises/tables avec contrainte de marché | `make run-basic` |
| 🟡 **Intermédiaire** | **[Production Industrielle](./data/furniture_production/README.md)** | Planification complexe avec 70+ contraintes (ESG, setup, pénalités) | `make run-furniture` |
| 🔴 **Expert** | **[Finance Quantitative](./data/portfolio_optimization/README.md)** | Portefeuille 16 actifs, contraintes réglementaires, logique type ALM | `make run-portfolio` |

> **💡 Conseil** : Commencez par les exemples éducatifs pour comprendre les concepts, puis progressez vers l'approche quantitative.

> **🎓 Note sur la terminologie** : Le système calcule les **valeurs marginales** (shadow prices) et **coûts de transaction**, mais ne produit pas d'analyse PnL ou ALM complète. Il suit cependant une **logique similaire** dans l'approche d'optimisation.

### 🏗️ **Structure Technique**

```
LPSolve/
├── 🎛️  lp_solver_engine/           # Moteur d'optimisation principal
│   ├── src/lpSolver/
│   │   ├── solvers/               # Algorithmes d'optimisation
│   │   │   ├── solver_core.py     # Solveur générique LP/MILP
│   │   │   └── portfolio_solver.py # Solveur spécialisé finance
│   │   ├── utils/                 # Utilitaires et parsing
│   │   │   ├── parsing.py         # Parsing CSV → modèle mathématique
│   │   │   ├── model_arrays.py    # Structures de données optimisées
│   │   │   └── modeling.py        # Construction des modèles  
│   │   └── archive/               # Versions historiques
│   ├── main.py                    # Point d'entrée générique
│   ├── portfolio_main.py          # Point d'entrée finance spécialisé  
│   └── requirements.txt           # Dépendances Python
├── � data/                        # Cas d'usage et données
│   ├── �📊 basic_linear_examples/   # Cas éducatifs (niveau 1)
│   ├── 🏭 furniture_production/    # Optimisation industrielle (niveau 2)
│   └── 💰 portfolio_optimization/  # Finance quantitative (niveau 3)
│       └── data/
│           ├── variables.csv      # 16 actifs (AAPL, MSFT, GOOGL...)
│           ├── objectives.csv     # Fonction d'utilité mean-variance
│           └── constraints.csv    # 40+ contraintes réglementaires
├── 📈 results/                     # Outputs d'optimisation
└── Makefile                       # Automation et commandes
```

---

## 🚀 Utilisation

### 🎯 **Fonctionnement Universel du Programme**

Ce programme est conçu pour résoudre **tout type de problème d'optimisation linéaire** en utilisant une approche standardisée basée sur des fichiers CSV. Peu importe votre domaine d'application (finance, production industrielle, logistique, etc.), le processus reste identique :

#### 📋 **Structure CSV Requise**

Le programme attend **3 fichiers CSV normalisés** dans le dossier `data/` de votre cas d'usage :

1. **`variables.csv`** - Définit les variables de décision
   ```csv
   variable_name,lower_bound,upper_bound,var_type
   x1,0,1,Continuous
   x2,0,100,Integer
   ```

2. **`objectives.csv`** - Définit la fonction objectif à optimiser
   ```csv
   variable_name,coefficient
   x1,10.5
   x2,-2.3
   ```

3. **`constraints.csv`** - Définit toutes les contraintes du problème
   ```csv
   constraint_name,variable_name,coefficient,operator,rhs
   budget_limit,x1,100,<=,50000
   budget_limit,x2,200,<=,50000
   minimum_production,x1,1,>=,10
   ```

#### 🔄 **Processus d'Exécution**

1. **Préparation** : Créez votre dossier de cas d'usage avec les 3 fichiers CSV
2. **Configuration** : Le programme parse automatiquement vos CSV
3. **Modélisation** : Construction automatique du modèle mathématique
4. **Résolution** : Optimisation avec le solveur CBC (COIN-OR)
5. **Analyse** : Génération des résultats et métriques détaillées

#### ✨ **Avantages de cette Approche**

- **🌐 Universalité** : Fonctionne pour tout problème LP/MILP
- **📊 Simplicité** : Interface CSV intuitive, pas de programmation requise
- **🔧 Flexibilité** : Ajout/modification de contraintes en éditant les CSV
- **📈 Scalabilité** : Gère des milliers de variables et contraintes
- **🎯 Reproductibilité** : Versionning facile des modèles via Git

### 📊 **Commandes Rapides**

```bash
# Lancer les trois cas d'usage principaux
make run-basic      # 🟢 Cas éducatif simple
make run-furniture  # 🟡 Optimisation industrielle  
make run-portfolio  # 🔴 Finance quantitative

# Créer votre propre cas d'usage
make create-case NAME=mon_projet
make run-custom PROJECT=mon_projet
```

---

## 🛠️ **Créer Votre Propre Cas d'Usage (En 2 Minutes !)**

Vous voulez résoudre VOTRE problème d'optimisation ? Rien de plus simple !

### 🚀 **Méthode Rapide avec Template**
```bash
# Créer un nouveau cas d'usage basé sur le template
make create-case NAME=mon_projet

# Cela crée automatiquement :
# data/mon_projet/
#   ├── data/
#   │   ├── variables.csv      # Template avec 2 variables exemple
#   │   ├── objectives.csv     # Template fonction objectif
#   │   └── constraints.csv    # Template contraintes
#   └── README.md              # Documentation personnalisable
```

### ✏️ **Personnalisation**
1. **Éditez les CSV** avec vos données spécifiques
2. **Modifiez le README** avec votre contexte métier
3. **Lancez l'optimisation** : `make run-custom PROJECT=mon_projet`

### 📋 **Template CSV Exemple**

Le template génère automatiquement un problème d'optimisation simple :
- **2 variables** : x1, x2 (continues, bornées)
- **1 objectif** : Maximiser 10*x1 + 5*x2
- **2 contraintes** : Budget et capacité

Remplacez simplement ces données par les vôtres !

---

## 📊 **Comprendre les Résultats d'Optimisation**

### 🎯 **Terminologie des Outputs**

Quand vous lancez une optimisation, le programme affiche plusieurs métriques importantes :

#### ✅ **Status de la Solution**
- **`OK`** : Solution optimale trouvée ✅
- **`INFEASIBLE`** : Aucune solution respectant toutes les contraintes ❌
- **`UNBOUNDED`** : Problème mal formulé (objectif tend vers l'infini) ⚠️

#### 📊 **Valeurs des Variables**
- **Valeur optimale** : Meilleure allocation trouvée pour chaque variable
- **Slack/Surplus** : Marge disponible sur chaque contrainte

#### 🔍 **Analyse des Contraintes**
- **`ACTIVE`** (binding) : Contrainte **saturée** - limite l'optimisation 🔴
- **`LB/UB`** : Lower/Upper Bound - bornes atteintes 📏
- **`SLACK > 0`** : Marge disponible - contrainte non saturée 🟢

#### 💰 **Valeurs Marginales (Shadow Prices)**
- **Coût marginal** : Amélioration possible si on relâche une contrainte d'1 unité
- **Contraintes saturées** : Valeur marginale élevée = goulot d'étranglement important
- **Contraintes avec slack** : Valeur marginale = 0 (pas d'amélioration immédiate)

> **💡 Astuce Pratique** : Les contraintes avec les **valeurs marginales les plus élevées** sont vos **priorités d'optimisation** - c'est là qu'investir des ressources supplémentaires aura le plus d'impact !

---

## 🔧 Installation & Configuration

### 📋 **Prérequis**
- **Python 3.9+** 
- **Git** (pour cloner le repo)

### ⚡ **Installation Rapide**
```bash
# Cloner le repository
git clone https://github.com/juliovasseur/LPSolve.git
cd LPSolve

# Installation des dépendances Python
pip install -r lp_solver_engine/requirements.txt

# Test de l'installation
make run-basic
```

### 📦 **Dépendances Principales**
- **PuLP 2.7+** : Interface de modélisation mathématique
- **CBC Solver** : Moteur d'optimisation COIN-OR (installé automatiquement)

---

## 🏆 **Performances & Limitations**

### ⚡ **Capacités Testées**
- **Variables** : Testé jusqu'à 1000+ variables continues/entières
- **Contraintes** : Testé jusqu'à 500+ contraintes linéaires
- **Temps de résolution** : <1s pour les cas d'usage fournis
- **Mémoire** : <100MB même sur les gros problèmes

### ⚠️ **Limitations Techniques**
- **Programmation linéaire uniquement** (pas de fonctions non-linéaires)
- **Interface CSV** (pas d'API REST/GraphQL)
- **Solveur CBC** (pas d'accès aux solveurs commerciaux comme Gurobi/CPLEX)

### 🎯 **Cas d'Usage Optimaux**
- ✅ Optimisation de portefeuille avec contraintes réglementaires
- ✅ Planification de production industrielle
- ✅ Allocation de ressources sous contraintes
- ✅ Problèmes de transport et logistique
- ❌ Optimisation non-linéaire (réseaux de neurones, etc.)
- ❌ Programmation stochastique avancée

---

## 📚 **Documentation Avancée**

### 🎓 **Ressources d'Apprentissage**
- **[Exemples Éducatifs](./data/basic_linear_examples/README.md)** : Concepts de base avec cas concret
- **[Production Industrielle](./data/furniture_production/README.md)** : Gestion de 70+ contraintes complexes  
- **[Finance Quantitative](./data/portfolio_optimization/README.md)** : Contraintes réglementaires et métriques de risque

### 🛠️ **Pour les Développeurs**
- **Code Source** : `lp_solver_engine/src/lpSolver/`
- **Tests** : Validation sur les 3 cas d'usage fournis
- **Extensions** : Ajout de nouveaux solveurs dans `solvers/`

### 💼 **Applications Métier**
Chaque README spécialisé contient :
- **Contexte business** détaillé
- **Analyse des contraintes** une par une
- **Interprétation des résultats** pour la prise de décision
- **Métriques de performance** sector-specific

---

## 🤝 **Contribution & Support**

### 🐛 **Signaler un Bug**
- Ouvrez une **issue GitHub** avec votre cas d'usage
- Incluez vos **fichiers CSV** et l'**erreur complète**

### 💡 **Nouvelles Fonctionnalités**
- **Fork** le projet
- Créez une **branche feature**
- **Pull Request** avec tests

### 📧 **Contact**
- **GitHub** : [@juliovasseur](https://github.com/juliovasseur)
- **Projet** : [LPSolve Repository](https://github.com/juliovasseur/LPSolve)

---

## 📜 **Licence & Crédits**

### 📋 **Licence**
**MIT License** - Libre utilisation commerciale et personnelle

### 🏆 **Technologies Utilisées**
- **[PuLP](https://pypi.org/project/PuLP/)** : Python Linear Programming Interface
- **[CBC](https://github.com/coin-or/Cbc)** : COIN-OR Branch & Cut Solver
- **[Python 3.9+](https://python.org)** : Langage de développement

### 🎯 **Inspirations Académiques**
- **Markowitz Modern Portfolio Theory** (1952)
- **Dantzig Simplex Algorithm** (1947) 
- **Asset Liability Management** principles

---

*Dernière mise à jour : Septembre 2025*

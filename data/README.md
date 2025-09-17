# 📂 Data - Cas d'Usage et Exemples

Ce dossier contient **3 niveaux de complexité croissante** pour démontrer les capacités du moteur d'optimisation quantitative.

## 🎯 Structure des Cas d'Usage

### 📊 **Basic Linear Examples** (Niveau 1 - Éducatif)
```
data/basic_linear_examples/
└── data/
    ├── variables.csv    # 2 variables simples (chaises, tables)
    ├── objectives.csv   # Maximisation profit basique
    └── constraints.csv  # 5 contraintes de ressources
```

**Objectif** : Validation des algorithmes et apprentissage des concepts de base
- **Complexité** : 2 variables, 5 contraintes
- **Temps** : <0.01s
- **Résultat** : 2,950€ de profit optimal

### 🏭 **Furniture Production** (Niveau 2 - Industriel)
```
data/furniture_production/
└── data/
    ├── variables.csv    # 56 variables (production, stocks, setup)
    ├── objectives.csv   # Maximisation profit avec coûts complexes
    └── constraints.csv  # 70+ contraintes multi-périodes
```

**Objectif** : Planification de production industrielle réaliste
- **Complexité** : 56 variables, 70+ contraintes
- **Temps** : ~0.16s
- **Résultat** : 11,293€ de profit optimal

### 💰 **Portfolio Optimization** (Niveau 3 - Finance Quantitative)
```
data/portfolio_optimization/
└── data/
    ├── variables.csv    # 33 variables (16 actifs + coûts + risque)
    ├── objectives.csv   # Utilité mean-variance sophistiquée
    └── constraints.csv  # 40+ contraintes réglementaires
```

**Objectif** : Optimisation de portefeuille financier professionnel
- **Complexité** : 33 variables, 40+ contraintes
- **Temps** : ~0.03s  
- **Résultat** : 13.64 bp/jour d'utilité espérée

## 🚀 Exécution

```bash
# Depuis le répertoire racine du projet
make run-basic      # Niveau 1 : Exemples éducatifs
make run-furniture  # Niveau 2 : Optimisation industrielle  
make run-portfolio  # Niveau 3 : Finance quantitative
```

## 📈 Progression de Complexité

| Niveau | Cas d'Usage | Variables | Contraintes | Temps | Performance |
|--------|-------------|-----------|-------------|-------|-------------|
| 1 | Basic Examples | 2 | 5 | <0.01s | 2,950€ |
| 2 | Furniture Prod | 56 | 70+ | 0.16s | 11,293€ |
| 3 | **Portfolio Finance** | **33** | **40+** | **0.03s** | **13.64 bp/j** |

## 🎓 Utilisation Pédagogique

Cette progression permet de :
- **Comprendre** les concepts sur des exemples simples
- **Appliquer** à des problèmes industriels réalistes  
- **Maîtriser** des optimisations financières complexes

Chaque niveau prépare aux compétences du suivant, offrant une **montée en compétence progressive** vers la finance quantitative professionnelle.

## 🔧 Format des Données

Tous les cas utilisent le **format CSV standardisé** :
- `variables.csv` : Définition des variables de décision
- `objectives.csv` : Fonction objectif à optimiser
- `constraints.csv` : Contraintes et limites du problème

Cette uniformité permet de **comparer les approches** et de **réutiliser le code** entre différents domaines d'application.

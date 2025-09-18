# 🎛️ LP Solver Engine

## 🏗️ Architecture du Moteur d'Optimisation

Le **LP Solver Engine** est le cœur du système d'optimisation quantitative. Il transforme des données CSV en modèles mathématiques d'optimisation et les résout avec des algorithmes de pointe.

### 📁 Structure des Modules

```
lp_solver_engine/
├── src/lpSolver/
│   ├── solvers/                    # Algorithmes d'optimisation
│   │   ├── solver_core.py          # Solveur générique LP/MILP
│   │   └── portfolio_solver.py     # Solveur spécialisé finance
│   └── utils/                      # Utilitaires et parsing
│       ├── parsing.py              # CSV → modèle mathématique
│       ├── model_arrays.py         # Structures données optimisées
│       └── modeling.py             # Construction modèles
├── main.py                         # Point d'entrée générique
├── portfolio_main.py               # Point d'entrée finance
└── requirements.txt                # Dépendances Python
```

## 🔧 Composants Principaux

### **Solvers (`solvers/`)**

#### `solver_core.py` - Solveur Générique
- Interface PuLP standardisée
- Support LP/MILP/QP
- Formatage résultats avancé
- Métriques de performance

#### `portfolio_solver.py` - Solveur Finance Spécialisé  
- Optimisation portefeuille quantitatif
- Analyse des contraintes réglementaires
- Métriques financières (Herfindahl, actifs effectifs)
- Terminologie finance quantitative

### **Utils (`utils/`)**

#### `parsing.py` - Parsing CSV
- Lecture fichiers variables.csv, objectives.csv, constraints.csv
- Validation format et cohérence
- Gestion erreurs robuste

#### `model_arrays.py` - Structures de Données
- Classe `LPModelData` optimisée
- Représentation matricielle efficace
- Interface pour solveurs

#### `modeling.py` - Construction Modèles
- Transformation données → modèles mathématiques
- Support contraintes complexes
- Optimisations numériques

## 🚀 Points d'Entrée

### `main.py` - Interface Générique
```python
# Utilisation standard pour tous types de problèmes
python main.py data/folder/
```

### `portfolio_main.py` - Interface Finance Spécialisée
```python  
# Interface optimisée pour problèmes financiers
python portfolio_main.py portfolio_optimization/data/
```

## 📊 Caractéristiques Techniques

- **Performance** : Optimisation <50ms pour problèmes complexes
- **Solveurs** : CBC (COIN-OR), interface PuLP
- **Robustesse** : Gestion contraintes infaisables
- **Scalabilité** : Support 100+ variables/contraintes  
- **Formats** : CSV standardisé, outputs formatés

## 🔍 Utilisation Avancée

### Personnalisation Solveurs
```python
from src.lpSolver.solvers import solve_lp_with_progress

# Résolution avec paramètres custom
result = solve_lp_with_progress(data, 
                               solver_params={'msg': 1, 'timeLimit': 300})
```

### Extension Nouveaux Formats
```python  
from src.lpSolver.utils import LPModelData

# Création modèle custom
data = LPModelData(variables, objectives, constraints, sense)
```

## 🛠️ Développement

### Tests
```bash
# Test tous les cas d'usage
make run-basic && make run-furniture && make run-portfolio
```

### Debugging
```bash
# Mode verbose
PULP_CBS_MSG=1 make run-portfolio
```

Cette architecture modulaire permet une extensibilité maximale tout en maintenant des performances optimales pour les applications quantitatives professionnelles.

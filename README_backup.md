# � **LPSolve** - *Moteur d'Optimisa### 🚀 *Rapide aux Cas d'Usage**

| Niveau | Cas d'Usage | Description | Accès Direct |
|--------|-------------|-------------|--------------|
| 🟢 **Débutant** | **[Exemples Éducatifs](./data/basic_linear_examples/README.md)** | Optimisation simple chaises/tables avec contrainte de marché | `make run-basic` |
| 🟡 **Intermédiaire** | **[Production Industrielle](./data/furniture_production/README.md)** | Planification complexe avec 70+ contraintes (ESG, setup, pénalités) | `make run-furniture` |
| 🔴 **Expert** | **[Finance Quantitative](./data/portfolio_optimization/README.md)** | Portefeuille 16 actifs, contraintes réglementaires, logique type ALM | `make run-portfolio` |

> **💡 Conseil** : Commencez par les exemples éducatifs pour comprendre les concepts, puis progressez vers la finance quantitative.néaire*
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

Le processus d'optimisation suit une logique claire :
1. **Ingestion** : Données structurées (CSV normalisés)
2. **Modélisation** : Construction automatique du modèle mathématique  
3. **Résolution** : Algorithmes d'optimisation (CBC/COIN-OR)
4. **Analyse** : Décisions quantifiées avec justifications

### 🎓 **Accessible à Tous**
- **Non-financiers** : Tous les termes techniques expliqués (ALM, basis points, etc.)
- **Non-mathématiciens** : Concepts d'optimisation linéaire vulgarisés
- **Interface intuitive** : CSV en entrée, résultats détaillés en sortie
- **Reproductible** : Versionning Git, environnement isolé

### � **Cas d'Usage Principaux**

1. **📚 Exemples Éducatifs** - Validation des concepts d'optimisation linéaire
2. **🏭 Optimisation Industrielle** - Planification de production avec analyse des goulots  
3. **💼 Finance Quantitative** - Optimisation de portefeuille avec contraintes réglementaires, calcul des **valeurs marginales** et gestion des **coûts de transaction**

> **🎓 Terminologie technique** : **Valeurs marginales** (shadow prices des contraintes saturées), **coûts de transaction** (en basis points), **contraintes réglementaires** (limites sectorielles et de concentration).

---

### 🏗️ **Structure Technique Simplifiée**

```
Quant_git/
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

## 🏗️ **Architecture du Système**

### 🎯 **Approche Modulaire par Niveaux de Complexité**

Le système suit une **architecture en couches**, inspirée des principes ALM et d'analyse PnL, sans pour autant calculer explicitement ces métriques. L'idée est de structurer l'optimisation selon une **logique financière progressive** :

#### 📊 **Trois Cas d'Usage Disponibles**

1. **[📚 Exemples Éducatifs](./data/basic_linear_examples/README.md)** - Concepts fondamentaux d'optimisation linéaire (production chaises/tables)

2. **[🏭 Optimisation Industrielle](./data/furniture_production/README.md)** - Planification complexe multi-contraintes (70+ contraintes de production)

3. **[💼 Finance Quantitative](./data/portfolio_optimization/README.md)** - Optimisation de portefeuille suivant une logique inspirée d'ALM avec contraintes réglementaires

> **🎓 Note sur la terminologie** : Le système calcule les **valeurs marginales** (shadow prices) et **coûts de transaction**, mais ne produit pas d'analyse PnL ou ALM complète. Il suit cependant une **logique similaire** dans l'approche d'optimisation.

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

### 🛠️ **Créer Votre Propre Cas d'Usage (En 2 Minutes !)**

Vous voulez résoudre VOTRE problème d'optimisation ? Rien de plus simple !

#### 🚀 **Méthode Rapide avec Template**
```bash
# Créer un nouveau cas d'usage basé sur le template
make create-case NAME=mon_projet

# Cela crée automatiquement :
# data/mon_projet/
#   ├── data/
#   │   ├── variables.csv      (template pré-rempli)
#   │   ├── objectives.csv     (template pré-rempli)  
#   │   └── constraints.csv    (template pré-rempli)
#   └── README.md              (template documentation)
```

#### 📝 **Personnaliser Vos Données**
1. **Éditez `variables.csv`** : Définissez vos variables de décision
2. **Éditez `objectives.csv`** : Définissez ce que vous voulez optimiser
3. **Éditez `constraints.csv`** : Ajoutez vos contraintes métier

#### 🎯 **Exécuter Votre Optimisation**
```bash
# Exécuter votre cas d'usage personnalisé
make run-custom CASE=mon_projet

# Ou directement
python lp_solver_engine/main.py --case=mon_projet
```

> **💡 Pro Tip** : Commencez par dupliquer un cas existant (`basic_linear_examples`) et modifiez progressivement !

### ⚡ **Commandes Rapides**

```bash
# 📊 Installation et configuration
make install

# 🎓 Exemples éducatifs (validation)  
make run-basic

# 🏭 Optimisation industrielle (production meubles)
make run-furniture  

# 💰 Finance quantitative (portfolio optimization)
make run-portfolio
```

### � **Focus sur l'Exemple Éducatif (Basic Examples)**

L'exemple éducatif de **production de meubles** illustre parfaitement les concepts d'optimisation avec des **contraintes de marché réalistes** :

#### 🎯 **Problème d'Optimisation**
- **Variables** : Chaises (`x_chairs`) et Tables (`x_tables`)
- **Objectif** : Maximiser le profit (30€/chaise + 50€/table)
- **Contraintes** : Ressources (menuiserie, assemblage, bois) + demandes min/max

#### 🔍 **Contrainte Clé : Limite de Demande Maximale**
```bash
# Nouvelle contrainte ajoutée
max_chairs: x_chairs ≤ 25
```

**Rationale économique** : Même si les chaises sont plus rentables par unité de ressource, la demande du marché est limitée à 25 unités maximum. Cette contrainte force une **réallocation optimale** des ressources vers les tables.

#### 📊 **Impact de la Contrainte**
- **Sans limite** : 90 chaises + 5 tables = 2,950€
- **Avec limite** : 25 chaises + 37.5 tables = 2,625€
- **Perte** : -325€ (-11%) due aux contraintes de marché

> 💡 **Leçon économique** : L'optimisation mathématique doit intégrer les réalités du marché. Une solution théoriquement optimale peut être commercialement impossible.

### �📈 **Exemple de Sortie Portfolio**

```
================================================================================
    🏛️  OPTIMISEUR DE PORTEFEUILLE QUANTITATIF v2.1
    📊  Mean-Variance Optimization avec contraintes réglementaires
================================================================================

✅ SOLUTION OPTIMALE TROUVÉE
📈 Utilité espérée: 13.6430 bp/jour
⏱️  Temps d'optimisation: 0.033s

💼 ALLOCATION OPTIMALE DU PORTEFEUILLE:
  📱 Technology & Communication Services (60.0%):
    • MSFT: 14.00% ($140,000)
    • GOOGL: 12.00% ($120,000) 
    • AMZN: 12.00% ($120,000)
    • NVDA: 10.00% ($100,000)
    [...]

🚨 ANALYSE DES CONTRAINTES RÉGLEMENTAIRES:
  🔴 CONTRAINTES SATURÉES (Goulots):
    • fully_invested (Contrainte budgétaire): SATURÉE
    • mega_cap_minimum (Allocation large caps): SATURÉE
    [...]

📊 MÉTRIQUES DE RISQUE & PERFORMANCE:
  📈 Indice Herfindahl: 0.0950 (Concentration modérée)
  🎯 Nombre effectif d'actifs: 10.5
  💻 Exposition Technology: 60.0% (SURPONDÉRATION)
```

---

## � **Guide d'Interprétation des Résultats**

### 🔍 **Comprendre l'Output du Programme**

Voici l'explication détaillée de tous les termes techniques affichés lors de l'exécution :

#### � **Résultat Principal (Pour Tout le Monde)**
```bash
✅ SOLUTION OPTIMALE TROUVÉE
📈 Utilité espérée: 2.4620 bp/jour  
⏱️  Temps d'optimisation: 0.032s
```

**🎓 Explication finance-friendly :**
- **Solution optimale** = Meilleure décision possible sous toutes les contraintes
- **2.46 bp/jour** = **Basis points** = 0.0246% de rendement par jour ≈ **9% annualisé**
- **0.032s** = Temps de calcul ultrarapide (production-ready)

#### 📊 **Variables de Décision (Cœur des Résultats)**
```bash
📊 Variables de décision:
  • w_MSFT = 0.14  [lb=0.0, ub=0.15]
  • w_GOOGL = 0.12  [lb=0.0, ub=0.12]
```

**🎓 Terminologie démystifiée :**
- **w_MSFT = 0.14** = Investir **14%** du portefeuille dans Microsoft  
- **lb=0.0** = **Lower Bound** = Minimum 0% (pas d'obligation d'investir)
- **ub=0.15** = **Upper Bound** = Maximum 15% (limite réglementaire)

#### 🔗 **Contraintes (Le Plus Important à Comprendre !)**
```bash
🔗 Contraintes (slacks):
  • fully_invested (==): slack=0 [ACTIVE]
  • tech_concentration (<=): slack=0.05 [OK] 
  • mega_cap_minimum (>=): slack=0 [ACTIVE]
```

**🎓 Guide complet des statuts :**

🔴 **`[ACTIVE]` / `slack=0`** - **Contrainte saturée (goulot)**
- La contrainte est utilisée à 100% de sa capacité
- **Critique** : Limite directement la performance
- Exemple : `cap_carp_w1: 240h utilisées sur 240h disponibles`

🟢 **`[OK]` / `slack>0`** - **Contrainte avec marge**  
- La contrainte n'est pas limitante
- `slack` = marge disponible non utilisée
- Exemple : `cap_asm_w1: slack=52` → 52h d'assemblage restantes

**Types d'opérateurs :**
- **`(<=)`** : Contrainte de capacité maximum
- **`(>=)`** : Contrainte de minimum requis  
- **`(==)`** : Contrainte d'égalité exacte (souvent équilibrage)

#### ⚙️ **Informations Techniques**
```bash
🔧 Interface: PuLP (Python Linear Programming)
⚙️ Solveur: CBC (COIN-OR Branch & Cut)
⏱️ Temps de résolution: 0.170s
```

**Composants :**
- **PuLP** : Interface Python pour la modélisation
- **CBC** : Moteur d'optimisation (open source, très performant)
- **Branch & Cut** : Algorithme pour problèmes mixtes entiers

#### 🎯 **Métriques de Performance**
```bash
📊 MODÈLE PARSÉ
• Variables: 56
• Contraintes: 70  
• Types: 44 integer, 12 binary
```

**Complexité du modèle :**
- **Variables** : Nombre de décisions à optimiser
- **Contraintes** : Nombre de limites/règles à respecter
- **Integer** : Variables entières (quantités de production)
- **Binary** : Variables 0/1 (choix oui/non, setups)

### 🚨 **Analyse des Goulots d'Étranglement**

#### 🔴 **Contraintes Critiques (ACTIVE)**
- **Impact** : Limitent directement le profit maximum
- **Action** : Investir pour augmenter ces capacités
- **Exemple** : Menuiserie saturée → recruter menuisiers ou acheter machines

#### 🟡 **Contraintes Proches de la Saturation (slack faible)**
- **Surveillance** : Risque de devenir critiques
- **Planification** : Prévoir montée en charge

#### 🟢 **Ressources Excédentaires (slack élevé)**
- **Opportunité** : Capacités sous-utilisées
- **Réallocation** : Possible réduction de coûts ou réorientation

### 💡 **Interprétation Business**

#### 📈 **Pour Maximiser les Profits**
1. **Éliminer les goulots** : Focus sur les contraintes `[ACTIVE]`
2. **Exploiter les marges** : Utiliser les ressources avec `slack` élevé
3. **Optimiser le mix** : Favoriser les produits à haute marge dans les limites

#### 🔍 **Signaux d'Alerte**
- **Trop de contraintes actives** : Modèle très contraint, peu de flexibilité
- **Temps de résolution élevé** : Problème trop complexe, simplification nécessaire
- **Solution non trouvée** : Contraintes contradictoires (infaisabilité)

---

## �🛠️ Configuration Technique

### 📦 **Dépendances**

- **Python 3.9+** (Typing hints, f-strings avancées)
- **PuLP 2.7+** (Interface programmation linéaire)  
- **CBC Solver** (COIN-OR Branch & Cut)
- **Pandas** (Manipulation données financières)
- **NumPy** (Calculs matriciels optimisés)

### 🔧 **Installation**

```bash
# Clone du repository
git clone https://github.com/juliovasseur/Quant_training.git
cd Quant_training

# Configuration environnement Python
python -m venv .venv
source .venv/bin/activate  # macOS/Linux
# .venv\Scripts\activate   # Windows

# Installation dépendances
pip install -r lp_solver_engine/requirements.txt

# Test de fonctionnement
make run-portfolio
```

---

## 📚 Applications et Cas d'Usage

### 1. 🎓 **Formation Quantitative**
- Apprentissage programmation linéaire
- Validation algorithmes d'optimisation  
- Comparaison performances solveurs

### 2. 🏦 **Asset Management**
- Construction portefeuilles institutionnels
- Respect contraintes réglementaires (UCITS, MIFID)
- Optimisation risk-adjusted returns

### 3. 🔬 **Recherche Quantitative**  
- Backtesting stratégies d'allocation
- Analyse factorielle (momentum, value, quality)
- Modélisation coûts de transaction

### 4. 🎯 **Trading Quantitatif**
- Allocation tactique d'actifs
- Rebalancing optimal avec contraintes
- Gestion exposition sectorielle

---

## 🏆 Résultats et Performance

### 📊 **Benchmarks de Performance**

| Cas d'Usage | Variables | Contraintes | Temps (CBC) | Profit Optimal |
|-------------|-----------|-------------|-------------|----------------|
| Basic Examples | 2 | 6 | <0.01s | 2,625€ |
| Furniture Production | 32 | 70+ | 0.02s | 11,293€ |
| **Portfolio Finance** | **77** | **40+** | **0.033s** | **13.64 bp/jour** |

### 🎯 **Métriques Qualité**

- ✅ **Convergence** : 100% sur tous les cas de test
- ⚡ **Performance** : <50ms pour problèmes complexes
- 🎲 **Robustesse** : Gestion contraintes infaisables
- 📋 **Compliance** : Respect total contraintes réglementaires



## 👥 Contribution et Support

### 🤝 **Contribution**

Ce projet est ouvert aux contributions ! Domaines d'intérêt :

- 🔧 **Nouveaux solveurs** (Gurobi, CPLEX, SCIP)
- 📊 **Nouvelles métriques** (Sharpe, Sortino, Calmar)
- 🏦 **Cas d'usage finance** (credit risk, market making)
- 📈 **Visualisations** (efficient frontier, factor decomposition)

### 📞 **Contact & Support**

- **GitHub** : [juliovasseur/Quant_training](https://github.com/juliovasseur/Quant_training)
- **Issues** : Signalement bugs et feature requests
- **Wiki** : Documentation technique approfondie

---

## 📜 License & Remerciements

**MIT License** - Utilisation libre pour recherche et applications commerciales

### 🙏 **Acknowledgments**

- **PuLP Team** - Excellent package d'optimisation Python
- **COIN-OR Foundation** - Solveur CBC open-source performant
- **Python Community** - Écosystème scientifique exceptionnel

---

## 📈 Showcase Technique

> Ce projet démontre une **maîtrise approfondie** de :
> - 🔢 **Programmation linéaire avancée** (dualité, analyse de sensibilité)
> - 💰 **Finance quantitative** (Markowitz, risk parity, factor models)
> - 🛠️ **Ingénierie logicielle** (architecture modulaire, tests, documentation)
> - 📊 **Optimisation numérique** (algorithmes Branch & Cut, performance)

**Parfait pour démontrer ses compétences techniques lors d'entretiens quantitatifs chez des hedge funds, asset managers, ou fintechs !** 🚀

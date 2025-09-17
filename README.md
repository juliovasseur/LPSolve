# 🏛️ Quantitative Finance Optimization Suite
## Système d'Optimisation de Portefeuille avec Programmation Linéaire Avancée

[![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)](https://python.org)
[![PuLP](https://img.shields.io/badge/PuLP-2.7+-green.svg)](https://pypi.org/project/PuLP/)
[![CBC](https://img.shields.io/badge/CBC-COIN--OR-orange.svg)](https://github.com/coin-or/Cbc)
[![License](https://img.shields.io/badge/License-MIT-red.svg)](LICENSE)

> **Projet de finance quantitative professionnelle** développant un moteur d'optimisation de portefeuille utilisant la programmation linéaire mixte pour résoudre des problèmes complexes d'allocation d'actifs avec contraintes réglementaires.

---

## 🎯 Vue d'ensemble du Projet

Ce projet implémente un **système d'optimisation quantitative avancé** qui transforme des données financières CSV en modèles mathématiques d'optimisation, résolus avec des algorithmes de pointe (CBC/COIN-OR). Le système couvre trois niveaux de complexité croissante, du prototypage éducatif aux applications professionnelles de gestion d'actifs.

### 🚀 Cas d'Usage Principaux

1. **📚 Exemples Éducatifs** - Validation des algorithmes d'optimisation
2. **🏭 Optimisation Industrielle** - Planification de production multi-périodes  
3. **💼 Finance Quantitative** - Optimisation de portefeuille avec contraintes réglementaires

---

## 🏗️ Architecture du Système

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

## 💼 Système de Portfolio Quantitatif (Niveau Expert)

### 🎯 Caractéristiques Financières Avancées

Notre **optimiseur de portefeuille quantitatif** implémente un modèle de Markowitz sophistiqué avec:

#### 📈 **Univers d'Investissement**
- **16 actifs US** : AAPL, MSFT, GOOGL, AMZN, TSLA, NVDA, META, NFLX, JPM, BAC, GS, MS, JNJ, PFE, UNH, PG
- **Classification GICS** : Technology, Financials, Healthcare, Consumer Defensive
- **Capitalisation** : Large caps et mega caps ($100B+)

#### ⚖️ **Contraintes Réglementaires (40+ contraintes)**
- **UCITS Compliance** : Limites de concentration par émetteur (5%, 10%)
- **Limites sectorielles** : Tech ≤65%, Financials ≤35%, Healthcare ≤25%
- **Gestion du risque** : High-beta ≤25%, Low-beta ≥15%
- **Liquidité** : Contraintes ADV, limites positions illiquides
- **ESG** : Exclusions tabac, seuils de compliance

#### 🔢 **Modélisation Mathématique**
- **Variables** : 77 variables d'optimisation (poids + coûts de transaction + risque)
- **Contraintes** : 40 contraintes linéaires et quadratiques
- **Objectif** : Maximisation utilité espérée (68 termes) 
- **Solveur** : CBC (Branch & Cut) via interface PuLP

### 📊 **Métriques Quantitatives**

Le système calcule automatiquement :

- **🎯 Utilité Espérée** : Rendement ajusté au risque (basis points/jour)
- **📈 Indice Herfindahl** : Mesure de concentration du portefeuille
- **🔢 Actifs Effectifs** : Diversification effective (1/Σwi²)
- **⚠️ Analyse des Contraintes** : Identification des goulots d'étranglement
- **📋 Valeurs Marginales** : Dual values pour optimisation des contraintes

### 🚨 **Analyse des Goulots (Bottleneck Analysis)**

Le rapport identifie :
- **🔴 Contraintes Saturées** : Goulots limitant la performance
- **🟡 Contraintes à Risque** : Proches de la saturation
- **🟢 Contraintes avec Marge** : Capacité d'optimisation restante

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

#### 📊 **Section "Variables de décision"**
```bash
• prod_CH_w1 = 20  [lb=0.0, ub=inf]
• setup_TA_w2 = 1  [lb=0, ub=1]
```

**Terminologie :**
- **Valeur optimale** : `20` = solution trouvée par le solveur
- **`lb` (Lower Bound)** : Borne inférieure (minimum autorisé)
- **`ub` (Upper Bound)** : Borne supérieure (maximum autorisé)
- **`inf`** : Infini (pas de limite supérieure)

#### 🔗 **Section "Contraintes (slacks)"**
```bash
• cap_carp_w1 (<=): slack=0 [ACTIVE]
• cap_asm_w1 (<=): slack=52 [OK]
• invbal_CH_w1 (==): slack=0 [ACTIVE]
```

**Statuts des contraintes :**

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

---

## 🚀 Développements Futurs

### 📅 **Roadmap Technique**

- [ ] **Intégration données temps réel** (API Bloomberg/Reuters)
- [ ] **Optimisation portfolio robuste** (CVaR, worst-case)  
- [ ] **Machine Learning** (prédiction rendements/volatilité)
- [ ] **Interface web** (dashboard interactif)
- [ ] **Parallélisation** (optimisation multi-threaded)

### 🔬 **Extensions Recherche**

- [ ] **Alternative Risk Premia** (momentum, carry, value)  
- [ ] **ESG Integration** (scoring carbone, impact social)
- [ ] **Options Strategies** (portfolio avec dérivés)
- [ ] **Multi-Asset** (actions, obligations, crypto, commodities)

---

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

# 🏛️ Optimisation de Portefeuille Quantitatif

## 🎯 Description

Système d'optimisation de portefeuille financier avancé utilisant la **programmation linéaire mixte** pour résoudre des problèmes d'allocation d'actifs avec contraintes réglementaires complexes.

## 📊 Caractéristiques du Modèle

### **Univers d'Investissement**
- **16 actifs US** : AAPL, MSFT, GOOGL, AMZN, TSLA, NVDA, META, NFLX, JPM, BAC, GS, MS, JNJ, PFE, UNH, PG
- **Classification GICS** : Technology (50%), Financials (25%), Healthcare (19%), Consumer Defensive (6%)
- **Capitalisation** : Large caps et mega caps ($100B+)

### **Contraintes Réglementaires (40+)**
- **UCITS Compliance** : Limites de concentration par émetteur 
- **Limites sectorielles** : Tech ≤65%, Financials ≤35%, Healthcare ≤25%
- **Gestion du risque** : High-beta ≤25%, Low-beta ≥15%
- **Liquidité** : Contraintes ADV, limites positions illiquides
- **ESG** : Seuils de compliance environnementale

### **Modélisation Mathématique**
- **Variables** : 33 variables d'optimisation (poids + coûts + risque)
- **Contraintes** : 40 contraintes linéaires 
- **Objectif** : Maximisation utilité espérée (33 termes)
- **Solveur** : CBC (Branch & Cut) via PuLP

## 🚀 Exécution

```bash
# Depuis le répertoire racine
make run-portfolio
```

## 📈 Résultats Typiques

- **Utilité Espérée** : ~13.64 bp/jour
- **Concentration** : Indice Herfindahl = 0.095 (modérée)
- **Diversification** : 10.5 actifs effectifs
- **Exposition Technology** : 60% (surpondération stratégique)
- **Performance** : Optimisation en <50ms

## 🔧 Structure des Données

- `variables.csv` - Définition des 16 actifs avec bounds
- `objectives.csv` - Fonction d'utilité mean-variance  
- `constraints.csv` - 40+ contraintes réglementaires

## 💼 Applications Professionnelles

- **Asset Management** : Construction portefeuilles institutionnels
- **Risk Management** : Respect contraintes réglementaires 
- **Quantitative Research** : Backtesting stratégies d'allocation
- **Trading** : Rebalancing optimal avec contraintes

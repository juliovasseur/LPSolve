# Exemple Simple d'Optimisation Linéaire: Production de Meubles

## Description du Problème

Ce cas pratique illustre un **problème d'optimisation linéaire classique** de production industrielle, facilement vérifiable mathématiquement.

### Contexte
Une entreprise de meubles produit deux types de produits:
- **Chaises** (variable `x_chairs`)
- **Tables** (variable `x_tables`)

### Fonction Objectif
**Maximiser le profit total:**
```
Profit = 30€ × x_chairs + 50€ × x_tables
```

### Contraintes de Ressources

1. **Temps de menuiserie** (200h disponibles):
   ```
   2h/chaise × x_chairs + 4h/table × x_tables ≤ 200h
   ```

2. **Temps d'assemblage** (120h disponibles):
   ```
   1h/chaise × x_chairs + 2h/table × x_tables ≤ 120h
   ```

3. **Matériau bois** (180m² disponibles):
   ```
   1m²/chaise × x_chairs + 3m²/table × x_tables ≤ 180m²
   ```

4. **Demande minimale chaises** (au moins 10):
   ```
   x_chairs ≥ 10
   ```

5. **Demande minimale tables** (au moins 5):
   ```
   x_tables ≥ 5
   ```

6. **Bornes des variables**:
   ```
   0 ≤ x_chairs ≤ 100
   0 ≤ x_tables ≤ 50
   ```

## Solution Optimale Obtenue

**Résultat du solveur:**
- **x_chairs = 90** (produire 90 chaises)
- **x_tables = 5** (produire 5 tables)  
- **Profit maximum = 2950€**

### Vérification Mathématique des Contraintes
- **Profit**: 30×90 + 50×5 = 2700 + 250 = **2950€** ✓
- **Menuiserie**: 2×90 + 4×5 = 180 + 20 = **200h** ≤ 200h ✓ (saturée)
- **Assemblage**: 1×90 + 2×5 = 90 + 10 = **100h** ≤ 120h ✓  
- **Bois**: 1×90 + 3×5 = 90 + 15 = **105m²** ≤ 180m² ✓
- **Min chaises**: 90 ≥ 10 ✓
- **Min tables**: 5 ≥ 5 ✓ (saturée)

### Analyse Économique
- La contrainte de **menuiserie** est le goulot d'étranglement (saturée à 200h)
- La contrainte de **demande minimale tables** est aussi saturée (exactement 5 tables)
- Il reste 20h d'assemblage et 75m² de bois non utilisés

## Utilisation

```bash
make run-basic
```

## Pourquoi cet exemple est excellent

Cette modification rend le problème:
- ✅ **Mathématiquement simple** à comprendre et vérifier
- ✅ **Concret** (production de meubles réaliste)
- ✅ **Facilement validable** (calculs manuels possibles)
- ✅ **Pédagogique** (exemple classique d'optimisation linéaire)
- ✅ **Solution non-triviale** (mélange optimal des deux produits)
- ✅ **Contraintes actives identifiables** (menuiserie et demande minimale tables)

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

6. **Demande maximale chaises** (limite du marché à 25):
   ```
   x_chairs ≤ 25
   ```
   > **Rationale économique**: Même si les chaises sont plus rentables par unité de menuiserie, 
   > la demande du marché est limitée à 25 unités. Au-delà, les chaises ne seraient pas vendues.

7. **Bornes des variables**:
   ```
   0 ≤ x_chairs ≤ 100
   0 ≤ x_tables ≤ 50
   ```

## Solution Optimale Obtenue

**Résultat du solveur:**
- **x_chairs = 25** (produire 25 chaises)
- **x_tables = 37.5** (produire 37.5 tables)  
- **Profit maximum = 2625€**

### Vérification Mathématique des Contraintes
- **Profit**: 30×25 + 50×37.5 = 750 + 1875 = **2625€** ✓
- **Menuiserie**: 2×25 + 4×37.5 = 50 + 150 = **200h** ≤ 200h ✓ (saturée)
- **Assemblage**: 1×25 + 2×37.5 = 25 + 75 = **100h** ≤ 120h ✓  
- **Bois**: 1×25 + 3×37.5 = 25 + 112.5 = **137.5m²** ≤ 180m² ✓
- **Min chaises**: 25 ≥ 10 ✓
- **Min tables**: 37.5 ≥ 5 ✓
- **Max chaises**: 25 ≤ 25 ✓ (saturée)

### Analyse Économique
🎯 **Impact de la contrainte de demande maximale:**
- **Avant**: 90 chaises + 5 tables = 2950€ de profit
- **Après**: 25 chaises + 37.5 tables = 2625€ de profit
- **Perte**: -325€ (-11%) due à la limite de marché sur les chaises

🔍 **Contraintes actives (goulots):**
- **Menuiserie** (200h): Saturée - limite la production totale
- **Demande max chaises** (25): Saturée - force à produire plus de tables

📈 **Réallocation optimale des ressources:**
- Moins de chaises (plus rentables par unité) mais limitées par la demande
- Plus de tables (moins rentables par unité) pour utiliser les ressources disponibles
- Il reste 20h d'assemblage et 42.5m² de bois non utilisés

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

# 📚 Exemple Éducatif d'**Optimisation Linéaire** : Production de Meubles

## 🎯 **Description du Problème - Accessible à Tous**

Ce cas pratique illustre un **problème d'optimisation linéaire classique** de production industrielle, parfait pour comprendre les concepts fondamentaux de l'**optimisation sous contraintes**.

> **🎓 Qu'est-ce que l'optimisation linéaire ?** C'est une méthode mathématique pour trouver la **meilleure solution** (ex: maximum de profit) quand on a des **limites à respecter** (ex: budget, temps, ressources).

### 🏭 **Contexte Business Simple**

Une entreprise de meubles doit décider combien produire de chaque produit pour **maximiser son profit** :
- **🪑 Chaises** : 45€ de profit par unité (variable `x_chairs`)
- **🪑 Tables** : 50€ de profit par unité (variable `x_tables`)

### 🎯 **Fonction Objectif** (Ce qu'on veut optimiser)
**Maximiser le profit total :**
```mathematica
Profit = 45€ × nombre_chaises + 50€ × nombre_tables
```

> **💡 En termes simples** : On cherche le nombre optimal de chaises et tables à produire pour gagner le maximum d'argent possible.

### ⚖️ **Contraintes** (Limites à respecter)

> **🎓 Contraintes ?** Ce sont les **limites imposées** par la réalité : budget, temps, matériaux, demande du marché, etc.

#### 🏭 **Ressources Limitées de Production**

1. **🔨 Atelier Menuiserie** (240h disponibles/semaine) :
   ```
   3h/chaise + 5h/table ≤ 240h maximum
   ```
   > *Chaque chaise prend 3h, chaque table 5h de menuiserie*

2. **🔧 Atelier Assemblage** (120h disponibles/semaine) :
   ```
   1h/chaise + 2h/table ≤ 120h maximum  
   ```
   > *Chaque chaise prend 1h, chaque table 2h d'assemblage*

3. **🌳 Matériau Bois** (200m² disponibles/semaine) :
   ```
   2m²/chaise + 4m²/table ≤ 200m² maximum
   ```
   > *Chaque chaise nécessite 2m², chaque table 4m² de bois*

4. **📊 Limite Marché Chaises** (max 50 unités/semaine) :
   ```
   x_chairs ≤ 50
   ```
   > *Demande du marché limitée à 50 chaises par semaine*

5. **Bornes des variables** (production entière seulement) :
   ```
   0 ≤ x_chairs ≤ 100 (entiers)
   0 ≤ x_tables ≤ 100 (entiers)
   ```
   > **Note importante** : On utilise la Programmation Linéaire en Nombres Entiers pour des unités de production réalistes !

## 🎯 **Solution Optimale - Résultat Data-Driven**

### 💰 **Décision Optimale du Solveur :**
- **🪑 Chaises = 50 unités** (maximum marché)
- **🪑 Tables = 18 unités** (capacité restante)  
- **💰 Profit maximum = 3,150€/semaine**

### 🔍 **Vérification des Calculs** (Transparence totale)
- **💰 Profit** : 45€×50 + 50€×18 = 2,250€ + 900€ = **3,150€** ✅
- **🔨 Menuiserie** : 3h×50 + 5h×18 = 150h + 90h = **240h/240h** ✅ **[SATURÉE]**
- **🔧 Assemblage** : 1h×50 + 2h×18 = 50h + 36h = **86h/120h** ✅ (34h libres)
- **🌳 Bois** : 2m²×50 + 4m²×18 = 100m² + 72m² = **172m²/200m²** ✅ (28m² libres)  
- **📊 Limite Chaises** : 50 ≤ 50 ✅ **[SATURÉE]**

**C'est un problème de Programmation Linéaire en Nombres Entiers (PLNE)** - on ne peut produire que des unités entières de meubles.

### 💡 **Leçons Business Importantes**

#### 🎯 **Insight #1 : Prioriser les Produits les Plus Rentables**
- **Chaises plus rentables par heure** : 45€ ÷ 3h = **15€/h menuiserie**
- **Tables moins rentables par heure** : 50€ ÷ 5h = **10€/h menuiserie**  
- **Stratégie** : Produire d'abord le maximum de chaises, puis compléter avec des tables

#### 🎯 **Insight #2 : Les Contraintes Saturées Montrent les Vrais Goulots**
- **Menuiserie** = SATURÉE (240h utilisées exactement) → **Ressource critique**
- **Marché Chaises** = SATURÉ (50 unités max atteintes) → **Limitation commerciale**
- **Assemblage** = marge (34h inutilisées) → **Capacité excédentaire**
- **Bois** = marge (28m² inutilisés) → **Approvisionnement suffisant**

💡 Pour augmenter le profit : **Développer la capacité menuiserie** ou **développer le marché des chaises** !

#### 🎯 **Insight #3 : Allocation Optimale des Ressources**
```
Mix de production intelligent :
• x₁ (chaises) = 50 unités → 2,250€ (71% du profit)
• x₂ (tables) = 18 unités → 900€ (29% du profit)
Profit total = 3,150€ grâce à l'allocation optimale des ressources
```

---

## 🚀 **Exécution**

```bash
make run-basic
```

---

## 🎓 **Pourquoi cet Exemple est Parfait pour Apprendre ?**

### ✅ **Accessible à Tous**
- **Contexte familier** : Production de meubles (tout le monde comprend)
- **Calculs simples** : Vérification manuelle possible
- **Contraintes réalistes** : Temps, matériaux, limites de marché

### ✅ **Concepts Clés Illustrés**
- **🎯 Optimisation** : Trouver le maximum de profit sous contraintes
- **⚖️ Arbitrages** : Équilibrer différents produits de manière optimale
- **📊 Contraintes saturées** : Identifier les vrais goulots d'étranglement
- **💡 Intuition économique** : Pourquoi optimal ≠ intuitif

### ✅ **Pertinence Professionnelle**
- **📈 Planification de production** : Prise de décision industrielle réelle
- **💼 Allocation de ressources** : Maximiser le ROI sous contraintes
- **🎯 Analyse des goulots** : Concentrer les efforts d'amélioration
- **📊 Décisions data-driven** : Les chiffres plutôt que l'intuition

L'optimisation révèle la puissance de la **pensée mathématique** : l'intuition pourrait dire "produire des quantités égales" mais les maths montrent que **50+18 bat n'importe quel mix équilibré** !

---

## 📋 **Structure des Fichiers**

```
data/basic_linear_examples/
├── README.md                 # Cette documentation
├── data/
│   ├── objectives.csv        # Coefficients de profit (45€, 50€)
│   ├── constraints.csv       # Limites de ressources et contraintes marché
│   └── variables.csv         # Variables de production (entières)
```

**Modèle Mathématique** : 2 variables, 4 contraintes, formulation en programmation linéaire entière avec solution optimale **50 chaises + 18 tables = 3,150€** de profit.

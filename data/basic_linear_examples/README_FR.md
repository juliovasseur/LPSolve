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
   4h/chaise + 4h/table ≤ 240h maximum
   ```
   > *Chaque chaise prend 4h, chaque table 4h de menuiserie*

2. **🔧 Atelier Assemblage** (240h disponibles/semaine) :
   ```
   2h/chaise + 4h/table ≤ 240h maximum  
   ```
   > *Chaque chaise prend 2h, chaque table 4h d'assemblage*

3. **� Atelier Finition** (240h disponibles/semaine) :
   ```
   3h/chaise + 4h/table ≤ 240h maximum
   ```
   > *Chaque chaise prend 3h, chaque table 4h de finition*

4. **📦 Espace de Stockage** (80 unités max/semaine) :
   ```
   1 unité/chaise + 1 unité/table ≤ 80 unités maximum
   ```

5. **Bornes des variables** (production entière seulement):
   ```
   0 ≤ x_chairs ≤ 100 (entiers)
   0 ≤ x_tables ≤ 100 (entiers)
   ```
   > **Note importante**: On utilise la programmation linéaire en nombres entiers car on ne peut pas produire 37.5 tables dans la réalité !

## 🎯 **Solution Optimale - Résultat Data-Driven**

### 💰 **Décision Optimale du Solveur (Programmation Linéaire Entière) :**
- **🪑 Chaises = 30 unités** (solution entière optimale)
- **🪑 Tables = 30 unités** (solution entière optimale)  
- **💰 Profit maximum = 2,850€/semaine**

### 🔍 **Vérification des Calculs** (Transparence totale)
- **💰 Profit**: 45€×30 + 50€×30 = 1,350€ + 1,500€ = **2,850€** ✅
- **🔨 Menuiserie**: 4h×30 + 4h×30 = 120h + 120h = **240h/240h** ✅ **[SATURÉE]**
- **🔧 Assemblage**: 2h×30 + 4h×30 = 60h + 120h = **180h/240h** ✅ (60h libres)
- **� Finition**: 3h×30 + 4h×30 = 90h + 120h = **210h/240h** ✅ (30h libres)
- **📦 Stockage**: 1×30 + 1×30 = 30 + 30 = **60/80 unités** ✅ (20 unités libres)
- **📊 Demande chaises**: 25 ≤ 25 ✅ **[CONTRAINTE ACTIVE]**

### 🚨 **Analyse des Goulots d'Étranglement**

#### 🔴 **Contraintes Saturées (Goulots critiques)**
1. **🔨 Menuiserie** : 100% utilisée (200h/200h)
   - **Impact** : Principal **goulot limitant** la production
   - **Décision** : Investir en priorité dans cet atelier pour croître

2. **📊 Production Équilibrée** : Solution entière optimale (30+30)
   - **Impact** : Contrainte menuiserie détermine le mix optimal
   - **Décision** : Augmenter capacité menuiserie pour plus de profit
- **Production chaises**: 30 unités (solution entière)
- **Production tables**: 30 unités (solution entière)

#### 🟢 **Ressources Sous-Utilisées (Capacité libre)**
- **🔧 Assemblage** : 60h libres/semaine (25% capacité excédentaire)
- **� Finition** : 30h libres/semaine (12.5% capacité excédentaire)
- **📦 Stockage** : 20 unités libres/semaine (25% capacité excédentaire)

### 💡 **Leçons Business Importantes**

#### 🎯 **Insight #1 : Les Contraintes Entières Sont la Réalité**
- **Relaxation continue** : 25 chaises + 37.5 tables = 2,625€ (théorique)
- **Programmation entière** : 30 chaises + 30 tables = 2,850€ (production réelle)
- **Impact** : +225€ (+8.6%) **car la solution entière trouve un meilleur point réalisable**

#### 🏭 **Insight #2 : Identifier les Vrais Goulots**
- **Menuiserie** = Vrai goulot opérationnel (240h/240h utilisées, investissement prioritaire)
- **Demande chaises** = Goulot commercial (action marketing/prix)
- **Assemblage + Bois** = Capacités excédentaires (optimisation possible)

#### � **Insight #3 : Data-Driven Decision Making**
L'optimisation révèle que l'intuition "chaises plus rentables → produire max chaises" est **fausse** quand on intègre toutes les contraintes réelles.

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
- **Résultats concrets** : €, heures, unités (pas d'abstractions)

### ✅ **Concepts Clés Illustrés**
- **🎯 Optimisation** : Trouver le maximum sous contraintes
- **⚖️ Trade-offs** : Arbitrage entre différents choix
- **🚨 Goulots** : Identification des contraintes limitantes
- **📊 Analyse marginale** : Impact de chaque contrainte

### ✅ **Data-Driven Approach**
- **Input** : Données CSV structurées (coûts, capacités, demandes)
- **Processing** : Algorithme d'optimisation mathématique
- **Output** : Décisions quantifiées et justifiées
- **Insights** : Analyse des goulots pour action managériale

### ✅ **Extensible & Réaliste**
- **Variables multiples** : Plusieurs produits/ressources
- **Contraintes variées** : Capacités, demandes, réglementations
- **Solution robuste** : Gère les conflits entre objectifs
- **Validation** : Résultats vérifiables et expliqués

> **🎯 Message clé** : Cet exemple démontre qu'avec des **données structurées** et des **algorithmes d'optimisation**, on peut prendre des **décisions business optimales** même dans des situations complexes avec multiples contraintes conflictuelles.

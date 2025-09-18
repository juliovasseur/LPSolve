# 📚 Exemple Éducatif d'**Optimisation Linéaire** : Production de Meubles

## 🎯 **Description du Problème - Accessible à Tous**

Ce cas pratique illustre un **problème d'optimisation linéaire classique** de production industrielle, parfait pour comprendre les concepts fondamentaux de l'**optimisation sous contraintes**.

> **🎓 Qu'est-ce que l'optimisation linéaire ?** C'est une méthode mathématique pour trouver la **meilleure solution** (ex: maximum de profit) quand on a des **limites à respecter** (ex: budget, temps, ressources).

### 🏭 **Contexte Business Simple**

Une entreprise de meubles doit décider combien produire de chaque produit pour **maximiser son profit** :
- **🪑 Chaises** : 30€ de profit par unité (variable `x_chairs`)
- **🪑 Tables** : 50€ de profit par unité (variable `x_tables`)

### 🎯 **Fonction Objectif** (Ce qu'on veut optimiser)
**Maximiser le profit total :**
```mathematica
Profit = 30€ × nombre_chaises + 50€ × nombre_tables
```

> **💡 En termes simples** : On cherche le nombre optimal de chaises et tables à produire pour gagner le maximum d'argent possible.

### ⚖️ **Contraintes** (Limites à respecter)

> **🎓 Contraintes ?** Ce sont les **limites imposées** par la réalité : budget, temps, matériaux, demande du marché, etc.

#### 🏭 **Ressources Limitées de Production**

1. **🔨 Atelier Menuiserie** (200h disponibles/semaine) :
   ```
   2h/chaise + 4h/table ≤ 200h maximum
   ```
   > *Chaque chaise prend 2h, chaque table 4h de menuiserie*

2. **🔧 Atelier Assemblage** (120h disponibles/semaine) :
   ```
   1h/chaise + 2h/table ≤ 120h maximum  
   ```
   > *Chaque chaise prend 1h, chaque table 2h d'assemblage*

3. **🌳 Matériau Bois** (180m² disponibles/semaine) :
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

## 🎯 **Solution Optimale - Résultat Data-Driven**

### 💰 **Décision Optimale du Solveur :**
- **🪑 Chaises = 25 unités** (limite marché atteinte)
- **🪑 Tables = 37.5 unités** (production optimisée)  
- **💰 Profit maximum = 2,625€/semaine**

### 🔍 **Vérification des Calculs** (Transparence totale)
- **💰 Profit**: 30€×25 + 50€×37.5 = 750€ + 1,875€ = **2,625€** ✅
- **🔨 Menuiserie**: 2h×25 + 4h×37.5 = 50h + 150h = **200h/200h** ✅ **[SATURÉE]**
- **🔧 Assemblage**: 1h×25 + 2h×37.5 = 25h + 75h = **100h/120h** ✅ (20h libres)
- **🌳 Bois**: 1m²×25 + 3m²×37.5 = 25m² + 112.5m² = **137.5m²/180m²** ✅ (42.5m² libres)
- **📊 Demande chaises**: 25 ≤ 25 ✅ **[CONTRAINTE ACTIVE]**

### 🚨 **Analyse des Goulots d'Étranglement**

#### 🔴 **Contraintes Saturées (Goulots critiques)**
1. **🔨 Menuiserie** : 100% utilisée (200h/200h)
   - **Impact** : Principal **goulot limitant** la production
   - **Décision** : Investir en priorité dans cet atelier pour croître

2. **📊 Demande chaises** : Limite marché atteinte (25/25)
   - **Impact** : Force la production vers les tables moins rentables/h
   - **Décision** : Développer le marché chaises ou focus qualité/prix
- **Min chaises**: 25 ≥ 10 ✓
- **Min tables**: 37.5 ≥ 5 ✓
- **Max chaises**: 25 ≤ 25 ✓ (saturée)

#### 🟢 **Ressources Sous-Utilisées (Capacité libre)**
- **🔧 Assemblage** : 20h libres/semaine (capacité excédentaire)
- **🌳 Bois** : 42.5m² libres/semaine (approvisionnement suffisant)

### 💡 **Leçons Business Importantes**

#### 🎯 **Insight #1 : Les Contraintes de Marché Changent Tout**
- **Sans limite chaises** : Théoriquement optimal = 90 chaises + 5 tables = 2,950€
- **Avec limite marché** : Réalité business = 25 chaises + 37.5 tables = 2,625€  
- **Impact** : -325€ (-11%) de **manque à gagner** dû aux limites marché

#### 🏭 **Insight #2 : Identifier les Vrais Goulots**
- **Menuiserie** = Vrai goulot opérationnel (investissement prioritaire)
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

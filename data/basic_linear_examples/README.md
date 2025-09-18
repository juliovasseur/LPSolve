# 📚 Educational **Linear Optimization** Example: Furniture Production

## 🎯 **Problem Description ### 💡 **Important Business Lessons**

#### 🎯 **Insight #1: Market Constraints Change Everything**
- **Without chair limits**: Theoretically optimal = 90 chairs + 5 tables = 2,950€
- **With market limits**: Business reality = 25 chairs + 37.5 tables = 2,625€  
- **Impact**: -325€ (-11%) **opportunity cost** due to market limits

#### 🏭 **Insight #2: Identify Real Bottlenecks**
- **Carpentry** = Real operational bottleneck (priority investment)
- **Chair demand** = Commercial bottleneck (marketing/pricing action)
- **Assembly + Wood** = Excess capacities (optimization possible)

#### 📊 **Insight #3: Data-Driven Decision Making**
Optimization reveals that the intuition "chairs more profitable → produce max chairs" is **false** when integrating all real constraints.

---

## 🚀 **Execution**

```bash
make run-basic
```

---

## 🎓 **Why is This Example Perfect for Learning?**

### ✅ **Accessible to Everyone**
- **Familiar context**: Furniture production (everyone understands)
- **Simple calculations**: Manual verification possible
- **Concrete results**: €, hours, units (no abstractions)

### ✅ **Key Concepts Illustrated**
- **🎯 Optimization**: Finding maximum under constraints
- **⚖️ Trade-offs**: Arbitrage between different choices
- **🚨 Bottlenecks**: Identification of limiting constraints
- **📊 Marginal analysis**: Impact of each constraint

### ✅ **Data-Driven Approach**
- **Input**: Structured CSV data (costs, capacities, demands)
- **Processing**: Mathematical optimization algorithm
- **Output**: Quantified and justified decisions
- **Insights**: Bottleneck analysis for managerial action

### ✅ **Extensible & Realistic**
- **Multiple variables**: Several products/resources
- **Various constraints**: Capacities, demands, regulations
- **Robust solution**: Handles conflicts between objectives
- **Validation**: Verifiable and explained results

> **🎯 Key message**: This example demonstrates that with **structured data** and **optimization algorithms**, we can make **optimal business decisions** even in complex situations with multiple conflicting constraints.o Everyone**

This practical case illustrates a **classic linear optimization problem** for industrial production, perfect for understanding fundamental concepts of **constrained optimization**.

> **🎓 What is linear optimization?** It's a mathematical method to find the **best solution** (e.g., maximum profit) when you have **limits to respect** (e.g., budget, time, resources).

### 🏭 **Simple Business Context**

A furniture company must decide how much to produce of each product to **maximize its profit**:
- **🪑 Chairs**: 30€ profit per unit (variable `x_chairs`)
- **🪑 Tables**: 50€ profit per unit (variable `x_tables`)

### 🎯 **Objective Function** (What we want to optimize)
**Maximize total profit:**
```mathematica
Profit = 30€ × number_chairs + 50€ × number_tables
```

> **💡 In simple terms**: We're looking for the optimal number of chairs and tables to produce to earn the maximum possible money.

### ⚖️ **Constraints** (Limits to respect)

> **🎓 Constraints?** These are **limits imposed** by reality: budget, time, materials, market demand, etc.

#### 🏭 **Limited Production Resources**

1. **🔨 Carpentry Workshop** (200h available/week):
   ```
   2h/chair + 4h/table ≤ 200h maximum
   ```
   > *Each chair takes 2h, each table 4h of carpentry*

2. **🔧 Assembly Workshop** (120h available/week):
   ```
   1h/chair + 2h/table ≤ 120h maximum  
   ```
   > *Each chair takes 1h, each table 2h of assembly*

3. **🌳 Wood Material** (180m² available/week):
   ```
   1m²/chair × x_chairs + 3m²/table × x_tables ≤ 180m²
   ```

4. **Minimum chair demand** (at least 10):
   ```
   x_chairs ≥ 10
   ```

5. **Minimum table demand** (at least 5):
   ```
   x_tables ≥ 5
   ```

6. **Maximum chair demand** (market limit at 25):
   ```
   x_chairs ≤ 25
   ```
   > **Economic rationale**: Even though chairs are more profitable per carpentry unit, 
   > market demand is limited to 25 units. Beyond that, chairs would not be sold.

7. **Variable bounds**:
   ```
   0 ≤ x_chairs ≤ 100
   0 ≤ x_tables ≤ 50
   ```

## 🎯 **Optimal Solution - Data-Driven Result**

### 💰 **Solver's Optimal Decision:**
- **🪑 Chairs = 25 units** (market limit reached)
- **🪑 Tables = 37.5 units** (optimized production)  
- **💰 Maximum profit = 2,625€/week**

### 🔍 **Calculation Verification** (Total transparency)
- **💰 Profit**: 30€×25 + 50€×37.5 = 750€ + 1,875€ = **2,625€** ✅
- **🔨 Carpentry**: 2h×25 + 4h×37.5 = 50h + 150h = **200h/200h** ✅ **[SATURATED]**
- **🔧 Assembly**: 1h×25 + 2h×37.5 = 25h + 75h = **100h/120h** ✅ (20h free)
- **🌳 Wood**: 1m²×25 + 3m²×37.5 = 25m² + 112.5m² = **137.5m²/180m²** ✅ (42.5m² free)
- **📊 Chair demand**: 25 ≤ 25 ✅ **[ACTIVE CONSTRAINT]**

### 🚨 **Bottleneck Analysis**

#### 🔴 **Saturated Constraints (Critical bottlenecks)**
1. **🔨 Carpentry**: 100% utilized (200h/200h)
   - **Impact**: Main **limiting bottleneck** for production
   - **Decision**: Invest priority in this workshop to grow

2. **📊 Chair demand**: Market limit reached (25/25)
   - **Impact**: Forces production towards less profitable tables/h
   - **Decision**: Develop chair market or focus quality/price
- **Min chairs**: 25 ≥ 10 ✓
- **Min tables**: 37.5 ≥ 5 ✓
- **Max chairs**: 25 ≤ 25 ✓ (saturated)

#### 🟢 **Under-utilized Resources (Free capacity)**
- **🔧 Assembly**: 20h free/week (excess capacity)
- **🌳 Wood**: 42.5m² free/week (sufficient supply)

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

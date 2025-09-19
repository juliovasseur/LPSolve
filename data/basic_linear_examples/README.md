# 📚 Educational **Linear Optimization** Example: Furniture Production

## 🎯 **Problem Description - Accessible to Everyone**

This practical case illustrates a **classic linear optimization problem** for industrial production, perfect for understanding fundamental concepts of **constrained optimization**.

> **🎓 What is linear optimization?** It's a mathematical method to find the **best solution** (e.g., maximum profit) when you have **limits to respect** (e.g., budget, time, resources).

### 🏭 **Simple Business Context**

A furniture company must decide how much to produce of each product to **maximize profit**:
- **🪑 Chairs**: 45€ profit per unit (variable `x_chairs`)
- **🪑 Tables**: 50€ profit per unit (variable `x_tables`)

### 🎯 **Objective Function** (What we want to optimize)
**Maximize total profit:**
```mathematica
Profit = 45€ × number_chairs + 50€ × number_tables
```

> **💡 In simple terms**: We're looking for the optimal number of chairs and tables to produce to earn the maximum possible money.

### ⚖️ **Constraints** (Limits to respect)

> **🎓 Constraints?** These are the **limits imposed** by reality: budget, time, materials, market demand, etc.

#### 🏭 **Limited Production Resources**

1. **🔨 Carpentry Workshop** (240h available/week):
   ```
   3h/chair + 5h/table ≤ 240h maximum
   ```
   > *Each chair takes 3h, each table 5h of carpentry work*

2. **🔧 Assembly Workshop** (120h available/week):
   ```
   1h/chair + 2h/table ≤ 120h maximum
   ```
   > *Each chair takes 1h, each table 2h of assembly*

3. **🌳 Wood Material** (200m² available/week):
   ```
   2m²/chair + 4m²/table ≤ 200m² maximum
   ```
   > *Each chair needs 2m², each table 4m² of wood*

4. **📊 Chair Market Limit** (max 50 units/week):
   ```
   x_chairs ≤ 50
   ```
   > *Market demand limited to 50 chairs per week*

5. **Variable bounds** (integer production only):
   ```
   0 ≤ x_chairs ≤ 100 (integers)
   0 ≤ x_tables ≤ 100 (integers)
   ```
   > **Important note**: We use Integer Linear Programming for realistic production units!

## 🎯 **Optimal Solution - Data-Driven Result**

### 💰 **Optimal Production Decision:**
- **🪑 Chairs = 50 units** (maximum market demand)
- **🪑 Tables = 18 units** (remaining capacity)  
- **💰 Maximum profit = 3,150€/week**

### 🔍 **Calculation Verification** (Complete transparency)
- **💰 Profit**: 45€×50 + 50€×18 = 2,250€ + 900€ = **3,150€** ✅
- **🔨 Carpentry**: 3h×50 + 5h×18 = 150h + 90h = **240h/240h** ✅ **[BINDING]**
- **🔧 Assembly**: 1h×50 + 2h×18 = 50h + 36h = **86h/120h** ✅ (34h free)
- **🌳 Wood**: 2m²×50 + 4m²×18 = 100m² + 72m² = **172m²/200m²** ✅ (28m² free)
- **📊 Chair Limit**: 50 ≤ 50 ✅ **[BINDING]**

**This is an Integer Linear Programming (ILP) problem** - we can only produce whole furniture units.

### 💡 **Important Business Lessons**

#### 🎯 **Insight #1: Prioritize High-Margin Products**
- **Chairs more profitable per hour**: 45€ / 3h = **15€/h carpentry**
- **Tables less profitable per hour**: 50€ / 5h = **10€/h carpentry**
- **Strategy**: Produce maximum chairs first, then fill remaining capacity with tables

#### 🎯 **Insight #2: Binding Constraints Show Real Bottlenecks**
- **Carpentry** = BINDING (240h used exactly) → **Critical resource**
- **Chair Market** = BINDING (50 units max reached) → **Sales limitation**
- **Assembly** = slack (34h unused) → **Excess capacity**
- **Wood** = slack (28m² unused) → **Sufficient supply**

💡 To increase profit: **Expand carpentry capacity** or **develop chair market** !

#### 🎯 **Insight #3: Optimal Resource Allocation**
```
Smart production mix:
• x₁ (chairs) = 50 units → 2,250€ (71% of profit)
• x₂ (tables) = 18 units → 900€ (29% of profit)
Total profit = 3,150€ from optimal resource allocation
```

---

## 🚀 **Execution**

```bash
make run-basic
```

---

## 🎓 **Why This Example is Perfect for Learning?**

### ✅ **Accessible to Everyone**
- **Familiar context**: Furniture production (everyone understands)
- **Simple calculations**: Manual verification possible
- **Realistic constraints**: Time, materials, market limits

### ✅ **Key Concepts Illustrated**
- **🎯 Optimization**: Finding maximum profit under constraints
- **⚖️ Trade-offs**: Balancing different products optimally
- **📊 Binding constraints**: Identifying true bottlenecks
- **💡 Economic intuition**: Why optimal ≠ intuitive

### ✅ **Professional Relevance**
- **📈 Production planning**: Real industrial decision-making
- **💼 Resource allocation**: Maximize ROI under limits
- **🎯 Bottleneck analysis**: Focus improvement efforts
- **📊 Data-driven decisions**: Numbers over gut feeling

The optimization reveals the power of **mathematical thinking**: intuition might say "produce equal amounts" but math shows **50+18 beats any balanced mix**!

---

## 📋 **Files Structure**

```
data/basic_linear_examples/
├── README.md                 # This documentation
├── data/
│   ├── objectives.csv        # Profit coefficients (45€, 50€)
│   ├── constraints.csv       # Resource limits & market constraints
│   └── variables.csv         # Production variables (integers)
```

**Mathematical Model**: 2 variables, 4 constraints, integer programming formulation with optimal solution **50 chairs + 18 tables = 3,150€** profit.
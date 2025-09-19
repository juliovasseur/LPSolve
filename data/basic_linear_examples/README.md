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
   4h/chair + 4h/table ≤ 240h maximum
   ```
   > *Each chair takes 4h, each table 4h of carpentry work*

2. **🔧 Assembly Workshop** (240h available/week):
   ```
   2h/chair + 4h/table ≤ 240h maximum  
   ```
   > *Each chair takes 2h, each table 4h of assembly*

3. **🎨 Finishing Workshop** (240h available/week):
   ```
   3h/chair + 4h/table ≤ 240h maximum
   ```
   > *Each chair takes 3h, each table 4h of finishing*

4. **📦 Storage Space** (80 units max/week):
   ```
   1 unit/chair + 1 unit/table ≤ 80 units maximum
   ```

5. **Variable bounds** (integer production only):
   ```
   0 ≤ x_chairs ≤ 100 (integers)
   0 ≤ x_tables ≤ 100 (integers)
   ```
   > **Important note**: We use Integer Linear Programming for realistic production units!

## 🎯 **Optimal Solution - Data-Driven Result**

### 💰 **Optimal Production Decision:**
- **🪑 Chairs = 30 units**
- **🪑 Tables = 30 units**  
- **💰 Maximum profit = 2,850€/week**

### 🔍 **Calculation Verification** (Complete transparency)
- **💰 Profit**: 45€×30 + 50€×30 = 1,350€ + 1,500€ = **2,850€** ✅
- **🔨 Carpentry**: 4h×30 + 4h×30 = 120h + 120h = **240h/240h** ✅ **[SATURATED]**
- **🔧 Assembly**: 2h×30 + 4h×30 = 60h + 120h = **180h/240h** ✅ (60h free)
- **🎨 Finishing**: 3h×30 + 4h×30 = 90h + 120h = **210h/240h** ✅ (30h free)
- **📦 Storage**: 1×30 + 1×30 = 30 + 30 = **60/80 units** ✅ (20 units free)

**This is an Integer Linear Programming (ILP) problem** - we can only produce whole furniture units.

### 💡 **Important Business Lessons**

#### 🎯 **Insight #1: Resource Bottlenecks Define Success**
- **Carpentry** = BINDING (240h used / 240h available) → **Zero slack**
- **Assembly** = slack (180h used / 240h available) → **60h unused** 
- **Finishing** = slack (210h used / 240h available) → **30h unused**
- **Storage** = slack (60 used / 80 available) → **20 units unused**

💡 Want more profit? **Invest in carpentry capacity** (hire carpenters or buy tools)!

#### 🎯 **Insight #2: Decision Variables Show The Way**
```
Optimal production plan:
• x₁ (chairs) = 30 units
• x₂ (tables) = 30 units
Total profit = 30×45 + 30×50 = 1,350 + 1,500 = 2,850€
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
- **Concrete results**: €, hours, units (no abstractions)

### ✅ **Key Concepts Illustrated**
- **🎯 Optimization**: Finding maximum under constraints
- **⚖️ Trade-offs**: Resource allocation decisions
- **🔄 Sensitivity**: Impact of changing constraints
- **📊 Binding constraints**: True bottlenecks identification

### ✅ **Professional Relevance**
- **📈 Production planning**: Real industrial application
- **💼 Resource management**: Budget/time allocation
- **🎯 Decision support**: Data-driven choices
- **🔄 What-if analysis**: Scenario planning

The optimization reveals that the intuition "chairs more profitable → produce max chairs" is **false** when integrating all real constraints.

---

## 📋 **Files Structure**

```
data/basic_linear_examples/
├── README.md                 # This documentation
├── data/
│   ├── objectives.csv        # Profit coefficients (45€, 50€)
│   ├── constraints.csv       # Resource limits (240h carpentry, etc.)
│   └── variables.csv         # Production variables (integers)
```

**Mathematical Model**: 2 variables, 4 resource constraints, integer programming formulation with optimal solution 30+30 = 2,850€ profit.
# 📚 Educational **Linear Optimization** Example: Furniture Production

## 🎯 **Problem Description #### 🎯 **I#### 🎯 **Insight #3: Decision Variables Show The Way**
```
Optimal integer production plan:
• x₁ (chairs) = 30 units
• x₂ (tables) = 30 units
Total profit = 30×45 + 30×50 = 1,350 + 1,500 = 2,850€
```sight #2: Resource Bottlenecks Define Success**
- **Carpentry** = BINDING (240h used / 240h available) → **Zero slack**
- **Assembly** = slack (200h used / 240h available) → **40h unused** 
- **Finishing** = slack (210h used / 240h available) → **30h unused**
- **Storage** = slack (60 used / 80 available) → **20 units unused**

💡 Want more profit? **Invest in carpentry capacity** (hire carpenters or buy tools)!cessible to Everyone**

This practical case illustrates a **classic linear optimization problem** for industrial production, perfect for understanding fundamental concepts of **constrained optimization**.

> **🎓 What is linear optimization?** It's a mathematical method to find the **best solution** (e.g., maximum profit) when you have **limits to respect** (e.g., budget, time, resources).

### 🏭 **Simple Business Context**

A **small furniture workshop** produces **2 products**:
- **🪑 Chairs**: 35€ profit/unit  
- **🪑 Tables**: 60€ profit/unit

### 🛠️ **Production Constraints (Resource Limits)**

```
🔨 CARPENTRY: 3h/chair + 5h/table ≤ 240h/week (limited skilled carpenters)
🔧 ASSEMBLY: 2h/chair + 2h/table ≤ 160h/week (workbench capacity)  
✨ FINISHING: 1h/chair + 4h/table ≤ 180h/week (specialized equipment)
📦 STORAGE: 1 unit/chair + 2 units/table ≤ 120 units (warehouse space)
🛒 CHAIRS MARKET: ≤ 50 chairs/week (market demand limit)
🛒 TABLES MARKET: ≤ 40 tables/week (market demand limit)
```

### ❓ **The Question**
**How many chairs and tables to produce to MAXIMIZE profit** while respecting ALL constraints?

---

## 🎓 **Why is This Example Perfect for Learning?**

### ✅ **Pedagogical Strengths**
1. **Intuitive**: Everyone understands furniture production
2. **Visual**: You can imagine the workshop and bottlenecks  
3. **Realistic**: Real business constraints (time, space, market)
4. **Scalable**: Concepts apply to much larger problems

### 📊 **Mathematical Rigor** 
- **2 variables** (chairs, tables): Easy to visualize  
- **6 constraints**: Shows multiple limiting factors
- **Feasible solutions**: Thousands of combinations possible
- **Single optimum**: Clear best answer exists

---

## 🔢 **Mathematical Formulation**

### **Decision Variables**
```
x₁ = Number of chairs to produce per week
x₂ = Number of tables to produce per week  
```

### **Objective Function** (Profit Maximization)
```
Maximize: Z = 35×x₁ + 60×x₂
```

### **Constraints**
```
3×x₁ + 5×x₂ ≤ 240  (Carpentry hours)
2×x₁ + 2×x₂ ≤ 160  (Assembly hours)  
1×x₁ + 4×x₂ ≤ 180  (Finishing hours)
1×x₁ + 2×x₂ ≤ 120  (Storage space)
x₁ ≤ 50            (Chair market limit)
x₂ ≤ 40            (Table market limit)
x₁, x₂ ≥ 0          (Non-negativity)
```

This practical case illustrates a **classic linear optimization problem** for industrial production, perfect for understanding fundamental concepts of **constrained optimization**.

---

## 📊 **Optimal Solution Analysis**

### 💰 **Financial Result (Integer Solution)**
- **Optimal Solution**: 30 chairs + 30 tables
- **Maximum Profit**: **2,850€/week**
- **Key Constraint**: Carpentry (240 hours exactly used)

### 🔍 **Constraint Analysis**
```
🔨 Carpentry: 3×30 + 5×30 = 90 + 150 = 240h (ACTIVE CONSTRAINT - BINDING)
🔧 Assembly: 2×30 + 2×30 = 60 + 60 = 120h (40h available - SLACK)
✨ Finishing: 1×30 + 4×30 = 30 + 120 = 150h (30h available - SLACK)  
📦 Storage: 1×30 + 2×30 = 30 + 60 = 90 units (30 units available - SLACK)
🛒 Chair limit: 30 ≤ 50 (20 chairs available - SLACK)
🛒 Table limit: 30 ≤ 40 (10 tables available - SLACK)
```

> **🔢 Integer Programming Note**: This is actually an **Integer Linear Programming (ILP)** problem since you cannot produce fractional furniture units. The continuous relaxation would give 25 chairs + 37.5 tables, but the integer solution is 30 chairs + 30 tables.

### 💡 **Important Business Lessons**

#### 🎯 **Insight #1: Integer Constraints Are Reality**
- **Continuous relaxation**: 25 chairs + 37.5 tables = 2,625€ (theoretical)
- **Integer programming**: 30 chairs + 30 tables = 2,850€ (actual production)
- **Impact**: +225€ (+8.6%) **because integer solution found better feasible point**

#### 🏭 **Insight #2: Identify Real Bottlenecks**
- **Carpentry** is the TRUE bottleneck (100% utilized)
- **Assembly, Finishing, Storage** have unused capacity
- **Investment priority**: Hire more carpenters or buy carpentry equipment

#### 💰 **Insight #3: Marginal Value (Shadow Prices)**
- **1 extra carpentry hour** = +0.75€ profit potential
- **1 extra assembly hour** = 0€ (already surplus)
- **Business decision**: Pay up to 0.75€/hour for carpentry overtime

---

## 🚀 **Execution**

```bash
make run-basic
```

### ⚡ **Performance**
- **Variables**: 2 (both continuous)
- **Constraints**: 6 (all linear)
- **Resolution time**: <0.01 seconds
- **Algorithm**: Simplex (CBC/COIN-OR)

---

## 🎯 **Pedagogical Value**

### 📚 **Core Concepts Learned**
1. **Linear Programming Formulation**: Variables, objectives, constraints
2. **Feasible Region**: Understanding solution space boundaries  
3. **Binding Constraints**: Identify real business bottlenecks
4. **Shadow Prices**: Economic value of relaxing constraints
5. **Sensitivity Analysis**: Impact of parameter changes

### 🔄 **Progression to Complex Cases**
This simple example prepares for:
- **Industrial Production**: [Multi-site furniture case](../furniture_production/README.md) (155 variables, 87 constraints)
- **Financial Optimization**: [Portfolio optimization](../portfolio_optimization/README.md) (33 variables, 40+ constraints)

### 💼 **Real-World Applications**
- **Production Planning**: Manufacturing capacity allocation
- **Resource Management**: Staff, equipment, budget optimization  
- **Supply Chain**: Inventory, logistics, distribution
- **Finance**: Portfolio allocation, risk management

---

## 🏆 **Conclusion**

This educational example demonstrates that **linear optimization** is:
- **Powerful**: Finds provably optimal solutions
- **Practical**: Solves real business problems  
- **Scalable**: Same principles apply to enterprise-scale problems
- **Accessible**: Mathematical rigor with business intuition

> **💡 Key Takeaway**: Even simple optimization reveals **non-obvious insights** (like carpentry being the real bottleneck) that intuition alone might miss. That's the power of quantitative decision-making!

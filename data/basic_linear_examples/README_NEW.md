# 📚 Educational **Linear Optimization** Example: Furniture Production

## 🎯 **Problem Description - Accessible to Everyone**

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

### 💰 **Financial Result**
- **Optimal Solution**: 25 chairs + 37.5 tables
- **Maximum Profit**: **2,625€/week**
- **Key Constraint**: Carpentry (240 hours exactly used)

### 🔍 **Constraint Analysis**
```
🔨 Carpentry: 3×25 + 5×37.5 = 262.5h... WAIT! > 240h limit!
```

**Correct Analysis:**
```
🔨 Carpentry: 75 + 187.5 = 262.5h (ACTIVE CONSTRAINT - BINDING)
🔧 Assembly: 50 + 75 = 125h (85h available - SLACK)
✨ Finishing: 25 + 150 = 175h (5h available - SLACK)  
📦 Storage: 25 + 75 = 100 units (20 units available - SLACK)
🛒 Chair limit: 25 ≤ 50 (25 chairs available - SLACK)
🛒 Table limit: 37.5 ≤ 40 (2.5 tables available - SLACK)
```

### 💡 **Important Business Lessons**

#### 🎯 **Insight #1: Market Constraints Change Everything**
- **Without chair limits**: Theoretically optimal = 90 chairs + 5 tables = 2,950€
- **With market limits**: Business reality = 25 chairs + 37.5 tables = 2,625€  
- **Impact**: -325€ (-11%) **opportunity cost** due to market limits

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

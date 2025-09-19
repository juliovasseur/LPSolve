# 🎯 **LPSolve** - *Linear Optimization Engine*
## Industrial-Grade Linear Programming Solver

[![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)](https://python.org)
[![PuLP](https://img.shields.io/badge/PuLP-2.7+-green.svg)](https://pypi.org/project/PuLP/)
[![CBC](https://img.shields.io/badge/CBC-COIN--OR-orange.svg)](https://github.com/coin-or/Cbc)
[![License](https://img.shields.io/badge/License-MIT-red.svg)](LICENSE)

> **From Data to Decisions**: Transform CSV datasets into **actionable optimization solutions** via linear programming. From data parsing to **binding constraints analysis** and **shadow price calculations**.

---

## 🎯 **Project Overview**

This project implements an **industrial-grade linear optimization engine** that transforms CSV data into mathematical models, solved using the CBC (COIN-OR) solver. The system covers three complexity levels, from educational examples to portfolio management applications with **marginal value calculations** and **binding constraints analysis**.

### 🚀 **Universal & Powerful Tool**
Above all, this is a **generalist optimization engine**: you can **clone this repo**, replace the CSV files with your normalized data, and solve **any linear programming problem under constraints**!

### 📊 **Complete Pipeline**
```
CSV Data → Mathematical Modeling → Optimization → Actionable Decisions
```

---

## 🏗️ **Architecture du Système**

### 🎯 **Modular Approach by Complexity Levels**

### 🚀 **Quick Access to Use Cases**

| Level | Use Case | Description | Direct Access |
|-------|----------|-------------|---------------|
| 🟢 **Beginner** | **[Educational Examples](./data/basic_linear_examples/README.md)** | Simple chair/table optimization with market constraints | `make run-basic` |
| 🟡 **Intermediate** | **[Industrial Production](./data/furniture_production/README.md)** | Multi-site planning with supply chain (87 constraints, ESG, transfers) | `make run-furniture` |
| 🔴 **Expert** | **[Quantitative Finance](./data/portfolio_optimization/README.md)** | 16-asset portfolio, regulatory constraints, ALM-type logic | `make run-portfolio` |

> **💡 Tip**: Start with educational examples to understand concepts, then progress to quantitative approaches.

> **🎓 Terminology Note**: The system calculates **shadow prices** and **transaction costs**, but doesn't produce complete PnL or ALM analysis. However, it follows **similar logic** in optimization approach.

### 🏗️ **Structure Technique**

```
LPSolve/
├── 🎛️  lp_solver_engine/           # Main optimization engine
│   ├── src/lpSolver/
│   │   ├── solvers/               # Optimization algorithms
│   │   │   ├── solver_core.py     # Generic LP/MILP solver
│   │   │   └── portfolio_solver.py # Specialized finance solver
│   │   └── utils/                 # Utilities and parsing
│   │       ├── parsing.py         # CSV → mathematical model parsing
│   │       ├── model_arrays.py    # Optimized data structures
│   │       └── modeling.py        # Model construction  
│   ├── main.py                    # Generic entry point
│   ├── portfolio_main.py          # Specialized finance entry point  
│   └── requirements.txt           # Python dependencies
├── 📁 data/                        # Use cases and data
│   ├── 📊 basic_linear_examples/   # Educational cases (level 1)
│   ├── 🏭 furniture_production/    # Industrial optimization (level 2)
│   └── 💰 portfolio_optimization/  # Quantitative finance (level 3)
│       └── data/
│           ├── variables.csv      # 16 assets (AAPL, MSFT, GOOGL...)
│           ├── objectives.csv     # Mean-variance utility function
│           └── constraints.csv    # 40+ regulatory constraints
├── 📈 results/                     # Optimization outputs
└── Makefile                       # Automation and commands
```

---

## 🚀 Usage

### 🎯 **Universal Program Operation**

This program is designed to solve **any type of linear programming problem** using a standardized CSV-based approach. Regardless of your application domain (finance, industrial production, logistics, etc.), the process remains identical:

#### 📋 **Required CSV Structure**

The program expects **3 normalized CSV files** in your use case's `data/` folder:

1. **`variables.csv`** - Defines decision variables
   ```csv
   variable_name,lower_bound,upper_bound,var_type
   x1,0,1,Continuous
   x2,0,100,Integer
   ```

2. **`objectives.csv`** - Defines the objective function to optimize
   ```csv
   variable_name,coefficient
   x1,10.5
   x2,-2.3
   ```

3. **`constraints.csv`** - Defines all problem constraints
   ```csv
   constraint_name,variable_name,coefficient,operator,rhs
   budget_limit,x1,100,<=,50000
   budget_limit,x2,200,<=,50000
   minimum_production,x1,1,>=,10
   ```

#### 🔄 **Execution Process**

1. **Preparation**: Create your use case folder with the 3 CSV files
2. **Configuration**: Program automatically parses your CSVs
3. **Modeling**: Automatic mathematical model construction
4. **Resolution**: Optimization with CBC (COIN-OR) solver
5. **Analysis**: Results generation and detailed metrics

#### ✨ **Advantages of This Approach**

- **🌐 Universality**: Works for any LP/MILP problem
- **📊 Simplicity**: Intuitive CSV interface, no programming required
- **🔧 Flexibility**: Add/modify constraints by editing CSVs
- **📈 Scalability**: Handles thousands of variables and constraints
- **🎯 Reproducibility**: Easy model versioning via Git

### 📊 **Quick Commands**

```bash
# Run the three main use cases
make run-basic      # 🟢 Simple educational case
make run-furniture  # 🟡 Industrial optimization  
make run-portfolio  # 🔴 Quantitative finance

# Create your own use case
make create-case NAME=my_project
make run-custom PROJECT=my_project
```

---

## 🛠️ **Create Your Own Use Case (In 2 Minutes!)**

Want to solve YOUR optimization problem? Nothing easier!

### 🚀 **Quick Method with Template**
```bash
# Create a new use case based on template
make create-case NAME=my_project

# This automatically creates:
# data/my_project/
#   ├── data/
#   │   ├── variables.csv      # Template with 2 example variables
#   │   ├── objectives.csv     # Objective function template
#   │   └── constraints.csv    # Constraints template
#   └── README.md              # Customizable documentation
```

### ✏️ **Customization**
1. **Edit the CSVs** with your specific data
2. **Run optimization**: `make run-custom PROJECT=my_project`

### 📋 **Example CSV Template**

The template automatically generates a simple optimization problem:
- **2 variables**: x1, x2 (continuous, bounded)
- **1 objective**: Maximize 10*x1 + 5*x2
- **2 constraints**: Budget and capacity

Simply replace this data with your own!

---

## 📊 **Understanding Optimization Results**

### 🎯 **Output Terminology**

When you run an optimization, the program displays several important metrics:

#### ✅ **Solution Status**
- **`OK`**: Optimal solution found ✅
- **`INFEASIBLE`**: No solution respecting all constraints ❌
- **`UNBOUNDED`**: Poorly formulated problem (objective tends to infinity) ⚠️

#### 📊 **Variable Values**
- **Optimal value**: Best allocation found for each variable
- **Slack/Surplus**: Available margin on each constraint

#### 🔍 **Constraint Analysis**
- **`ACTIVE`** (binding): **Saturated** constraint - limits optimization 🔴
- **`LB/UB`**: Lower/Upper Bound - bounds reached 📏
- **`SLACK > 0`**: Available margin - non-saturated constraint 🟢

#### 💰 **Shadow Prices (Marginal Values)**
- **Marginal cost**: Possible improvement if we relax a constraint by 1 unit
- **Saturated constraints**: High shadow price = important bottleneck
- **Constraints with slack**: Shadow price = 0 (no immediate improvement)

> **💡 Practical Tip**: Constraints with the **highest shadow prices** are your **optimization priorities** - investing additional resources there will have the greatest impact!

---

## 🔧 Installation & Configuration

### 📋 **Prerequisites**
- **Python 3.9+** 
- **Git** (to clone the repo)

### ⚡ **Quick Installation**
```bash
# Clone the repository
git clone https://github.com/juliovasseur/LPSolve.git
cd LPSolve

# Install Python dependencies
pip install -r lp_solver_engine/requirements.txt

# Test installation
make run-basic
```

### 📦 **Main Dependencies**
- **PuLP 2.7+**: Mathematical modeling interface
- **CBC Solver**: COIN-OR optimization engine (installed automatically)

---

## 🏆 **Performances & Limitations**

### ⚡ **Tested Capabilities**
- **Variables**: Tested up to 1000+ continuous/integer variables
- **Constraints**: Tested up to 500+ linear constraints
- **Resolution time**: <1s for provided use cases
- **Memory**: <100MB even on large problems

### ⚠️ **Technical Limitations**
- **Linear programming only** (no non-linear functions)
- **CSV interface** (no REST/GraphQL API)
- **CBC Solver** (no access to commercial solvers like Gurobi/CPLEX)

### 🎯 **Optimal Use Cases**
- ✅ Portfolio optimization with regulatory constraints
- ✅ Industrial production planning
- ✅ Resource allocation under constraints
- ✅ Transportation and logistics problems
- ❌ Non-linear optimization (neural networks, etc.)
- ❌ Advanced stochastic programming

---

## 📚 **Documentation Avancée**

### 🎓 **Learning Resources**
- **[Educational Examples](./data/basic_linear_examples/README.md)**: Basic concepts with concrete case
- **[Industrial Production](./data/furniture_production/README.md)**: Multi-site optimization with supply chain (155 variables, 87 constraints)
- **[Quantitative Finance](./data/portfolio_optimization/README.md)**: Regulatory constraints and risk metrics

### 🛠️ **For Developers**
- **Source Code**: `lp_solver_engine/src/lpSolver/`
- **Tests**: Validation on the 3 provided use cases
- **Extensions**: Add new solvers in `solvers/`

### 💼 **Business Applications**
Each specialized README contains:
- **Detailed business context**
- **Constraint-by-constraint analysis**
- **Results interpretation** for decision making
- **Sector-specific performance metrics**

---

## 🤝 **Contribution & Support**

### 🐛 **Report a Bug**
- Open a **GitHub issue** with your use case
- Include your **CSV files** and **complete error**

### 📧 **Contact**
- **GitHub**: [@juliovasseur](https://github.com/juliovasseur)
- **Project**: [LPSolve Repository](https://github.com/juliovasseur/LPSolve)

---

## 📜 **Licence & Crédits**

### 📋 **License**
**MIT License** - Free commercial and personal use

### 🏆 **Technologies Used**
- **[PuLP](https://pypi.org/project/PuLP/)**: Python Linear Programming Interface
- **[CBC](https://github.com/coin-or/Cbc)**: COIN-OR Branch & Cut Solver
- **[Python 3.9+](https://python.org)**: Development language

### 🎯 **Academic Inspirations**
- **Markowitz Modern Portfolio Theory** (1952)
- **Dantzig Simplex Algorithm** (1947) 
- **Asset Liability Management** principles

---

*Last updated: September 2025*

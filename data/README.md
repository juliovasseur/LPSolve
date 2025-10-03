# 📂 Data - Use Cases and Examples

This folder contains **3 increasing complexity levels** to demonstrate the capabilities of the quantitative optimization engine.

## 🎯 Use Case Structure

### 📊 **Basic Linear Examples** (Level 1 - Educational)
```
data/basic_linear_examples/
└── data/
    ├── variables.csv    # 2 simple variables (chairs, tables)
    ├── objectives.csv   # Basic profit maximization
    └── constraints.csv  # 6 resource constraints
```

**Objective**: Algorithm validation and basic concept learning
- **Complexity**: 2 variables, 4 constraints
- **Time**: <0.01s
- **Result**: 3,150€ optimal profit

### 🏭 **Furniture Production with Supply Chain** (Level 2 - Industrial)
```
data/furniture_production/
└── data/
    ├── variables.csv    # 155 variables (multi-site production + 24 transfer variables)
    ├── objectives.csv   # Profit maximization with transport costs  
    └── constraints.csv  # 87 constraints (production + supply chain)
```

**Objective**: Advanced industrial production with intelligent supply chain
- **Complexity**: 155 variables, 87 constraints
- **Time**: ~0.12s
- **Result**: 6,985,500€ optimal profit (zero transfers needed!)
- **🔍 Key Insight**: Current geographic configuration already optimal

### 💰 **Portfolio Optimization** (Level 3 - Quantitative Finance)
```
data/portfolio_optimization/
└── data/
    ├── variables.csv    # 33 variables (16 assets + costs + risk)
    ├── objectives.csv   # Sophisticated mean-variance utility
    └── constraints.csv  # 40+ regulatory constraints
```

**Objective**: Professional financial portfolio optimization
- **Complexity**: 33 variables, 40+ constraints
- **Time**: ~0.03s  
- **Result**: 13.64 bp/day expected utility

## 🚀 Execution

```bash
# From project root directory
make run-basic      # Level 1: Educational examples
make run-furniture  # Level 2: Industrial optimization  
make run-portfolio  # Level 3: Quantitative finance
```

## 📈 Complexity Progression

| Level | Use Case | Variables | Constraints | Time | Performance |
|-------|----------|-----------|-------------|------|-------------|
| 1 | Basic Examples | 2 | 4 | <0.01s | 3,150€ |
| 2 | **Furniture Multi-Sites** | **155** | **87** | **<0.05s** | **6,985,500€** |
| 3 | **Portfolio Finance** | **33** | **40** | **<0.02s** | **2.46 bp/day** |

## 🎓 Educational Usage

This progression allows to:
- **Understand** concepts on simple examples
- **Apply** to realistic industrial problems  
- **Master** complex financial optimizations

Each level prepares skills for the next, offering **progressive skill building** towards professional quantitative finance.

## 🔧 Data Format

All cases use the **standardized CSV format**:
- `variables.csv`: Decision variables definition
- `objectives.csv`: Objective function to optimize
- `constraints.csv`: Problem constraints and limits

This uniformity allows to **compare approaches** and **reuse code** between different application domains.

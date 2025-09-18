# 🎛️ LP Solver Engine

## 🏗️ Optimization Engine Architecture

The **LP Solver Engine** is the core of the quantitative optimization system. It transforms CSV data into mathematical optimization models and solves them using state-of-the-art algorithms.

### 📁 Module Structure

```
lp_solver_engine/
├── src/lpSolver/
│   ├── solvers/                    # Optimization algorithms
│   │   ├── solver_core.py          # Generic LP/MILP solver
│   │   └── portfolio_solver.py     # Specialized finance solver
│   ├── utils/                      # Utilities and parsing
│   │   ├── parsing.py              # CSV → mathematical model
│   │   ├── model_arrays.py         # Optimized data structures
│   │   └── modeling.py             # Model construction
│   └── archive/                    # Historical versions
├── main.py                         # Generic entry point
├── portfolio_main.py               # Finance entry point
└── requirements.txt                # Python dependencies
```

## 🔧 Main Components

### **Solvers (`solvers/`)**

#### `solver_core.py` - Generic Solver
- Standardized PuLP interface
- Support LP/MILP/QP
- Advanced result formatting
- Performance metrics

#### `portfolio_solver.py` - Specialized Finance Solver  
- Quantitative portfolio optimization
- Regulatory constraints analysis
- Financial metrics (Herfindahl, effective assets)
- Quantitative finance terminology

### **Utils (`utils/`)**

#### `parsing.py` - CSV Parsing
- Reading variables.csv, objectives.csv, constraints.csv files
- Format validation and consistency checks
- Robust error handling

#### `model_arrays.py` - Data Structures
- Optimized `LPModelData` class
- Efficient matrix representation
- Interface for solvers

#### `modeling.py` - Model Construction
- Data transformation → mathematical models
- Complex constraints support
- Numerical optimizations

### **Archive (`archive/`)**
- `solver_v1_backup.py` - Historical version with reduced costs
- `solver_v2_experimental.py` - Experimental version

## 🚀 Entry Points

### `main.py` - Generic Interface
```python
# Standard usage for all problem types
python main.py data/folder/
```

### `portfolio_main.py` - Specialized Finance Interface
```python  
# Optimized interface for financial problems
python portfolio_main.py portfolio_optimization/data/
```

## 📊 Technical Characteristics

- **Performance** : Optimization <50ms for complex problems
- **Solvers** : CBC (COIN-OR), PuLP interface
- **Robustness** : Infeasible constraints handling
- **Scalability** : Support 100+ variables/constraints  
- **Formats** : Standardized CSV, formatted outputs

## 🔍 Advanced Usage

### Solver Customization
```python
from src.lpSolver.solvers import solve_lp_with_progress

# Resolution with custom parameters
result = solve_lp_with_progress(data, 
                               solver_params={'msg': 1, 'timeLimit': 300})
```

### New Format Extensions
```python  
from src.lpSolver.utils import LPModelData

# Custom model creation
data = LPModelData(variables, objectives, constraints, sense)
```

## 🛠️ Development

### Tests
```bash
# Test all use cases
make run-basic && make run-furniture && make run-portfolio
```

### Debugging
```bash
# Verbose mode
PULP_CBS_MSG=1 make run-portfolio
```

This modular architecture enables maximum extensibility while maintaining optimal performance for professional quantitative applications.

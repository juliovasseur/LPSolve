# Linear Programming Solver — Python-based Optimization Framework

**TL;DR** — A comprehensive framework that transforms CSV files into linear programming (LP/MILP) optimization problems, solved using **PuLP** and **CBC**. 

This project demonstrates three different complexity levels of linear programming applications, showcasing how mathematical optimization can solve real-world problems.

## 🏗️ Project Structure

```
├── lp_solver_engine/           # Core solver implementation
├── basic_linear_examples/      # Simple mathematical examples  
├── furniture_production/       # Medium complexity business case
└── portfolio_optimization/     # Advanced financial optimization
```

## 📊 Three Application Cases

### 1. Basic Linear Examples (`basic_linear_examples/`)
Pure mathematical linear programming examples designed to:
- Verify solver functionality  
- Provide baseline performance benchmarks
- Demonstrate correct mathematical output

### 2. Furniture Production Optimization (`furniture_production/`)
Comprehensive business case featuring:
- Multi-period production planning (chairs, tables, desks)
- Resource constraints (capacity, labor, materials)
- Inventory management and setup costs
- Carbon budget constraints (70+ constraints)
- Complete business optimization scenario

### 3. Portfolio Optimization (`portfolio_optimization/`)
Advanced financial application including:
- Markowitz portfolio optimization
- Risk management (CVaR constraints)
- Exposure limits and regulatory compliance  
- Transaction costs modeling
- Large-scale financial optimization

## 🎯 Project Objectives

Demonstrate the transition from:
- CSV data files → Mathematical optimization model → Optimal solution
- Simple examples → Real business problems → Complex financial applications
- Educational tool → Production-ready optimization framework

## 🚀 Quick Start

### Setup Environment
```bash
cd lp_solver_engine
make install
```

### Run Examples
```bash
# Run basic mathematical examples
make run-basic

# Run furniture production optimization
make run-furniture

# Run portfolio optimization  
make run-portfolio

# Run all examples
make test-all
```

## 📁 Data Format

Each optimization case uses standardized CSV format:
- `variables.csv`: Decision variable definitions
- `objectives.csv`: Objective function coefficients and sense (min/max)
- `constraints.csv`: Linear constraint specifications

## 🛠️ Technical Stack

- **Python 3.8+**: Core language
- **PuLP**: Linear programming modeling
- **CBC**: Open-source solver
- **CSV**: Human-readable data format
- **Make**: Build automation

## 📈 Complexity Progression

1. **Basic Examples**: 2-3 variables, 3-5 constraints
2. **Furniture Production**: 50+ variables, 70+ constraints  
3. **Portfolio Optimization**: 100+ variables, complex constraint matrix

Each level demonstrates increasing model complexity and real-world applicability.

## 🔧 Development

The solver engine (`lp_solver_engine/`) provides:
- Modular architecture for easy extension
- Error handling and validation
- Progress tracking for large problems
- Multiple output formats
- Comprehensive logging

See individual README files in each directory for detailed information.

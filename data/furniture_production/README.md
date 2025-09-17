# Furniture Production Optimization

This directory contains a comprehensive business case study for furniture manufacturing optimization, focusing on chairs and tables production.

## Business Case

A furniture company needs to optimize its production schedule to maximize profit while respecting:
- Resource constraints (wood, labor, machine time)
- Storage limitations
- Demand forecasts
- Production capacity limits

## Content

- **data/**: CSV files containing the furniture production optimization problem
  - `variables.csv`: Production variables (chairs, tables, by week)
  - `objectives.csv`: Profit margins and optimization goals
  - `constraints.csv`: Business constraints and resource limitations

## Key Features

- Multi-period production planning
- Resource allocation optimization
- Inventory management constraints
- Profit maximization objectives

## Usage

From the `lp_solver_engine` directory:
```bash
make run-furniture
```

This represents a medium-complexity real-world optimization problem typical in manufacturing industries.

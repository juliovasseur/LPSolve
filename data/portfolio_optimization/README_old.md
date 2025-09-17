# Portfolio Optimization

This directory contains advanced financial portfolio optimization problems, representing the most complex application of the LP solver.

## Financial Application

Portfolio optimization for investment management involving:
- Asset allocation decisions
- Risk management constraints
- Return maximization objectives
- Regulatory compliance requirements
- Market constraints and liquidity limits

## Content

- **data/**: CSV files containing portfolio optimization problems
  - `variables.csv`: Investment decision variables (asset allocations)
  - `objectives.csv`: Risk-return optimization objectives
  - `constraints.csv`: Financial regulations and risk limits

## Key Features

- Modern Portfolio Theory implementation
- Risk-return tradeoff optimization
- Diversification constraints
- Regulatory compliance modeling
- Large-scale financial optimization

## Usage

From the `lp_solver_engine` directory:
```bash
make run-portfolio
```

This represents the most complex and computationally intensive optimization scenario, designed to test the solver's performance on large-scale financial problems.

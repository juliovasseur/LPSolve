# Linear Programming Solver Engine

This directory contains the core LP solver implementation with parsing, modeling, and solving capabilities.

## Architecture

- **main.py**: Entry point and orchestration
- **src/lpSolver/**: Core solver modules
  - `parsing.py`: CSV data parsing and validation
  - `modeling.py`: LP model construction
  - `model_arrays.py`: Array-based model building
  - `lite.py`: Lightweight solver with progress tracking

## Features

- CSV-based problem definition
- PuLP integration for solving
- Progress tracking and reporting
- Error handling and validation
- Multiple output formats

## Usage Examples

### Run specific optimization case:
```bash
make run-basic        # Basic mathematical examples
make run-furniture    # Furniture production optimization  
make run-portfolio    # Portfolio optimization
```

### Run all test cases:
```bash
make test-all
```

### Setup environment:
```bash
make install
```

### Clean artifacts:
```bash
make clean
```

## Data Format

The solver expects CSV files in the following format:
- `variables.csv`: Variable definitions
- `objectives.csv`: Objective function coefficients
- `constraints.csv`: Linear constraints specification

See the example directories for specific data format examples.

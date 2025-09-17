SHELL := /bin/bash

# === Colors for better output readability ===
RESET := \033[0m
BOLD  := \033[1m
GREEN := \033[32m
BLUE  := \033[34m
YELL  := \033[33m
RED   := \033[31m

# === Configuration ===
PY      ?= python3
VENV    ?= .venv
PYTHON  := $(VENV)/bin/python
PIP     := $(VENV)/bin/pip
OUT     ?= results                # output directory
FORMAT  ?= csv                    # csv | txt

# === Data directories ===
BASIC_EXAMPLES := data/basic_linear_examples/data
FURNITURE_DATA := data/furniture_production/data
PORTFOLIO_DATA := data/portfolio_optimization/data

.PHONY: help install venv run-basic run-furniture run-portfolio clean

help:
	@printf "$(BOLD)🏛️  Linear Programming Solver - Data-Driven Optimization$(RESET)\n"
	@printf "\n$(BOLD)📊 Built-in Examples:$(RESET)\n"
	@printf "  $(GREEN)make install$(RESET)          : Setup virtual environment and install dependencies\n"
	@printf "  $(GREEN)make run-basic$(RESET)        : Run basic linear programming examples\n"
	@printf "  $(GREEN)make run-furniture$(RESET)    : Run furniture production optimization\n"
	@printf "  $(GREEN)make run-portfolio$(RESET)    : Run portfolio optimization (finance)\n"
	@printf "\n$(BOLD)🛠️  Custom Cases (Your Data):$(RESET)\n"
	@printf "  $(BLUE)make create-case NAME=my_project$(RESET) : Create new optimization case with templates\n"
	@printf "  $(BLUE)make run-custom CASE=my_project$(RESET)  : Run your custom optimization case\n"
	@printf "  $(BLUE)make list-cases$(RESET)                  : List all available cases (built-in + custom)\n"
	@printf "\n$(BOLD)🧹 Maintenance:$(RESET)\n"
	@printf "  $(GREEN)make clean$(RESET)            : Clean artifacts and output files\n"

usage: help

# === Environment Setup ===
venv:
	@if [ ! -d "$(VENV)" ]; then \
	  printf "$(YELL)>> Creating virtual environment$(RESET)\n"; \
	  $(PY) -m venv $(VENV) >/dev/null 2>&1 && printf "$(GREEN)✓ Virtual environment ready$(RESET)\n"; \
	fi

install: venv
	@printf "$(YELL)>> Installing dependencies$(RESET)\n"
	@if [ -f lp_solver_engine/requirements.txt ]; then \
	  $(PIP) install -r lp_solver_engine/requirements.txt >/dev/null 2>&1; \
	else \
	  $(PIP) install --upgrade pip >/dev/null 2>&1; \
	  $(PIP) install pulp click >/dev/null 2>&1; \
	fi
	@printf "$(GREEN)✓ Dependencies installed$(RESET)\n"

# === Execution Commands ===
run-basic: install
	@mkdir -p "$(OUT)"
	@printf "$(YELL)>> Running Basic Linear Examples$(RESET)\n"
	@if [ -d "$(BASIC_EXAMPLES)" ]; then \
	  $(PYTHON) lp_solver_engine/main.py "$(BASIC_EXAMPLES)"; \
	else \
	  printf "$(RED)Error: Basic examples data not found at $(BASIC_EXAMPLES)$(RESET)\n"; \
	fi

run-furniture: install
	@mkdir -p "$(OUT)"
	@printf "$(YELL)>> Running Furniture Production Optimization$(RESET)\n"
	@if [ -d "$(FURNITURE_DATA)" ]; then \
	  $(PYTHON) lp_solver_engine/main.py "$(FURNITURE_DATA)"; \
	else \
	  printf "$(RED)Error: Furniture data not found at $(FURNITURE_DATA)$(RESET)\n"; \
	fi

run-portfolio: install
	@mkdir -p "$(OUT)"
	@printf "$(YELL)>> Running Advanced Portfolio Optimization$(RESET)\n"
	@if [ -d "$(PORTFOLIO_DATA)" ]; then \
	  $(PYTHON) lp_solver_engine/portfolio_main.py "$(PORTFOLIO_DATA)"; \
	else \
	  printf "$(RED)Error: Portfolio data not found at $(PORTFOLIO_DATA)$(RESET)\n"; \
	fi

run-portfolio-basic: install
	@mkdir -p "$(OUT)"
	@printf "$(YELL)>> Running Basic Portfolio Optimization$(RESET)\n"
	@if [ -d "$(PORTFOLIO_DATA)" ]; then \
	  $(PYTHON) lp_solver_engine/main.py "$(PORTFOLIO_DATA)"; \
	else \
	  printf "$(RED)Error: Portfolio data not found at $(PORTFOLIO_DATA)$(RESET)\n"; \
	fi

# === Custom Case Management ===
create-case:
	@if [ -z "$(NAME)" ]; then \
	  printf "$(RED)Error: NAME is required. Usage: make create-case NAME=my_project$(RESET)\n"; \
	  exit 1; \
	fi
	@printf "$(YELL)>> Creating new case: $(NAME)$(RESET)\n"
	@mkdir -p "data/$(NAME)/data"
	@printf "name,low,up,type\n# Variables de décision\nx1,0,100,continuous\nx2,0,50,continuous\n" > "data/$(NAME)/data/variables.csv"
	@printf "var,coeff,sense\n# Fonction objectif - A maximiser\nx1,10,max\nx2,15,max\n" > "data/$(NAME)/data/objectives.csv"
	@printf "name,expr,sense,rhs\n# Contraintes du problème\nconstraint1,1*x1 + 2*x2,<=,100\nconstraint2,2*x1 + 1*x2,<=,80\n" > "data/$(NAME)/data/constraints.csv"
	@printf "# $(NAME) - Cas d'Usage Personnalisé\n\n## Description\n\nVotre problème d'optimisation personnalisé.\n\n## Utilisation\n\n\`\`\`bash\nmake run-custom CASE=$(NAME)\n\`\`\`\n\n## Données\n\n- **variables.csv** : Définit vos variables de décision\n- **objectives.csv** : Définit votre fonction objectif\n- **constraints.csv** : Définit vos contraintes métier\n" > "data/$(NAME)/README.md"
	@printf "$(GREEN)✓ Nouveau cas d'usage créé : data/$(NAME)/$(RESET)\n"
	@printf "$(BLUE)  Éditez les fichiers CSV dans data/$(NAME)/data/ puis lancez:$(RESET)\n"
	@printf "$(BLUE)  make run-custom CASE=$(NAME)$(RESET)\n"

run-custom: install
	@if [ -z "$(CASE)" ]; then \
	  printf "$(RED)Error: CASE is required. Usage: make run-custom CASE=my_project$(RESET)\n"; \
	  exit 1; \
	fi
	@mkdir -p "$(OUT)"
	@printf "$(YELL)>> Running Custom Case: $(CASE)$(RESET)\n"
	@if [ -d "data/$(CASE)/data" ]; then \
	  $(PYTHON) lp_solver_engine/main.py "data/$(CASE)/data"; \
	else \
	  printf "$(RED)Error: Custom case data not found at data/$(CASE)/data$(RESET)\n"; \
	  printf "$(BLUE)Create it first with: make create-case NAME=$(CASE)$(RESET)\n"; \
	fi

list-cases:
	@printf "$(BOLD)Available Cases:$(RESET)\n"
	@printf "$(GREEN)Built-in Cases:$(RESET)\n"
	@printf "  - basic_linear_examples  (make run-basic)\n"  
	@printf "  - furniture_production   (make run-furniture)\n"
	@printf "  - portfolio_optimization (make run-portfolio)\n"
	@printf "$(BLUE)Custom Cases:$(RESET)\n"
	@for dir in data/*/; do \
	  case_name=$$(basename "$$dir"); \
	  if [ "$$case_name" != "basic_linear_examples" ] && [ "$$case_name" != "furniture_production" ] && [ "$$case_name" != "portfolio_optimization" ]; then \
	    printf "  - $$case_name  (make run-custom CASE=$$case_name)\n"; \
	  fi; \
	done

# === Legacy compatibility ===
run: run-basic

# === Cleanup ===
clean:
	@printf "$(YELL)>> Cleaning up artifacts$(RESET)\n"
	@rm -rf __pycache__ .pytest_cache "$(OUT)" src/**/__pycache__
	@printf "$(GREEN)✓ Cleanup completed$(RESET)\n"

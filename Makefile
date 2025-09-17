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
	@printf "$(BOLD)Linear Programming Solver - Available Commands:$(RESET)\n"
	@printf "  $(GREEN)make install$(RESET)          : Setup virtual environment and install dependencies\n"
	@printf "  $(GREEN)make run-basic$(RESET)        : Run basic linear programming examples\n"
	@printf "  $(GREEN)make run-furniture$(RESET)    : Run furniture production optimization\n"
	@printf "  $(GREEN)make run-portfolio$(RESET)    : Run portfolio optimization (finance)\n"
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

# === Legacy compatibility ===
run: run-basic


# === Cleanup ===
clean:
	@printf "$(YELL)>> Cleaning up artifacts$(RESET)\n"
	@rm -rf __pycache__ .pytest_cache "$(OUT)" src/**/__pycache__
	@printf "$(GREEN)✓ Cleanup completed$(RESET)\n"

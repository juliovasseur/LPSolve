from __future__ import annotations
import time
from typing import Dict, Any, List, Optional, Tuple
from ..utils.model_arrays import LPModelData
from pulp import (
    LpMinimize,
    LpMaximize,
    LpProblem,
    lpDot,
    LpVariable,
    COIN_CMD,
    LpStatus,
    value,
)

class C:
    reset = "\033[0m"
    bold = "\033[1m"
    red = "\033[31m"
    green = "\033[32m"
    yellow = "\033[33m"
    blue = "\033[34m"
    magenta = "\033[35m"
    cyan = "\033[36m"
    dim = "\033[2m"

def cfmt(text: str, *styles: str) -> str:
    return "".join(styles) + str(text) + C.reset

def solve_portfolio_optimization(data: LPModelData, **kwargs) -> Dict[str, Any]:
    """Portfolio optimization solver with financial terminology"""
    sense = "min" if data.sense.lower().startswith("min") else "max"
    prob_sense = LpMinimize if sense == "min" else LpMaximize
    prob = LpProblem("PortfolioOptimizer", prob_sense)

    # Variables
    lp_vars: List[LpVariable] = []
    for i, name in enumerate(data.var_names):
        vtype = data.vtypes[i] if i < len(data.vtypes) else "continuous"
        low = float(data.low[i]) if i < len(data.low) and data.low[i] is not None else None
        up = float(data.up[i]) if i < len(data.up) and data.up[i] is not None else None

        if vtype.lower() == "binary":
            var = LpVariable(name, lowBound=0, upBound=1, cat="Binary")
        elif vtype.lower() == "integer":
            var = LpVariable(name, lowBound=low, upBound=up, cat="Integer")
        else:
            var = LpVariable(name, lowBound=low, upBound=up, cat="Continuous")
        lp_vars.append(var)

    # Objectif
    prob += lpDot(data.c, lp_vars), "ExpectedUtility"

    # Contraintes
    for j, row in enumerate(data.A):
        lhs = lpDot(row, lp_vars)
        rhs = float(data.b[j])
        op = data.senses[j].strip()
        name = data.constr_names[j] if j < len(data.constr_names) and data.constr_names[j] else f"constraint_{j}"
        
        if op == "<=":
            prob += (lhs <= rhs), name
        elif op == ">=":
            prob += (lhs >= rhs), name
        else:
            prob += (lhs == rhs), name

    # Résolution
    start_time = time.time()
    solver = COIN_CMD(msg=0)
    prob.solve(solver)
    solve_time = time.time() - start_time

    # Résultats
    status_key = LpStatus[prob.status]
    objective_value = value(prob.objective) if prob.objective else None
    
    var_values = {}
    for v in lp_vars:
        var_values[v.name] = v.value()

    # Formatage financier spécialisé
    lines = []
    
    # Status de l'optimisation
    if status_key == "Optimal":
        lines.append(cfmt("✅ SOLUTION OPTIMALE TROUVÉE", C.bold, C.green))
    elif status_key == "Infeasible":
        lines.append(cfmt("❌ PORTEFEUILLE INFAISABLE", C.bold, C.red))
    elif status_key == "Unbounded":
        lines.append(cfmt("⚠️  PROBLÈME NON BORNÉ", C.bold, C.yellow))
    else:
        lines.append(cfmt(f"⚠️  STATUS: {status_key}", C.bold, C.yellow))
    
    # Métriques de performance
    lines.append(f"🔧 Modélisation: {cfmt('PuLP (Mean-Variance Optimization)', C.blue)}")
    lines.append(f"⚙️  Solveur: {cfmt('CBC (Quadratic Programming)', C.blue)}")
    lines.append(f"⏱️  Temps d'optimisation: {cfmt(f'{solve_time:.3f}s', C.blue)}")
    
    if objective_value is not None:
        utility_label = "Utilité espérée" if sense == "max" else "Fonction de coût"
        lines.append(f"📈 {utility_label}: {cfmt(f'{objective_value:.4f} bp/jour', C.bold, C.magenta)}")
    
    lines.append("")
    
    # Allocation du portefeuille
    portfolio_weights = [(v, v.value()) for v in lp_vars if v.name.startswith('w_') and v.value() is not None and v.value() > 1e-6]
    transaction_costs = [(v, v.value()) for v in lp_vars if v.name.startswith('tc_') and v.value() is not None and v.value() > 1e-6]
    
    if portfolio_weights:
        lines.append(cfmt("💼 ALLOCATION OPTIMALE DU PORTEFEUILLE:", C.bold, C.blue))
        total_weight = sum(weight for _, weight in portfolio_weights)
        
        # Grouper par secteurs
        tech_weights = [(ticker, weight) for ticker, weight in portfolio_weights if ticker.name.replace('w_', '') in ['AAPL', 'MSFT', 'GOOGL', 'AMZN', 'TSLA', 'NVDA', 'META', 'NFLX']]
        finance_weights = [(ticker, weight) for ticker, weight in portfolio_weights if ticker.name.replace('w_', '') in ['JPM', 'BAC', 'GS', 'MS']]
        health_weights = [(ticker, weight) for ticker, weight in portfolio_weights if ticker.name.replace('w_', '') in ['JNJ', 'PFE', 'UNH']]
        consumer_weights = [(ticker, weight) for ticker, weight in portfolio_weights if ticker.name.replace('w_', '') in ['PG']]
        
        # Affichage par secteur
        if tech_weights:
            lines.append(f"  📱 {cfmt('Technology & Communication Services:', C.cyan)}")
            for ticker, weight in sorted(tech_weights, key=lambda x: x[1], reverse=True):
                ticker_name = ticker.name.replace('w_', '')
                weight_pct = weight * 100
                lines.append(f"    • {cfmt(ticker_name, C.bold)}: {cfmt(f'{weight_pct:.2f}%', C.green)} (${cfmt(f'{weight*1000000:.0f}', C.dim)})")
        
        if finance_weights:
            lines.append(f"  🏦 {cfmt('Financials:', C.cyan)}")
            for ticker, weight in sorted(finance_weights, key=lambda x: x[1], reverse=True):
                ticker_name = ticker.name.replace('w_', '')
                weight_pct = weight * 100
                lines.append(f"    • {cfmt(ticker_name, C.bold)}: {cfmt(f'{weight_pct:.2f}%', C.green)} (${cfmt(f'{weight*1000000:.0f}', C.dim)})")
        
        if health_weights:
            lines.append(f"  🏥 {cfmt('Healthcare:', C.cyan)}")
            for ticker, weight in sorted(health_weights, key=lambda x: x[1], reverse=True):
                ticker_name = ticker.name.replace('w_', '')
                weight_pct = weight * 100
                lines.append(f"    • {cfmt(ticker_name, C.bold)}: {cfmt(f'{weight_pct:.2f}%', C.green)} (${cfmt(f'{weight*1000000:.0f}', C.dim)})")
        
        if consumer_weights:
            lines.append(f"  🧴 {cfmt('Consumer Defensive:', C.cyan)}")
            for ticker, weight in consumer_weights:
                ticker_name = ticker.name.replace('w_', '')
                weight_pct = weight * 100
                lines.append(f"    • {cfmt(ticker_name, C.bold)}: {cfmt(f'{weight_pct:.2f}%', C.green)} (${cfmt(f'{weight*1000000:.0f}', C.dim)})")
    
    # Coûts de transaction
    if transaction_costs:
        lines.append("")
        lines.append(cfmt("💸 COÛTS DE TRANSACTION:", C.bold, C.magenta))
        total_tc = sum(cost for _, cost in transaction_costs)
        lines.append(f"  📊 Total: {cfmt(f'{total_tc:.2f} bp', C.red)} ({cfmt(f'${total_tc*100:.0f}', C.dim)} sur $1M)")
        
        for ticker, cost in sorted(transaction_costs, key=lambda x: x[1], reverse=True)[:5]:
            ticker_name = ticker.name.replace('tc_', '')
            lines.append(f"    • {ticker_name}: {cfmt(f'{cost:.2f} bp', C.yellow)}")
    
    # Analyse des contraintes - GOULOTS D'ÉTRANGLEMENT
    lines.append("")
    lines.append(cfmt("🚨 ANALYSE DES CONTRAINTES RÉGLEMENTAIRES:", C.bold, C.blue))
    
    binding_constraints = []
    slack_constraints = []
    
    for j, row in enumerate(data.A):
        constraint_name = data.constr_names[j] if j < len(data.constr_names) else f"c{j}"
        
        # Calculer la valeur LHS
        lhs_value = sum(row[i] * (lp_vars[i].value() or 0) for i in range(len(row)))
        rhs_value = data.b[j]
        sense_op = data.senses[j].strip()
        
        # Calculer le slack
        if sense_op == "<=":
            slack_value = rhs_value - lhs_value
        elif sense_op == ">=":
            slack_value = lhs_value - rhs_value
        else:  # "=="
            slack_value = abs(lhs_value - rhs_value)
        
        # Classification des contraintes
        if abs(slack_value) < 1e-6:
            binding_constraints.append((constraint_name, sense_op, slack_value, lhs_value, rhs_value))
        else:
            slack_constraints.append((constraint_name, sense_op, slack_value, lhs_value, rhs_value))
    
    # Contraintes saturées (goulots d'étranglement)
    if binding_constraints:
        lines.append(f"  🔴 {cfmt('CONTRAINTES SATURÉES (Goulots)', C.red, C.bold)}:")
        for name, sense_op, slack, lhs, rhs in binding_constraints[:8]:  # Top 8
            constraint_type = classify_constraint(name)
            if constraint_type:
                lines.append(f"    • {cfmt(name, C.bold)} ({constraint_type}): {cfmt('SATURÉE', C.red)} - {cfmt('VALEUR MARGINALE ÉLEVÉE', C.yellow)}")
    
    # Contraintes avec marge
    if slack_constraints:
        lines.append(f"  🟢 {cfmt('CONTRAINTES AVEC MARGE:', C.green)}:")
        # Trier par slack croissant pour montrer les plus proches de la saturation
        slack_constraints.sort(key=lambda x: x[2])
        for name, sense_op, slack, lhs, rhs in slack_constraints[:5]:
            constraint_type = classify_constraint(name)
            if constraint_type:
                if slack < 0.05:  # Proche de la saturation
                    lines.append(f"    • {cfmt(name, C.bold)} ({constraint_type}): marge={cfmt(f'{slack:.4f}', C.yellow)} - {cfmt('RISQUE DE SATURATION', C.yellow)}")
                else:
                    lines.append(f"    • {cfmt(name)} ({constraint_type}): marge={cfmt(f'{slack:.4f}', C.green)}")

    # Métriques de risque
    lines.append("")
    lines.append(cfmt("📊 MÉTRIQUES DE RISQUE & PERFORMANCE:", C.bold, C.cyan))
    
    # Calcul de métriques synthétiques
    if portfolio_weights:
        # Concentration Risk (HHI)
        hhi = sum(weight**2 for _, weight in portfolio_weights)
        lines.append(f"  📈 Indice Herfindahl (concentration): {cfmt(f'{hhi:.4f}', C.magenta)} {risk_level(hhi, 'concentration')}")
        
        # Diversification effective
        eff_stocks = 1/hhi if hhi > 0 else 0
        lines.append(f"  🎯 Nombre effectif d'actifs: {cfmt(f'{eff_stocks:.1f}', C.blue)}")
        
        # Exposition sectorielle
        tech_exp = sum(weight for ticker, weight in portfolio_weights if ticker.name.replace('w_', '') in ['AAPL', 'MSFT', 'GOOGL', 'AMZN', 'TSLA', 'NVDA', 'META', 'NFLX'])
        finance_exp = sum(weight for ticker, weight in portfolio_weights if ticker.name.replace('w_', '') in ['JPM', 'BAC', 'GS', 'MS'])
        
        lines.append(f"  💻 Exposition Technology: {cfmt(f'{tech_exp*100:.1f}%', C.cyan)} {exposure_level(tech_exp)}")
        lines.append(f"  🏦 Exposition Financials: {cfmt(f'{finance_exp*100:.1f}%', C.cyan)} {exposure_level(finance_exp)}")

    details = "\n".join(lines)

    return {
        "status": status_key,
        "objective": objective_value,
        "var_values": var_values,
        "details": details,
        "constraints": [],
        "reduced_costs": {},
        "solver": "CBC-Portfolio",
    }

def classify_constraint(name: str) -> str:
    """Classifier les contraintes selon leur type financier"""
    if "concentration" in name:
        return "Limite sectorielle"
    elif "fully_invested" in name:
        return "Contrainte budgétaire"
    elif "limit" in name and "single" in name:
        return "Limite réglementaire"
    elif "beta" in name:
        return "Gestion du risque"
    elif "esg" in name:
        return "Critère ESG"
    elif "factor" in name:
        return "Exposition factorielle"
    elif "tc_" in name:
        return "Coût de transaction"
    elif "tracking" in name:
        return "Contrainte de tracking"
    else:
        return "Autre contrainte"

def risk_level(value: float, metric_type: str) -> str:
    """Évaluer le niveau de risque"""
    if metric_type == "concentration":
        if value > 0.15:
            return cfmt("(CONCENTRATION ÉLEVÉE)", C.red)
        elif value > 0.08:
            return cfmt("(Concentration modérée)", C.yellow)
        else:
            return cfmt("(Bien diversifié)", C.green)
    return ""

def exposure_level(exposure: float) -> str:
    """Évaluer le niveau d'exposition"""
    if exposure > 0.6:
        return cfmt("(SURPONDÉRATION)", C.red)
    elif exposure > 0.4:
        return cfmt("(Pondération élevée)", C.yellow)
    else:
        return cfmt("(Pondération normale)", C.green)

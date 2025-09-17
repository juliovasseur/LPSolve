from __future__ import annotations
import time
from typing import Dict, Any, List, Optional, Tuple
from .model_ar        )
    
    # Informations sur les contraintes (slacks calculés manuellement)LPModelData
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

def cfmt(text: str, *styles: str) -> str:
    return "".join(styles) + str(text) + C.reset

def solve_lp_with_progress(data: LPModelData, **kwargs) -> Dict[str, Any]:
    sense = "min" if data.sense.lower().startswith("min") else "max"
    prob_sense = LpMinimize if sense == "min" else LpMaximize
    prob = LpProblem("LPModel", prob_sense)

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
    prob += lpDot(data.c, lp_vars), "Objective"

    # Contraintes
    for j, row in enumerate(data.A):
        lhs = lpDot(row, lp_vars)
        rhs = float(data.b[j])
        op = data.senses[j].strip()
        name = data.constr_names[j] if j < len(data.constr_names) and data.constr_names[j] else f"c{j}"
        
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

    # Formatage détaillé
    lines = []
    
    # Status de la résolution
    if status_key == "Optimal":
        lines.append(cfmt("✅ SOLUTION OPTIMALE", C.bold, C.green))
    elif status_key == "Infeasible":
        lines.append(cfmt("❌ PROBLÈME INFAISABLE", C.bold, C.red))
    elif status_key == "Unbounded":
        lines.append(cfmt("⚠️  PROBLÈME NON BORNÉ", C.bold, C.yellow))
    else:
        lines.append(cfmt(f"⚠️  STATUS: {status_key}", C.bold, C.yellow))
    
    # Informations sur la résolution
    lines.append(f"⏱️  Temps de résolution: {cfmt(f'{solve_time:.3f}s', C.blue)}")
    lines.append(f"🔧 Solveur: {cfmt('CBC (COIN-OR)', C.blue)}")
    
    if objective_value is not None:
        sensestr = "Profit" if sense == "max" else "Coût"
        lines.append(f"💰 {sensestr}: {cfmt(f'{objective_value:.2f}€', C.bold, C.magenta)}")
    
    lines.append("")
    lines.append(cfmt("📊 Variables de décision:", C.bold, C.blue))
    
    # Affichage détaillé de toutes les variables avec bornes
    for v in lp_vars:
        lb = v.lowBound if v.lowBound is not None else float("-inf")
        ub = v.upBound if v.upBound is not None else float("inf")
        vv = v.value()
        val_color = C.green if (vv is not None and vv > 1e-6) else C.yellow if (vv is not None and abs(vv) <= 1e-6) else C.red
        val_str = f"{vv:.6g}" if vv is not None else "None"
        
        lines.append(
            f"  • {cfmt(v.name, C.bold)} = {cfmt(val_str, val_color)}  "
            f"{cfmt('[', C.magenta)}lb={lb}, ub={ub}{cfmt(']', C.magenta)}"
        )
    
    # Coûts réduits (pour les problèmes LP - disponibles avec CBC)
    lines.append("")
    lines.append(cfmt("� Coûts réduits:", C.bold, C.magenta))
    for v in lp_vars:
        # Les coûts réduits ne sont pas directement disponibles avec PuLP+CBC de manière simple
        # On affiche un message informatif
        pass
    lines.append(f"  {cfmt('Non disponibles avec CBC via PuLP', C.yellow)}")
    
    # Informations sur les contraintes (slacks calculés manuellement)
    lines.append("")
    lines.append(cfmt("🔗 Contraintes (slacks):", C.bold, C.blue))
    
    # Calculer les slacks manuellement à partir des données originales
    for j, row in enumerate(data.A):
        constraint_name = data.constr_names[j] if j < len(data.constr_names) else f"c{j}"
        
        # Calculer la valeur LHS (Left Hand Side)
        lhs_value = sum(row[i] * (lp_vars[i].value() or 0) for i in range(len(row)))
        rhs_value = data.b[j]
        sense = data.senses[j].strip()
        
        # Calculer le slack selon le type de contrainte
        if sense == "<=":
            slack_value = rhs_value - lhs_value  # Ressource restante
        elif sense == ">=":
            slack_value = lhs_value - rhs_value  # Surplus par rapport au minimum
        else:  # "=="
            slack_value = abs(lhs_value - rhs_value)  # Écart à l'égalité
        
        # Couleur selon l'état
        if abs(slack_value) < 1e-6:
            slack_col = C.red  # Contrainte active/saturée
            status = "ACTIVE"
        elif slack_value > 1e-6:
            slack_col = C.green  # Contrainte non saturée
            status = "OK"
        else:
            slack_col = C.yellow  # Cas particulier
            status = "?"
            
        lines.append(
            f"  • {cfmt(constraint_name, C.bold)} ({sense}): "
            f"slack={cfmt(f'{slack_value:.6g}', slack_col)} "
            f"{cfmt(f'[{status}]', slack_col)}"
        )

    details = "\n".join(lines)

    return {
        "status": status_key,
        "objective": objective_value,
        "var_values": var_values,
        "details": details,
        "constraints": [],
        "reduced_costs": {},
        "solver": "CBC",
    }

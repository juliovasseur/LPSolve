# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    portfolio_main.py                                  :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: Quant Engine                               +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/09/17 Portfolio Optimizer       #+#    #+#              #
#    Updated: 2025/09/17 Financial Analytics       ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from __future__ import annotations
import sys
from typing import List
from src.lpSolver.utils import ParseError, parse_data_dir, build_model_arrays
from src.lpSolver.solvers import solve_portfolio_optimization

class Colors:
    RESET = "\033[0m"
    BOLD = "\033[1m"
    GREEN = "\033[32m"
    BLUE = "\033[34m"
    YELLOW = "\033[33m"
    RED = "\033[31m"
    MAGENTA = "\033[35m"
    CYAN = "\033[36m"

def main(argc: int, argv: List[str]) -> int:
    """
    Optimiseur de portefeuille quantitatif - Point d'entrée principal
    Utilise la programmation linéaire pour l'allocation d'actifs sous contraintes
    """
    if argc < 2:
        print("Usage: python portfolio_main.py <portfolio_data_dir>", file=sys.stderr)
        return 1

    data_dir = argv[1]
    try:
        # Header avec branding financier
        print(f"{Colors.CYAN}{'='*80}{Colors.RESET}")
        print(f"{Colors.BOLD}{Colors.BLUE}    🏛️  OPTIMISEUR DE PORTEFEUILLE QUANTITATIF v2.1{Colors.RESET}")
        print(f"{Colors.BOLD}{Colors.BLUE}    📊  Mean-Variance Optimization avec contraintes réglementaires{Colors.RESET}")
        print(f"{Colors.CYAN}{'='*80}{Colors.RESET}")
        print()
        
        model = parse_data_dir(data_dir)
   
        print(f"{Colors.BOLD}{Colors.BLUE}📋 ANALYSE DU MODÈLE FINANCIER:{Colors.RESET}")
        print(f"  🎯 Actifs sous gestion: {Colors.GREEN}{len([v for v in model['variables'] if v.startswith('w_')])}{Colors.RESET}")
        print(f"  📊 Variables d'optimisation: {Colors.BLUE}{len(model['variables'])}{Colors.RESET}")
        print(f"  ⚖️  Contraintes réglementaires: {Colors.YELLOW}{len(model['constraints'])}{Colors.RESET}")
        
        # Analyse des types de variables
        weight_vars = [v for v in model['variables'] if v.startswith('w_')]
        tc_vars = [v for v in model['variables'] if v.startswith('tc_')]
        risk_vars = [v for v in model['variables'] if 'risk' in v]
        
        print(f"  💼 Poids de portefeuille: {Colors.GREEN}{len(weight_vars)}{Colors.RESET}")
        print(f"  💸 Variables de coût de transaction: {Colors.YELLOW}{len(tc_vars)}{Colors.RESET}")
        print(f"  📈 Variables de risque: {Colors.MAGENTA}{len(risk_vars)}{Colors.RESET}")
        
        # Analyse des contraintes par type
        sector_constraints = [c for c in model['constraints'] if 'concentration' in c['name']]
        regulatory_constraints = [c for c in model['constraints'] if 'limit' in c['name']]
        risk_constraints = [c for c in model['constraints'] if 'beta' in c['name'] or 'tracking' in c['name']]
        
        print(f"  🏭 Contraintes sectorielles: {Colors.CYAN}{len(sector_constraints)}{Colors.RESET}")
        print(f"  📋 Contraintes réglementaires: {Colors.RED}{len(regulatory_constraints)}{Colors.RESET}")
        print(f"  ⚠️  Contraintes de risque: {Colors.MAGENTA}{len(risk_constraints)}{Colors.RESET}")
        
        obj_sense = "Maximisation de l'utilité" if model['objective']['sense'] == "max" else "Minimisation du coût"
        print(f"  🎯 Fonction objectif: {Colors.BOLD}{obj_sense}{Colors.RESET} ({len(model['objective']['coeffs'])} termes)")
        print()
        
        # Construction du modèle matriciel
        print(f"{Colors.YELLOW}⚙️  Construction de la matrice d'optimisation...{Colors.RESET}")
        array = build_model_arrays(model)
        print(f"{Colors.GREEN}✓ Modèle matriciel construit{Colors.RESET}")
        print()

        # Lancement de l'optimisation
        print(f"{Colors.BOLD}{Colors.MAGENTA}🚀 LANCEMENT DE L'OPTIMISATION QUANTITATIVE{Colors.RESET}")
        print(f"{Colors.CYAN}{'─'*60}{Colors.RESET}")
        result = solve_portfolio_optimization(array)
        
        print(result["details"])
        
        if result["status"] != "Optimal":
            print(f"\n{Colors.RED}⚠️  Attention: Solution non-optimale détectée{Colors.RESET}")
            return 2
        
        # Footer
        print(f"\n{Colors.CYAN}{'='*80}{Colors.RESET}")
        print(f"{Colors.BOLD}{Colors.GREEN}✅ OPTIMISATION TERMINÉE AVEC SUCCÈS{Colors.RESET}")
        print(f"{Colors.DIM}Moteur d'optimisation: CBC • Interface: PuLP • Temps: <1s{Colors.RESET}")
        print(f"{Colors.CYAN}{'='*80}{Colors.RESET}")
        
        return 0

    except ParseError as e:
        print(f"{Colors.RED}❌ Erreur de parsing des données financières: {e}{Colors.RESET}", file=sys.stderr)
        return 1
    except Exception as e:
        print(f"{Colors.RED}❌ Erreur critique du moteur d'optimisation: {e}{Colors.RESET}", file=sys.stderr)
        return 1

# Ajout de la classe Colors manquante
Colors.DIM = "\033[2m"

if __name__ == "__main__":
    raise SystemExit(main(len(sys.argv), sys.argv))

# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    main.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: Jvasseur <jvasseur@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/09/08 12:38:17 by Jvasseur          #+#    #+#              #
#    Updated: 2025/09/17 16:31:03 by Jvasseur         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from __future__ import annotations
import sys
from typing import List
from src.lpSolver.utils import ParseError, parse_data_dir, build_model_arrays
from src.lpSolver.solvers import solve_lp_with_progress



def main(argc: int, argv: List[str]) -> int:
    """
    Point d'entrée principal.
    Attendu: chemin d'un dossier contenant data/*.csv
    """
    if argc < 2:
        print("Usage: python lp.py <data_dir>", file=sys.stderr)
        return 1

    data_dir = argv[1]
    try:
        model = parse_data_dir(data_dir)
   
        print("📊 MODÈLE PARSÉ")
        print(f"  • Variables: {len(model['variables'])}")
        print(f"  • Contraintes: {len(model['constraints'])}")
        
        # Analyse des types de variables
        var_types = {}
        for var_name, var_info in model['variables'].items():
            vtype = var_info.get('type', 'continuous')
            var_types[vtype] = var_types.get(vtype, 0) + 1
        
        if len(var_types) > 1:
            types_str = ", ".join([f"{count} {vtype}" for vtype, count in var_types.items()])
            print(f"  • Types: {types_str}")
        
        # Analyse des contraintes
        constr_types = {}
        for constr in model['constraints']:
            sense = constr.get('sense', '<=')
            constr_types[sense] = constr_types.get(sense, 0) + 1
        
        if len(constr_types) > 1:
            constr_str = ", ".join([f"{count} '{sense}'" for sense, count in constr_types.items()])
            print(f"  • Contraintes: {constr_str}")
        
        obj_sense = "maximisation" if model['objective']['sense'] == "max" else "minimisation"
        print(f"  • Objectif: {obj_sense} ({len(model['objective']['coeffs'])} termes)")
        print()
        
        array = build_model_arrays(model)

        # Appel de la résolution LP
       
        print("\n🔍 RÉSOLUTION")
        result = solve_lp_with_progress(array)
        print(result["details"])
        if result["status"] != "Optimal":
            return 2
        



    except ParseError as e:
        print(f"Erreur de parsing: {e}", file=sys.stderr)
        return 1
    except Exception as e:
        print(f"Erreur inattendue: {e}", file=sys.stderr)
        return 1
    

if __name__ == "__main__":
    raise SystemExit(main(len(sys.argv), sys.argv))
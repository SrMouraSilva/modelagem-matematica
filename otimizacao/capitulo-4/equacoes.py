import sympy as sp
from sympy.utilities.lambdify import lambdify
import math


def equacoes_aproximacao_linear(x, y, hessiana):
    x1, x2 = sp.var('x1 x2', real=True)
    
    sistema_linear = hessiana * sp.Matrix([[x1], [x2]])
    
    f1, f2 = sistema_linear
    f1_atualizado = lambdify([x1, x2], f1)
    f2_atualizado = lambdify([x1, x2], f2)
    
    return f1_atualizado(x, y), f2_atualizado(x, y)


def solucao_geral(c1, c2, t, hessiana):
    solucao_geral = None
    t_var = sp.var(f't', real=True)
    variaveis = []
    for i, (autovalor, multiplicity, matriz) in enumerate(sp.simplify(hessiana).eigenvects()):
        ci = sp.var(f'c{i+1}', real=True)
        variaveis.append(ci)
        
        if solucao_geral is None:
            solucao_geral = ci * matriz[0].as_mutable() * sp.exp(autovalor*t_var)
        else:
            solucao_geral = solucao_geral + ci * matriz[0].as_mutable() * sp.exp(autovalor*t_var)

    variaveis.append(t_var)
    
    f1, f2 = solucao_geral
    f1_atualizado = lambdify(variaveis, f1)
    f2_atualizado = lambdify(variaveis, f2)
    
    return f1_atualizado(c1, c2, t), f2_atualizado(c1, c2, t)
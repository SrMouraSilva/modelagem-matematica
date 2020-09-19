from sympy import *
from IPython.display import display, Math, Markdown

def markdown(string):
    display(Markdown(string))
def math(string):
    display(Math(string))

def latexc(entrada):
    return latex(entrada, decimal_separator="comma")

def forma_geral(hessiana, solucoes):
    for solucao in solucoes:
        forma_geral_solucao(hessiana, solucao)
        
def forma_geral_solucao(hessiana, solucao):
    markdown(f'## Solução: {solucao}')
    markdown('### Hessiana')
    hessiana = simplify(hessiana.subs(solucao))
    display(hessiana)

    markdown('### Sistema Linear ')
    x1, x2 = var('x1 x2', real=True)
    x1l, x2l = var("x'_1 x'_2", real=True)
    matrizx1lx2l = Matrix([[x1l], [x2l]])
    matrizx1x2 = Matrix([[x1], [x2]])
    math(f'{latexc(matrizx1lx2l)}={latexc(hessiana)}{latexc(matrizx1x2)}')
    math(f'{latexc(matrizx1lx2l)}={latexc(hessiana*matrizx1x2)}')

    markdown('### Solução geral: ')
    t = var(f't', real=True)
    e = var(f'e', real=True)
    l = var(f'\lambda', real=True)

    matriz00 = Matrix([[0], [0]])
    matrizLambda = Matrix([[l, 0], [0, l]])

    partes = []
    for i, (autovalor, multiplicity, matriz) in enumerate(simplify(hessiana).eigenvects()):
        ci = var(f'c{i+1}', real=True)
        partes.append([ci, matriz[0], e**(autovalor*t)])

        markdown(f"""
* **Multiplicidade**: {multiplicity}
* **Autovalor:** {autovalor}
* **Autovetor**
        """)
        display(Math(f'{latexc(matrizLambda-hessiana)}{latexc(matrizx1x2)}={latexc(matriz00)}'))
        display(Math(f'{latexc((matrizLambda-hessiana).subs({l: autovalor}))}{latexc(matrizx1x2)}={latexc(matriz00)}'))
        display(Math(f'{latexc(matrizx1x2)}={latexc(matriz[0])}'))

    #Eq(x1x2, partes[0] + partes[1])
    markdown('**General solution to this linear system**')
    parte1 = ''.join([latexc(it) for it in partes[0]])
    parte2 = ''.join([latexc(it) for it in partes[1]])
    math(f'{latexc(matrizx1x2)}={parte1}+{parte2}')
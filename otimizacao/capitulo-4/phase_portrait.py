import locale
import matplotlib as mpl
from equacoes import equacoes_aproximacao_linear, solucao_geral
import numpy as np
import matplotlib.pyplot as plt
from IPython.display import set_matplotlib_formats
import sympy as sp

locale.setlocale(locale.LC_NUMERIC, "pt_BR.UTF-8")
mpl.rcParams['axes.formatter.use_locale'] = True
set_matplotlib_formats('pdf')
plt.rcParams["figure.figsize"] = (8, 8)


def phase_portrait(linhas, H, solucao, linspace):
    x1, x2 = sp.var('x1 x2', real=True)
    
    s = float(solucao[x1]), float(solucao[x1])
    x1min, x1max = (0-1, 0+1)
    x2min, x2max = (0-1, 0+1)

    fig = plt.figure(num=1)
    ax=fig.add_subplot(111)

    hessiana = H.subs(solucao)

    x1graf, x2graf = np.meshgrid(np.linspace(x1min, x1max, 25), np.linspace(x2min, x2max, 25))

    for x, y in linhas:
        linha = solucao_geral(x, y, linspace, hessiana)
        plt.plot(*linha, 'r:')

    f1, f2 = equacoes_aproximacao_linear(x1graf, x2graf, hessiana)
    normalizador = np.sqrt(f1**2+f2**2)
    plt.quiver(x1graf, x2graf, f1/normalizador, f2/normalizador, color='#156dbd', angles='xy')

    ax = plt.axes()
    ax.set_xlim([x1min, x1max])
    ax.set_ylim([x2min, x2max])
    ax.set_xlabel('$x_1$')
    ax.set_ylabel('$x_2$')

    plt.show()
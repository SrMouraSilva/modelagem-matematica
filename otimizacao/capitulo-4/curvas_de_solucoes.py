import numpy as np
from scipy.integrate import ode


def curvas_de_solucoes(pontos_iniciais, equacoes, ax):
    '''
    # https://stackoverflow.com/a/18833385/1524997
    '''
    cores = ['gray' for i in pontos_iniciais]
    cores[-1] = 'red'

    vf = lambda t, x: np.array(equacoes(x[0], x[1]))

    t0=0; tEnd=5000; dt=1;
    r = ode(vf).set_integrator('vode', method='bdf', max_step=dt)
    
    for p, i in enumerate(pontos_iniciais):
        Y=[];T=[];S=[];
        r.set_initial_value(i, t0).set_f_params()
        while r.successful() and r.t + dt < tEnd:
            r.integrate(r.t+dt)
            Y.append(r.y)

        S = np.array(np.real(Y))
        ax.plot(S[:,0],S[:,1], color=cores[p], lw = 1.25)
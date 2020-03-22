import pylab as pl

def plot(RES):
    pl.figure(figsize=(10, 6))

    pl.title('1.1 Modelo SIR simples sem nascimentos e mortes')
    pl.plot(RES[:,0], '-g', label='Sucetíveis')
    pl.plot(RES[:,1], '-r', label='Infectados')
    pl.plot(RES[:,2], '-k', label='Recuperados')

    pl.legend(loc=0)

    pl.xlabel('Tempo (dias)')
    pl.ylabel('Proporção da população')

    pl.show()

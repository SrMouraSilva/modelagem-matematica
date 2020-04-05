from plot import plot
import pandas as pd
import numpy as np
import pylab as pl

import locale
locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

from src.dataset import dataset
from src.utils import rmse


class Relatorio:
    def __init__(self, parametros, resultado):
        self.parametros = parametros
        self.resultado = resultado
        self.dataset = dataset(self.parametros.pais)

    def relatorio(self):
        print('===============================')
        print(f' País: {self.parametros.pais}')
        print('===============================')
        print()
        print('Parâmetros')
        print('-------------------------------')
        print(f' - υ: Taxa de natalidade: {self.parametros.υ}')
        print(f' - μ: Taxa de mortalidade (por mortes naturais): {self.parametros.μ}')
        print()
        print(f' - γ: Taxa de recuperação: {self.parametros.γ}')
        print(f'   -> 1/γ: Período infeccioso médio: {self.parametros.γ ** -1} dias')
        print(f' - ρ: Probabilidade de falecimento: {self.parametros.ρ * 100:.2f}%')
        print(f' - β: Taxa de transmissão: {self.parametros.β}')

        pico = np.argmax(self.I)
        dia_primeira_infeccao = self.dataset.dateRep.values[0]
        dia_pico = self.dataset.date.values[0] + np.timedelta64(pico, "D")
        dia_pico_formatado = pd.to_datetime(str(dia_pico)).strftime('%d/%m/%Y')

        print()
        print(f'Datas')
        print('-------------------------------')
        print(f'{dia_primeira_infeccao} - Data de identificação do primeiro infectado')
        print(f'{dia_pico_formatado} - Dia de pico de infectados ({pico}º dia de contágio)')
        
        print()
        print(f'População')
        print('-------------------------------')
        
        populacao_inicial = sum(self.resultado[0,:3])
        populacao_final = sum(self.resultado[-1,:3])
        habitantes = np.ceil(populacao_inicial - populacao_final)
        mortos_virus = self.resultado[-1,3]

        
        print(f'População inicial:   {locale.format("%d", populacao_inicial, grouping=True)} habitantes (100%)')
        print(f'População em um ano: {locale.format("%d", populacao_final, grouping=True)} habitantes ({(populacao_final/populacao_inicial) * 100:.2f}%)')
        print(f' - Diferença na população em um ano: {locale.format("%d", habitantes, grouping=True)} de habitantes a menos')
        print(f' - População morta pelo SARS-COV-2 em um ano: {locale.format("%d", mortos_virus, grouping=True)} habitantes')
        
        print()
        
        print()
        print(f'Comparação com o cenário atual')
        print('-------------------------------')
        casos_reais = self.dataset.cum_cases.values
        dias = len(casos_reais)
        print('RMSE: ', rmse(casos_reais, self.I[:dias]))
        #print('RMSE: ', rmse(casos_reais/self.parametros.P_0, self.I[:dias]/self.parametros.P_0))

    def plot(self):
        self.plot_geral()
        self.plot_comparativo()

    def plot_geral(self):
        pl.figure(figsize=(10, 6))
        pl.title('Modelo SIR com mortalidade induzida por doença:\nTransmissão dependente da frequência')

        pl.plot(self.S, '-', color='#0173b2', linewidth=2.5, label='Suscetíveis')
        pl.plot(self.I, '-', color='#de8f05', linewidth=2.5, label='Infectados')
        pl.plot(self.R, '-', color='#949494', linewidth=2.5, label='Recuperados')
        pl.plot(self.D, '-', color='#ece133', linewidth=2.5, label='Mortes')

        pl.plot(self.P, '--k', label='População total')
        pl.xlabel('Tempo (em dias)')
        pl.legend(loc=0)
        pl.ylabel('População')
        pl.show()

    def plot_comparativo(self):
        casos_reais = self.dataset.cum_cases.values
        total_dias = len(casos_reais) + 7

        mortos_dia_a_dia = [ontem - hoje for hoje, ontem in zip(self.P[1:], self.P)]
        
        dia_primeira_infeccao = self.dataset.dateRep.values[0]
        dia_final = self.dataset.date.values[0] + np.timedelta64(total_dias, "D")
        dia_final_formatado = pd.to_datetime(str(dia_final)).strftime('%d/%m/%Y')
        
        pl.figure(figsize=(10, 6))
        pl.title(f'Número de infectados e predição entre os dias {dia_primeira_infeccao} e {dia_final_formatado}')
        pl.plot(self.I[:total_dias], '-', color='#de8f05', linewidth=2., label='Infectados - Predição')
        pl.plot(casos_reais, 'xr', color='#8c0800', linewidth=2., label='Infectados - Confirmados')

        pl.legend(loc=0)
        pl.xlabel('Tempo (em dias)')
        pl.ylabel('População')
        pl.show()

    @property
    def S(self):
        return self.resultado[:, 0]

    @property
    def I(self):
        return self.resultado[:, 1]

    @property
    def R(self):
        return self.resultado[:, 2]
    
    @property
    def D(self):
        return self.resultado[:, 3]
    
    @property
    def P(self):
        return sum([self.S, self.I, self.R])
import pandas as pd
import numpy as np

def dataset(pais):
    dataset = all()
    dataset['date'] = pd.to_datetime(dataset.dateRep, format='%d/%m/%Y')

    first_date = dataset[(dataset.countriesAndTerritories == pais) & (dataset.cases > 0)].sort_values(by='date').iloc[0].dateRep
    dataset_pais = dataset[(dataset.countriesAndTerritories == pais) & (dataset.date >= first_date)].sort_values(by='date').copy()

    dataset_pais['cum_cases'] = np.cumsum(dataset_pais.cases)
    dataset_pais['cum_deaths'] = np.cumsum(dataset_pais.deaths)
    
    return dataset_pais

def all(data='17-05-2020'):
    return pd.read_csv(f'./src/dataset-{data}.csv', encoding='iso-8859-1')

def mortalidade(base):
    return base.deaths.sum()/base.cases.sum()

def dataset_estado(sigla):
    import pandas as pd
    data = pd.read_excel('./src/HIST_PAINEL_COVIDBR_20200516.xlsx')

    data['cum_cases'] = data.casosAcumulado
    data['cum_deaths'] = data.obitosAcumulado
    data['date'] = pd.to_datetime(data.data, format='%Y-%m-%d')
    data['dateRep'] = data.data

    data = data[(data.estado == sigla) & data.codmun.isnull()].copy()
    data['cases'] = data.casosAcumulado.values - np.concatenate([[0], data.casosAcumulado[:-1].values])
    data['deaths'] = data.obitosAcumulado.values - np.concatenate([[0], data.obitosAcumulado[:-1].values])

    return data

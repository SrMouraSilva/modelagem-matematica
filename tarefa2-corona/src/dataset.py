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
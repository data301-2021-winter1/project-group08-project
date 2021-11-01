import pandas as pd
import numpy as np

def load_and_process(path_to_csv_file):
    
    bc = (
        pd.read_csv('C:/Users/mille/school/year3/Data301/project-group08-project/data/processed/Bitcoin Historical Data cleaned.csv')
        .rename(columns={'Close':'Close BC'})
        .rename(columns={'Open':'Open BC'})
        .rename(columns={'High':'High BC'})
        .rename(columns={'Low':'Low BC'})
        .rename(columns={'Vol.':'Vol. BC'})
    )
    bc = bc.iloc[::-1]
    bc = bc.reset_index(drop=True)
    bc = bc.dropna(axis=0)

    eth_rounded = (
        pd.read_csv('C:/Users/mille/school/year3/Data301/project-group08-project/data/processed/etherium cleaned.csv')
        .rename(columns={'Close':'Close ETH'})
        .rename(columns={'Open':'Open ETH'})
        .rename(columns={'High':'High ETH'})
        .rename(columns={'Low':'Low ETH'})
        .rename(columns={'Volume':'Vol. ETH'})
        .rename(columns={'Date':'Date ETH'})
    )
    eth_rounded = np.round(eth, decimals = 2)   
    merge = pd.concat([bc, eth_rounded], axis=1)
    merge = merge.head(2177)
    merge =merge.drop('Date ETH', axis=1)
    merge
    return merge
merge
import pandas as pd
import numpy as np

def load_and_process_file1(path):   
    
    
    btc = (
        pd.read_csv(path)
        .rename(columns={'Vol.':"Volume"})
        .iloc[::-1]
        .reset_index(drop=True))

    
    btc['Open']=(btc['Open'].str.replace(',','').astype(float))
    btc['Close']=(btc['Close'].str.replace(',','').astype(float))
    btc['High']=(btc['High'].str.replace(',','').astype(float))
    btc['Low']=(btc['Low'].str.replace(',','').astype(float))
    btc['Volume']=(btc['Volume'].str.replace('K','000').str.replace('M','000000').astype(float))



    btc['Date']=(btc['Date'].str.replace('Jan','01')
                 .str.replace('Feb','02')
                 .str.replace('Mar','03')
                 .str.replace('Apr','04')
                 .str.replace('May','05')
                 .str.replace('Jun','06')
                 .str.replace('Jul','07')
                 .str.replace('Aug','08')
                 .str.replace('Sep','09')
                 .str.replace('Oct','10')
                 .str.replace('Nov','11')
                 .str.replace('Dec','12')
                 .str.replace(',','')
                 .str.replace(' ','')
                 .astype(float))
    btc['Date'] = (pd.to_datetime(btc['Date'], format='%m%d%Y')
                   
    return btc


def load_and_process_file2(path):
    eth =(pd.read_csv(path)
         .dropna(axis=0)
          .iloc[::-1]
          .reset_index(drop=True)
         )
    eth['Date'] = pd.to_datetime(eth['Date'], format='%d/%m/%y')
    
    return eth


def merge_and_process_dataframes(file1, file2):
    merge1=pd.merge(btc,eth,on="Date",how="inner")
    merge1.columns= [x.replace('_x','_btc') for x in merge1.columns]
    merge1.columns=[x.replace('_y','_eth') for x in merge1.columns]
    
    return merge1
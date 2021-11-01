import pandas as pd
import numpy as np 

def load_and_process_file1(data_path): 
    #method chain 1
    eth=(
    pd.read_csv(data_path)
      .dropna(axis=0)
      .reindex(columns=[ 'Date', 'Open', 'Close', 'High', 'Low', 'Volume'])
      .iloc[::-1]
      .reset_index(drop=True)
)
    eth['Date'] = pd.to_datetime(eth['Date'], format='%d/%m/%y')
    return eth
    
def load_and_process_file2(data_path):
    #Method chain1
    bit=(
    pd.read_csv(data_path)
     .rename(columns={'Vol.': 'Volume'}) 
     .reindex(columns=[ 'Date', 'Open', 'Close', 'High', 'Low', 'Volume'])
     .iloc[::-1]
     .reset_index(drop=True))
    #method chain 2
    bit['Open'] =( 
    bit['Open'].str.replace(',', '')
      .astype(float))
    #method chain 3
    bit['Close'] = (
    bit['Close'].str.replace(',', '')
      .astype(float))
    #method chain4
    bit['High'] = (
    bit['High'].str.replace(',', '')
      .astype(float))
    #method chain5
    bit['Low'] =(
    bit['Low'].str.replace(',', '')
      .astype(float))
    #method chain 6
    bit['Volume']=(
    bit['Volume'].str.replace('.','')
        .str.replace('K','000')
        .str.replace('M','000000')
        .astype(float))
    #method chain 7
    bit['Date']=(
    bit['Date'].str.replace('Jan','01')
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
   .str.replace(' ',''))
    bit['Date'] = pd.to_datetime(bit['Date'], format='%m%d%Y')

    return bit

def merge_and_process_dataframes(file1, file2):
    merge1=pd.merge(file1,file2,on="Date",how="inner")
    merge1.columns= [x.replace('_x','_bit') for x in merge1.columns]
    merge1.columns= [x.replace('_y','_eth') for x in merge1.columns]
    
    return merge1
{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "17ca3d86-9b5b-4101-966d-1547dba68892",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "import numpy as np \n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "255d1889-4ef7-4f8d-ade5-ff4ca6e43f42",
   "metadata": {},
   "outputs": [
    {
     "ename": "NameError",
     "evalue": "name 'eth' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "\u001b[0;32m<ipython-input-6-5498443f9dad>\u001b[0m in \u001b[0;36m<module>\u001b[0;34m\u001b[0m\n\u001b[1;32m      8\u001b[0m       \u001b[0;34m.\u001b[0m\u001b[0mreset_index\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mdrop\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0;32mTrue\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      9\u001b[0m )\n\u001b[0;32m---> 10\u001b[0;31m \u001b[0meth\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0;34m'Date'\u001b[0m\u001b[0;34m]\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mpd\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mto_datetime\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0meth\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0;34m'Date'\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mformat\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0;34m'%d/%m/%y'\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m     11\u001b[0m \u001b[0;32mreturn\u001b[0m \u001b[0meth\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     12\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;31mNameError\u001b[0m: name 'eth' is not defined"
     ]
    }
   ],
   "source": [
    "def load_and_process_file1(data_path): \n",
    "    #method chain 1\n",
    "   eth=(\n",
    "    pd.read_csv(data_path)\n",
    "      .dropna(axis=0)\n",
    "      .reindex(columns=[ 'Date', 'Open', 'Close', 'High', 'Low', 'Volume'])\n",
    "      .iloc[::-1]\n",
    "      .reset_index(drop=True)\n",
    ")\n",
    "eth['Date'] = pd.to_datetime(eth['Date'], format='%d/%m/%y')\n",
    "return eth\n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "d9522e03-a04a-449a-aa9b-6b7e924db3d5",
   "metadata": {},
   "outputs": [
    {
     "ename": "NameError",
     "evalue": "name 'bit' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "\u001b[0;32m<ipython-input-5-2477d7e35b05>\u001b[0m in \u001b[0;36m<module>\u001b[0;34m\u001b[0m\n\u001b[1;32m     45\u001b[0m    \u001b[0;34m.\u001b[0m\u001b[0mstr\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mreplace\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m','\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m''\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     46\u001b[0m    .str.replace(' ',''))\n\u001b[0;32m---> 47\u001b[0;31m \u001b[0mbit\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0;34m'Date'\u001b[0m\u001b[0;34m]\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mpd\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mto_datetime\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mbit\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0;34m'Date'\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mformat\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0;34m'%m%d%Y'\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m     48\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     49\u001b[0m \u001b[0;32mreturn\u001b[0m \u001b[0mbit\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;31mNameError\u001b[0m: name 'bit' is not defined"
     ]
    }
   ],
   "source": [
    "def load_and_process_file2(data_path):\n",
    "    #Method chain1\n",
    "    bit=(\n",
    "    pd.read_csv(data_path)\n",
    "     .rename(columns={'Vol.': 'Volume'}) \n",
    "     .reindex(columns=[ 'Date', 'Open', 'Close', 'High', 'Low', 'Volume'])\n",
    "     .iloc[::-1]\n",
    "     .reset_index(drop=True))\n",
    "    #method chain 2\n",
    "    bit['Open'] =( \n",
    "    bit['Open'].str.replace(',', '')\n",
    "      .astype(float))\n",
    "    #method chain 3\n",
    "    bit['Close'] = (\n",
    "    bit['Close'].str.replace(',', '')\n",
    "      .astype(float))\n",
    "    #method chain4\n",
    "    bit['High'] = (\n",
    "    bit['High'].str.replace(',', '')\n",
    "      .astype(float))\n",
    "    #method chain5\n",
    "    bit['Low'] =(\n",
    "    bit['Low'].str.replace(',', '')\n",
    "      .astype(float))\n",
    "    #method chain 6\n",
    "    bit['Volume']=(\n",
    "    bit['Volume'].str.replace('.','')\n",
    "        .str.replace('K','000')\n",
    "        .str.replace('M','000000')\n",
    "        .astype(float))\n",
    "    #method chain 7\n",
    "    bit['Date']=(\n",
    "bit['Date'].str.replace('Jan','01')\n",
    "   .str.replace('Feb','02')\n",
    "   .str.replace('Mar','03')\n",
    "   .str.replace('Apr','04')\n",
    "   .str.replace('May','05')\n",
    "   .str.replace('Jun','06')\n",
    "   .str.replace('Jul','07')\n",
    "   .str.replace('Aug','08')\n",
    "   .str.replace('Sep','09')\n",
    "   .str.replace('Oct','10')\n",
    "   .str.replace('Nov','11')\n",
    "   .str.replace('Dec','12')\n",
    "   .str.replace(',','')\n",
    "   .str.replace(' ',''))\n",
    "bit['Date'] = pd.to_datetime(bit['Date'], format='%m%d%Y')\n",
    "\n",
    "return bit\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "82b9b82b-c2d8-4b71-bf2a-bf4fb3e8a46a",
   "metadata": {},
   "outputs": [
    {
     "ename": "SyntaxError",
     "evalue": "'return' outside function (<ipython-input-7-311b3b7d73bf>, line 6)",
     "output_type": "error",
     "traceback": [
      "\u001b[0;36m  File \u001b[0;32m\"<ipython-input-7-311b3b7d73bf>\"\u001b[0;36m, line \u001b[0;32m6\u001b[0m\n\u001b[0;31m    return merge1\u001b[0m\n\u001b[0m    ^\u001b[0m\n\u001b[0;31mSyntaxError\u001b[0m\u001b[0;31m:\u001b[0m 'return' outside function\n"
     ]
    }
   ],
   "source": [
    "def merge_and_process_dataframes(file1, file2):\n",
    "    merge1=pd.merge(file1,file2,on=\"Date\",how=\"inner\")\n",
    "    merge1.columns= [x.replace('_x','_bit') for x in merge1.columns]\n",
    "    merge1.columns= [x.replace('_y','_eth') for x in merge1.columns]\n",
    "    \n",
    "return merge1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "c2e77373-9e30-45ad-9ed0-12357bf9f790",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}

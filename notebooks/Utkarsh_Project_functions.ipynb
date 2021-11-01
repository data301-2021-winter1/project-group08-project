{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "ebb7a2e4-afd2-4369-adf1-47c32e860dbd",
   "metadata": {},
   "outputs": [],
   "source": [
    "def load_and_process_file1(data_path): \n",
    "    #method chain 1\n",
    "    eth=(\n",
    "    pd.read_csv(data_path)\n",
    "      .dropna(axis=0)\n",
    "      .reindex(columns=[ 'Date', 'Open', 'Close', 'High', 'Low', 'Volume'])\n",
    "      .iloc[::-1]\n",
    "      .reset_index(drop=True)\n",
    ")\n",
    "eth['Date'] = pd.to_datetime(eth['Date'], format='%d/%m/%y')\n",
    " return eth\n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "430d6924-def0-41c7-a82a-d96ad52c1993",
   "metadata": {},
   "outputs": [],
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
    " return bit\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "6348ca30-f312-4e04-9861-f23aefadaf40",
   "metadata": {},
   "outputs": [],
   "source": [
    "def merge_and_process_dataframes(file1, file2):\n",
    "    merge1=pd.merge(file1,file2,on=\"Date\",how=\"inner\")\n",
    "    merge1.columns= [x.replace('_x','_bit') for x in merge1.columns]\n",
    "    merge1.columns= [x.replace('_y','_eth') for x in merge1.columns]\n",
    "    \n",
    "    return merge1"
   ]
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

#!/usr/bin/env python
# coding: utf-8

# # Imports

# In[59]:


import pandas as pd
import numpy as np

import sys


# # Constants

# In[60]:


CD_CONTA = 'CD_CONTA'
DS_CONTA = 'DS_CONTA'


# In[61]:


file_name = sys.argv[1]
output_name = 'output.csv'


# In[62]:


CNPJ_CIA = '97.837.181/0001-47'
ORDEM_EXERC = 'ÚLTIMO'


# # Read from file

# ## Load .csv

# In[63]:


try:
    cia_aberta_df = pd.read_csv(file_name, encoding='ISO-8859-1', sep=';')
except Exception as e:
    print(f"Error: {e}")


# ## Select Company

# In[64]:


df = cia_aberta_df[cia_aberta_df['CNPJ_CIA'] == CNPJ_CIA].copy()    # seleciono somente as linhas relativas a uma companhia de interesse
df = df[df['ORDEM_EXERC'] == ORDEM_EXERC]                           # seleciono somente o último ou penúltimo exercício
df = df[[CD_CONTA, DS_CONTA,'VL_CONTA']]
df.reset_index(inplace=True, drop=True)


# In[65]:


# # Wrangling

# ## Number of steps

# In[66]:


cd_conta_split = df[CD_CONTA].str.split('.')
cd_conta_len = [len(cd_to_lst) for cd_to_lst in cd_conta_split]    # cd_to_lst = code to list
num_levels = max(cd_conta_len)


# In[67]:


# ## For Loop

# In[68]:


range_rounds = range(1, num_levels)

for round in range_rounds:

    ### Merge
    """
    We want to find which codes have minimum lenght. The minimum length should correspond to the round number
    (the minimum length at round `1` should be `1`, at round `2` should be `2`, etc.).
    """
    len_cd = [len(cd) for cd in df[CD_CONTA]]           # len_CD = length of codes in 'CD_CONTA'
    min_len = np.array(len_cd).min()            # min_len = minimum length of codes

    """
    Now that we have a column of code lengths named `cd_conta_len`, we just need to find which index corresponds to the codes with minimum length.
    We store this list of indexes in a variable named `ind_min_len`.
    """
    ind_min_len = np.where(len_cd==min_len)[0]          # ind_min_len = index of code 'CD_CONTA' with minimum length
    
    """
    Now that we have a list of the indexes of the codes which correspond to the highest rank, we need to join the corrisponding description to all the indexes of lowest rank.
    For example: the description corrisponding to `1` will be assigned to all the codes which start with `1` (`1.01` , `1.01.01`...), the description corrisponding to `2` will be assigned to all the codes which start with `2`, et cetera.

    We'll first store a list of the join keys in the variable `merge_keys` and then create a dataframe named `merge_df` with the join keys as keys and the description extracted from `DS_CONTA` as values.
    """
    merge_keys = df[CD_CONTA].apply(lambda string: string[:min_len])
    merge_df = pd.merge(merge_keys, df[[CD_CONTA, DS_CONTA]], how='left')

    ### Insert
    df.insert(round, f'{DS_CONTA}_{round}', merge_df[DS_CONTA])

    ### Drop
    """
    For each key which was used to join, we check if the code in the next row in `CD_CONTA` starts with the same key (example: `CD_CONTA` `1.01` starting with `1`; `CD_CONTA` `1.01.01` starting with `1.01`, etc.)
    If so, we can safely delete the row.
    Otherwise, we keep the row and add `.00` to the code in `CD_CONTA`, so the code can have the correct length in the next round (length 2 in round 2, length 3 in round 3, etc.)
    """
    for idx in ind_min_len:
        if merge_df.loc[idx, CD_CONTA] == merge_df.loc[idx+1, CD_CONTA]:
            df = df.drop(idx)
        else:
            df.loc[idx, CD_CONTA] = df.loc[idx, CD_CONTA] + '.00'

    df.reset_index(inplace=True, drop=True)

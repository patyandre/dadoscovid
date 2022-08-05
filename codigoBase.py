#!/usr/bin/env python
# coding: utf-8

# In[31]:


import pandas as pd
import plotly.express as px
import streamlit as st


# In[32]:


#streamlit run codigoBase.py


# In[33]:


#LENDO O DATASET
df = pd.read_csv('https://raw.githubusercontent.com/wcota/covid19br/master/cases-brazil-states.csv')


# In[34]:


#MELHORANDO O NOME DAS COLUNAS DA TABELA
df = df.rename(columns={'newDeaths': 'Novos óbitos','newCases': 'Novos casos','deaths_per_100k_inhabitants': 'Óbitos por 100 mil habitantes','totalCases_per_100k_inhabitants':'Casos por 100 mil habitantes'})


# In[35]:


#SELECÃO DO ESTADO
estados = list(df['state'].unique())
state = st.sidebar.selectbox('Qual estado?', estados)


# In[36]:


#SELEÇÃO DA COLUNA
#column ='Casos por 100 mil habitantes'
colunas = ['Novos óbitos','Novos casos','Óbitos por 100 mil habitantes','Casos por 100 mil habitantes']
column = st.sidebar.selectbox('Qual tipo de informação?', colunas)


# In[37]:


#SELEÇÃO DAS LINHAS QUE PERTECEM AO ESTADO 
df = df[df['state'] == state]


# In[38]:


fig = px.line(df, x="date", y=column, title=column + ' - ' + state)
fig.update_layout( xaxis_title='Data', yaxis_title=column.upper(), title = {'x':0.5})


# In[39]:


st.title('DADOS COVID - BRASIL')
st.write('Nessa aplicação, o usuário tem a opção de escolher o estado e o tipo de informação para mostrar o gráfico. Utilize o menu lateral para alterar a mostragem.')


# In[40]:


st.plotly_chart(fig, use_container_width=True)


# In[41]:



st.caption('Os dados foram obtidos a partir do site: https://github.com/wcota/covid19br')


# In[ ]:





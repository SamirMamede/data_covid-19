import pandas as pd
import plotly.express as px
import streamlit as st #rodando o código "streamlit run nome_do_codigo.py"

dados = pd.read_csv("https://raw.githubusercontent.com/wcota/covid19br/master/cases-brazil-states.csv")

# renomeando colunas para melhorar apresentação
dados = dados.rename(columns={'newDeaths':'Novos óbitos', 'newCases':'Novos casos', 'deaths_per_100k_inhabitants':'Óbitos por 100 mil habitantes', 'totalCases_per_100k_inhabitants':'Casos por 100 mil habitantes'})

# seleção do estado
# inserindo na mão -> state = 'AM'
estados = list(dados['state'].unique())
state = st.sidebar.selectbox('Estado', estados)

# seleção da coluna
# column = 'Casos por 100 mil habitantes'
informacoes = ['Novos hábitos', 'Novos casos', 'Óbitos por 100 mil habitantes', 'Casos por 100 mil habitantes']
column = st.sidebar.selectbox('Dados', informacoes)

# seleção das linhas que pertencem ao estado
dados = dados[dados['state'] == state]

# plotando imagem
fig = px.line(dados, x='date', y=column, title=column + ' - ' + state)
fig.update_layout(xaxis_title='Data', yaxis_title=column.upper(), title = {'x':0.5})

# inserindo textos na aplicação
#print('DADOS COVID-19 BRASIL')
st.title('DADOS COVID-19 BRASIL')
st.write('Escolha o estado, os dados no menu lateral e visualize um gráfico interativo contendo as informações desejadas.')
st.caption('Os dados foram obtidos a partir de: https://raw.githubusercontent.com/wcota/covid19br/master/cases-brazil-states.csv')

#fig.show()
st.plotly_chart(fig, use_container_width=True)
import pandas as pd
url = 'https://raw.githubusercontent.com/alura-cursos/pandas-conhecendo-a-biblioteca/main/base-de-dados/aluguel.csv'
dados = pd.read_csv(url, sep=';')

# SALVANDO DADOS E CRIANDO UM ARQUIVO CVS GUARDANDO ELES
dados.to_csv('dados_moveis.cvs', index=True, sep=';')

# CRIANDO COLUNAS NÚMERICAS
# SIMPLES
dados ['Valor_por_mes' ] = dados['Valor' ] + dados['Condominio' ]
print(dados.head())

# MAIS ELABORADA
dados ['Valor_por_ano' ] = dados['Valor_por_mes' ] * 12 + dados['IPTU' ]
print(dados.head())

# CRIANDO COLUNAS CATEGÓRICAS (STRINGS) O METODO ASTYPE (STR) CONVERTE AQUELE VALOR PARA UMA STRING
# SIMPLES
dados['Descricao' ] = dados['Tipo'] + ' em ' + dados['Bairro']
print(dados.head())

# MAIS ELABORADA
dados['Descricao' ] = dados['Tipo' ] + ' em ' + dados['Bairro'] + ' com ' + \
dados['Quartos' ].astype(str) + ' quarto(s) ' + \
'e ' + dados['Vagas'].astype(str) + ' vaga(s) de garagem. '

print(dados.head())


# CRIANDO COLUNA BINÁRIA
# LAMBDA: CRIAÇÃO DE FUNÇÕES RAPIDAS
dados['Possui_suite' ] = dados['Suites' ].apply(lambda x: "Sim" if x > 0 else "Não")
print(dados.head())


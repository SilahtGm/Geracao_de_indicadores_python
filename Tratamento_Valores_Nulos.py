import pandas as pd

url = 'https://raw.githubusercontent.com/alura-cursos/pandas-conhecendo-a-biblioteca/main/base-de-dados/aluguel.csv'
dados = pd.read_csv(url, sep=';')

# CHECANDO SE ALGUMA INFORMAÇÃO É NULL, SE FOR ESTARÁ COMO TRUE
print(dados.isnull())

# EXIBE QUANTOS VALORES NULL TEM EM TODA A LISTA EM CADA COLUNA
print(dados.isnull().sum())

# PREENCHENDO OS VALORES NULOS COM 0
print(dados.fillna(0))

# ARMAZENANDO NA VARIAVEL DF O DATAFRAME DADOS COM OS VALORES NULOS PREENCHIDOS POR 0
df = dados.fillna(0)

# REMOVE TODAS AS LINHAS QUE POSSUEM NO MINIMO UMA INFORMAÇÃO NULA
print (dados.dropna())

# ARMAZENANDO O DATAFRAME SEM DADOS NULOS E EXBIBINDO VALORES NULOS POR COLUNA
tb = dados.dropna()
print (tb.isnull().sum())

# PREENCHE OS VALORES NULOS COM O VALOR DA LINHA ANTERIOR
print(dados.fillna(method='ffill'))

# PREENCHE OS VALORES NULOS COM O VALOR DA LINHA POSTERIOR
print(dados.fillna(method='bfill'))

# PREENCHE OS VALORES NULOS COM VALORES CALCULADOS APARTIR DE VALORES VIZINHOS
print(dados.interpolate())
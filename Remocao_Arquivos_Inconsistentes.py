import pandas as pd

url = 'https://raw.githubusercontent.com/alura-cursos/pandas-conhecendo-a-biblioteca/main/base-de-dados/aluguel.csv'
dados = pd.read_csv(url, sep=';')

# APENAS PREENCHENDO VALORES NULOS COM 0 PARA NOSSAS PROXIMAS OPERAÇÕES
dados = dados.fillna(0)

# BUSCANDO VALORES ESPECIFICOS E TRAZENDO SEUS INDICES ATRAVES DE .INDEX
print(dados.query('Valor == 0 | Condominio == 0').index)

# ARMAZENANDO EM UMA VARIAVEL OS DADOS QUE QUEREMOS EXCLUIR
registros_a_remover = dados.query('Valor == 0 | Condominio == 0').index

# UTILIZANDO O METODO DROP PARA APAGAR REGISTROS
# AXIS, 0 QUER DIZER QUE QUEREMOS APAGAR LINHAS, 1 QUER DIZER QUE QUEREMOS APAGAR COLUNAS
# INPLACE QUER DIZER QUE ESSAS ALTERAÇÕES SEJAM DEFINITIVAMENTE ALTERADAS EM NOSSO DATAFRAME
dados.drop(registros_a_remover, axis=0, inplace=True)
print(dados.query('Valor == 0 | Condominio == 0').index)
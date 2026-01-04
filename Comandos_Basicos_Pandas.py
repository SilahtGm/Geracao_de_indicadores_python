# IMPORTANDO A BIBLIOTECA PANDAS
import pandas as pd

# ARMAZENANDO O CSV NA VARIAVEL URL
url = "https://raw.githubusercontent.com/alura-cursos/pandas-conhecendo-a-biblioteca/main/base-de-dados/aluguel.csv"

# ARMAZENANDO O RETORNO DA FUNÇÃO PD.READ_CSV, QUE NOS RETORNA A LEITURA DO CSV
dados = pd.read_csv(url, sep=';')

# EXIBE O CVC, OS 5 PRIMEIROS E OS 5 UTIMOS (PORQUE O CSV É ENORME)
print (dados)

# EXIBE AS 10 PRIMEIRAS COLUNAS DA VARIAVEL DADOS, QUE ARMAZENA O CSV
print (dados.head(10))

# EXIBE OS 10 ULTIMOS
print (dados.tail(10))

# EXIBE O TIPO DE DADO DA NOSSA VARIAVEL DADOS, QUE É DO TIPO DATAFRAME
print (type(dados))

# EXIBE A QUANTIDADE DE LINHAS E COLUNAS
print (dados.shape)

# EXIBE OS NOMES DAS COLUNAS
print (dados.columns)

# EXIBE OS TIPOS DE DADOS QUE PODEM SER ARMAZENADOS EM CADA COLUNA
print (dados.info())

# EXIBE O TIPO DE DADO QUE PODE SER ARMAZENADO EM UMA COLUNA ESPECIFICA
print (dados['Tipo'])

# EXIBE OS TIPOS DE DADOS QUE PODEM SER ARMAZENADOS EM DUAS COLUNAS
print (dados[['Quartos', 'Valor']])
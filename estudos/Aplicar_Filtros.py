import pandas as pd

url = 'https://raw.githubusercontent.com/alura-cursos/pandas-conhecendo-a-biblioteca/main/base-de-dados/aluguel.csv'
dados = pd.read_csv(url, sep=';')

# GUARDANDO EM UMA VARIAVEL OS REGISTROS QUARTOS QUE POSSUEM APENAS O VALOR 1 E EXIBIMOS ATRAVES DE DADOS[VARIAVEL]
selecao = dados['Quartos'] == 1
print(dados[selecao])

# GUARDANDO EM UMA VARIAVEL OS REGISTROS DOS ALUGUEIS QUE POSSUEM APENAS O VALOR MENOR QUE 1200 E EXIBIMOS ATRAVES DE DADOS[VARIAVEL]
selecao2= dados['Valor'] < 1200
print(dados[selecao2])

# EXIBINDO TODOS QUE POSSUEM OS QUARTS IGUAL A 1 E VALORES DE ALUGUÉIS MENORES QUE 1200
selecao_final = (selecao) & (selecao2)
print(dados[selecao_final])

# EXIBINDO APARTAMENTOS QUE POSSUEM PELO MENOS 2 QUARTOS, ALUGUEL MENOR QUE 3000 E AREA MAIOR
# QUE 70
f = (dados['Quartos'] >= 2) & (dados['Valor'] < 3000) & (dados['Area'] > 70)
print(dados[f])

# ARMAZENANDO EM UMA VARIAVEL PARA FACIL ACESSO
filtro = dados[f]
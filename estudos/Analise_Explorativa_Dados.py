import pandas as pd
import matplotlib.pyplot as plt

url = 'https://raw.githubusercontent.com/alura-cursos/pandas-conhecendo-a-biblioteca/main/base-de-dados/aluguel.csv'
dados = pd.read_csv(url, sep=';')

print (dados['Valor'].mean())

# TRÁS A MÉDIA DE CADA COLUNA, QUE TENHA APENAS NUMERO, AGRUPANDO PELO TIPO
print (dados.groupby('Tipo').mean(numeric_only=True))

# AGRUPANDO A MÉDIA DO VALOR DE CADA TIPO
print (dados.groupby('Tipo')['Valor'].mean())

# AGRUPANDO A MÉDIA DO VALOR DE CADA TIPO, DO MENOR PARA O MAIOR ATRAVEZ DE VALOR
print (dados.groupby('Tipo')[['Valor']].mean().sort_values('Valor'))

# CRIANDO A VARIAVEL GRAFICO, ARMAZENANDO NELA OS DADOS JA AGRUPADOS E CRIANDO UM GRAFICO COM O METODO .PLOT
grafico = dados.groupby('Tipo')[['Valor']].mean().sort_values('Valor')

grafico.plot(kind='barh', figsize=(14, 10), color='purple')

# EXIBIÇÃO DO GRAFICO
plt.show()

# EXIBINDO TODOS OS TIPOS DE TIPO, DE FORMA UNICA SEM REPETIR
print (dados.Tipo.unique())

# EXIBIR SEM ALGUNS TIPOS ESPECIFICOS
imoveis_comerciais = ['Conjunto Comercial/Sala',
                      'Prédio Inteiro', 'Loja/Salão',
                      'Galpão/Depósito/Armazém',
                      'Casa Comercial', 'Terreno Padrão',
                      'Loja Shopping/ Ct Comercial',
                      'Box/Garagem', 'Chácara',
                      'Loteamento/Condomínio', 'Sítio',
                      'Pousada/Chalé', 'Hotel', 'Indústria']

# METODO QUE ESPECIFICA O QUE QUEREMOS SELECIONAR E O QUE QUEREMOS FAZER COM ELA, O @ É POR CONTA QUE É UMA VARIAVEL. EXIBINDO APENAS OS TIPOS
# DE COMERCIAIS
dados.query('@imoveis_comerciais in Tipo')

# EXIBINDO O QUE NÃO QUEREMOS
dados.query('@imoveis_comerciais not in Tipo')

# ARMAZENANDO EM UMA VARIAVEL O CONTEUDO COM APENAS OS TIPOS QUE QUEREMOS E EXIBINDO
dt = dados.query('@imoveis_comerciais not in Tipo')

print(dt.Tipo.unique())

# EXIBIR QUANTAS VEZES AQUELE TIPO APARECEU NO CSV INTEIRO
print (dt.Tipo.value_counts())

# EXIBINDO QUANTAS VEZES AQUELE TIPO APARECEU, EM PERCENTUAL. EM UM GRAFICO DE BARRA
dt_percentual_tipo = dt.Tipo.value_counts(normalize=True).to_frame().sort_values('Tipo')

dt_percentual_tipo.plot(kind='bar', figsize=(14, 10), color ='green',
xlabel = 'Tipos', ylabel = 'Percentual');

plt.show()

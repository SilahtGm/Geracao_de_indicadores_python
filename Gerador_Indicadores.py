# IMPORTANDO BIBLIOTECAS
import pandas as pd
from pandas.errors import EmptyDataError, ParserError

# --- FUNÇÕES UTILITÁRIAS ---
def pausar():
    # ESSA FUNÇÃO SEGURA A TELA PARA VOCÊ LER A MENSAGEM ANTES DE LIMPAR
    input("\nPRESSIONE [ENTER] PARA CONTINUAR...")
    print("\n\n\n\n")

# FUNÇÕES PRINCIPAIS

def carregar_base_de_dados():
    try:
        url = 'https://raw.githubusercontent.com/alura-cursos/pandas-conhecendo-a-biblioteca/main/base-de-dados/aluguel.csv'
        dados = pd.read_csv(url, sep=';')
        print("🔄 Conectando ao servidor...")
        print("✅ Arquivo carregado com sucesso!")

        # Tratamento preventivo: preencher vazios com 0 para não quebrar contas
        dados.fillna(0, inplace=True)

        return dados

    except FileNotFoundError:
        print("❌ Erro: URL não encontrada.")
    except EmptyDataError:
        print("❌ Erro: Arquivo vazio.")
    except ParserError:
        print("❌ Erro: Formato inválido (separador errado?).")
    except Exception as e:
        print(f"❌ Erro inesperado: {e}")


# FUNÇÕES MENU DE INDICADORES

def media_valor_aluguel(dados):
    media = dados['Valor'].mean()
    print(f"💰 Média Geral do Aluguel: R${media:.2f}")
    pausar()


def custo_total_medio(dados):
    aluguel = dados['Valor']
    condominio = dados['Condominio']
    iptu = dados['IPTU']
    custo_individual = aluguel + condominio + iptu
    media_total = custo_individual.mean()
    print(f"📦 Custo Total Médio (Pacote Completo): R$ {media_total:.2f}")

def bairros_mais_carros(dados):
    ranking = dados.groupby('Bairro')['Valor'].mean().sort_values(ascending=False).head(10).round(2)

    print("--- 🏆 TOP 10 BAIRROS MAIS CAROS (Média) ---")
    print(ranking)
    pausar()


def preco_medio_m2(dados):
    dados_validos = dados.query('Area > 0 & Valor > 0')

    valor_m2 = dados_validos['Valor'] / dados_validos['Area']

    media = valor_m2.mean()

    print(f"📐 Preço Médio do m² no Dataset: R$ {media:.2f}")
    pausar()


def imoveis_m2_barato(dados):
    dados['Valor_m2'] = (dados['Valor'] / dados['Area']).round(2)
    df_filtrado = dados.query('Valor_m2 > 0')

    ranking = df_filtrado.sort_values('Valor_m2', ascending=True).head(10)
    print("\n--- 📉 TOP 10 OPORTUNIDADES (Menor R$/m²) ---")
    print(ranking[['Bairro', 'Valor', 'Area', 'Valor_m2']])
    pausar()


def imoveis_por_tipo(dados):
    tabela_distribuicao = dados['Tipo'].value_counts().to_frame(name='Quantidade')

    tabela_distribuicao.index.name = 'Tipo de Imóvel'

    print("\n--- 🏘️ DISTRIBUIÇÃO POR TIPO DE IMÓVEL ---")
    print(tabela_distribuicao)
    pausar()


# FUNÇÕES MENU DE EXPORTAÇÃO

def salvar_arquivo(dataframe, nome):
    try:
        dataframe.to_csv(f"{nome}.csv", sep=';', index=True, encoding='utf-8-sig')
        print(f"\n✅ Arquivo '{nome}.csv' gerado com sucesso!")
    except PermissionError:
        print(f"❌ Erro: O arquivo '{nome}.csv' está aberto em outro programa. Feche-o e tente novamente.")
    except Exception as e:
        print(f"❌ Ocorreu um erro inesperado ao salvar: {e}")
    finally:
        pausar()


def exportar_apartamentos(dados):
    resultado = dados.query("Tipo == 'Apartamento'")
    salvar_arquivo(resultado, "lista_apartamentos")

def exportar_imoveis_comerciais(dados):
    comerciais = ['Conjunto Comercial/Sala', 'Loja/Salão', 'Galpão/Depósito/Armazém']
    resultado = dados.query("Tipo in @comerciais")
    salvar_arquivo(resultado, "imoveis_comerciais")

def exportar_imoveis_baratos(dados):
    resultado = dados.query("Valor > 0 and Valor <= 1500")
    salvar_arquivo(resultado, "imoveis_populares")

def exportar_preco_medio_bairro(dados):
    resumo = dados.groupby('Bairro')['Valor'].mean().sort_values().to_frame()
    salvar_arquivo(resumo, "media_precos_por_bairro")



# FUNÇÕES MENU DE BUSCA

def exibir_comerciais(dados):
    imoveis_comerciais = ['Conjunto Comercial/Sala',
                          'Prédio Inteiro', 'Loja/Salão',
                          'Galpão/Depósito/Armazém',
                          'Casa Comercial', 'Terreno Padrão',
                          'Loja Shopping/ Ct Comercial',
                          'Box/Garagem', 'Chácara',
                          'Loteamento/Condomínio', 'Sítio',
                          'Pousada/Chalé', 'Hotel', 'Indústria']

    dt = dados.query('Tipo in @imoveis_comerciais ')
    print(dt[['Tipo', 'Bairro', 'Valor', 'Area']].head(10))
    print(f"\nTotal encontrados: {len(dt)}")
    pausar()

def exibir_para_estudante(dados):
    imoveis_baratos = dados.query('Valor <= 1000 & Area < 60')
    print(imoveis_baratos[['Tipo', 'Bairro', 'Valor', 'Area']].head(10))
    print(f"\nTotal encontrados: {len(imoveis_baratos)}")
    pausar()

def exibir_imoveis_flat(dados):
    print("\n--- 🏖️ FLATS E APART-HOTÉIS ---")
    imoveis_flat = dados.query("Tipo == 'Flat'")
    print(imoveis_flat[['Bairro', 'Valor', 'Condominio']].head(10))
    print(f"\nTotal encontrados: {len(imoveis_flat)}")
    pausar()

def exibir_imoveis_alto_padrao(dados):
    imoveis_alto_padrao = dados.query('Valor > 10000 | Area > 300')
    print(imoveis_alto_padrao[['Tipo', 'Bairro', 'Valor', 'Area']].head(10))
    print(f"\nTotal encontrados: {len(imoveis_alto_padrao)}")
    pausar()

# FUNÇÕES DO MENU
def menu_indicadores(dados):
    while True:
        print("==================================================")
        print("PAINEL DE INDICADORES 📊")
        print("==================================================")

        print(f"Base carregada: aluguel.csv  (possuindo {dados.shape[0]} linhas)\n")
        print("--- 💰 FINANCEIRO - --")
        print("[1] Média do Valor do Aluguel (Geral)")
        print("[2] Custo Total Médio (Aluguel + Condomínio + IPTU)")
        print("[3] Ranking: Top 10 Bairros Mais Caros\n")
        print("--- 📐 TÉCNICO ---")
        print("[4] Preço Médio do m² (Valor / Area)")
        print("[5] Imóveis com m² mais barato (Oportunidades)\n")
        print("--- 🏘️ CATEGORIZAÇÃO ---")
        print("[6] Distribuição: Quantidade de Imóveis por Tipo")
        print("--------------------------------------------------")
        print("[7] 🔙 Voltar ao Menu Principal")
        print("==================================================")
        op = input("Qual indicador deseja visualizar? ")

        match op:
            case "1":
                    media_valor_aluguel(dados)

            case "2":
                    custo_total_medio(dados)

            case "3":
                    bairros_mais_carros(dados)

            case "4":
                    preco_medio_m2(dados)

            case "5":
                    imoveis_m2_barato(dados)

            case "6":
                    imoveis_por_tipo(dados)

            case "7":
                    print("Retornando ao Menu Principal...")
                    return
            case _:
                    print("❌ Opção Inválida. Tente novamente.")


def menu_filtros(dados):
    while True:
        print("==================================================")
        print("          🔍 BUSCA AVANÇADA ")
        print("==================================================")
        print(f"Base ativa: {dados.shape[0]} registros\n")

        print("[1] 🏢 Comerciais: (Salas, Lojas e Galpões)")
        print("[2] 🎓 Estudante/Solteiro: (Até R$ 1.000,00 e pequeno)")
        print("[3] 🏖️ Flats e Apart-Hotéis: (Para temporada)")
        print("[4] 💎 Alto Padrão: (Aluguel > 10k ou Área > 300m²)")

        print("\n--------------------------------------------------")
        print("[5] 🔙 Voltar ao Menu Principal")
        print("==================================================")

        op = input("Selecione o filtro: ")

        match op:
            case "1":
                exibir_comerciais(dados)
            case "2":
                exibir_para_estudante(dados)
            case "3":
                exibir_imoveis_flat(dados)
            case "4":
                exibir_imoveis_alto_padrao(dados)
            case "5":
                return
            case _:
                print("❌ Opção Inválida.")


def menu_exportacao(dados):
    while True:
        print("==================================================")
        print("          💾 GERAR ARQUIVOS PARA A EQUIPE")
        print("==================================================")
        print("Escolha qual lista você deseja salvar em Excel/CSV:\n")

        print("[1] 🏠 Lista de Apartamentos (Para Vendas)")
        print("[2] 🏢 Lista de Imóveis Comerciais (Para Expansão)")
        print("[3] 💰 Lista de Imóveis 'Baratos' (Até R$ 1.500)")
        print("[4] 📐 Tabela de Preço Médio por Bairro")
        print("\n--------------------------------------------------")
        print("[5] 🔙 Voltar ao Menu Principal")
        print("==================================================")

        op = input("Opção de exportação: ")

        match op:
            case "1":
                exportar_apartamentos(dados)

            case "2":
                exportar_imoveis_comerciais(dados)

            case "3":
                exportar_imoveis_baratos(dados)

            case "4":
                exportar_preco_medio_bairro(dados)



            case "5":
                return
            case _:
                print("❌ Opção Inválida.")






# MENU PRINCIPAL

dados = None

while True:
    print("==================================================\n🏦 SISTEMA DE GESTÃO DE IMÓVEIS (v1.0)")
    print("==================================================")
    # Mostra o status atual
    if dados is not None:
        status = "✅ Carregado"
    else:
        status = "🔴 Pendente"
    print(f"STATUS: {status}")
    print("--------------------------------------------------")
    print("[1] 📂 Carregar Base de Dados (CSV)")
    print("[2] 📊 Painel de Indicadores (Dashboard)")
    print("[3] 🔍 Filtros e Busca Personalizada")
    print("[4] 💾 Exportar Relatórios")
    print("[0] ❌ Sair do Sistema")
    print("==================================================")
    op = input("Digite a opção desejada: ")
    print("\n\n\n\n")

    match op:
        case "1":
            if dados is None:
                print("Carregando Base de Dados CSV.")
                dados = carregar_base_de_dados()
            else:
                print("Base de dados já foi carregada com sucesso!.")
                pausar()
        case "2":
            if dados is not None:
                menu_indicadores(dados)
            else:
                print("Carregue a base de dados antes de tentar acessar esse serviço")
                pausar()
        case "3":
            if dados is not None:
                menu_filtros(dados)
            else:
                print("Carregue a base de dados antes de tentar acessar esse serviço")
                pausar()
        case "4":
            if dados is not None:
                menu_exportacao(dados)
            else:
                print("Carregue a base de dados antes de tentar acessar esse serviço")
                pausar()
        case "0":
            print("Obrigado por usar nosso programa, até breve!\nEncerrando programa...")
            break
        case _:
            print("❌ Opção Inválida. Tente novamente.")



# 🏦 Sistema de Gestão de Imóveis (v1.0)

Este projeto é uma ferramenta de linha de comando (CLI) desenvolvida em **Python** e **Pandas** para análise de dados do setor imobiliário. O sistema foi projetado para transformar bases de dados brutas (CSV) em relatórios de inteligência para tomada de decisão.



## 🚀 Funcionalidades

O sistema está dividido em quatro módulos principais:

1.  **Carregamento e Limpeza:** Importação automática via URL com tratamento de exceções (arquivos vazios, corrompidos ou inexistentes) e tratamento de dados nulos (`fillna`).
2.  **Painel de Indicadores:** * Cálculo de Ticket Médio de Aluguel e Custo Total (Aluguel + Condomínio + IPTU).
    * Cálculo técnico de Valor por m².
    * Ranking de bairros com maior valorização.
3.  **Busca Avançada (Filtros):**
    * Segmentação para imóveis comerciais, residenciais compactos (estudantes), Flats e imóveis de Alto Padrão.
4.  **Módulo de Exportação:**
    * Geração de arquivos CSV formatados com `utf-8-sig` para compatibilidade direta com Microsoft Excel.

## 🛠️ Tecnologias Utilizadas

* **Python 3.10+**
* **Pandas:** Biblioteca principal para manipulação e análise de dados.
* **Try/Except:** Tratamento de erros em tempo de execução.
* **Match/Case:** Estrutura de menus moderna e organizada.

## 📊 Estrutura do Projeto

* `main.py`: Código-fonte principal com toda a lógica do sistema.
* `aluguel.csv`: Base de dados utilizada (Consumo via URL do GitHub).

## 💡 Aprendizados Técnicos

Durante o desenvolvimento deste projeto, foram aplicados conceitos fundamentais de análise de dados:
- **Higiene de Dados:** Filtragem de `outliers` e remoção de valores que causariam erros matemáticos (como divisão por zero).
- **Feature Engineering:** Criação de novas métricas (como o Valor do m²) a partir das colunas existentes.
- **Segurança de Execução:** Implementação de `PermissionError` para evitar travamentos caso o usuário tente salvar um arquivo que já está aberto.

## ✒️ Autor

* **Thalis** - [Seu Perfil no GitHub](https://github.com/seu-usuario)

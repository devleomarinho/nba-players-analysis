# Análise sobre as estatísticas de jogadores da NBA nas últimas 20 temporadas regulares (2003-04 a 2023-24)

Este projeto foi desenvolvido para analisar as estatísticas de líderes da NBA ao longo das últimas 20 temporadas. Os dados foram extraídos diretamente do site oficial da NBA usando **web scraping** e analisados com as bibliotecas **pandas**, **matplotlib** e **seaborn**.

## 📊 Dados

O arquivo CSV contém as seguintes colunas:

- `SEASON`: Temporada
- `PLAYER_ID`: Identificador do jogador
- `RANK`: Ranking
- `PLAYER`: Nome do jogador
- `TEAM_ID`: Identificador do time
- `TEAM`: Nome do time
- `GP`: Jogos disputados
- `MIN`: Minutos jogados
- `PTS`: Pontos
- `REB`: Rebotes
- `AST`: Assistências
- (e outras estatísticas relacionadas, como roubos de bola, turnovers, etc.)

## 🚀 Objetivo

O objetivo deste projeto é explorar as estatísticas dos jogadores da NBA ao longo das temporadas, identificar tendências, outliers, e fazer comparações entre jogadores e times.

## 📋 Etapas de Análise

1. **Coleta de Dados**: Extraí os dados através de um script de web scraping.
2. **Limpeza de Dados**: Removi colunas redundantes e corrigi erros nos dados.
3. **Estatísticas Descritivas**: Fiz uma visão geral das principais métricas dos jogadores.
4. **Boxplots**: Criei visualizações para Pontos, Rebotes e Assistências ao longo das temporadas, com o objetivo de identificar padrões e variações.
5. **Matriz de Correlação**: Analisei a relação entre diferentes estatísticas dos jogadores, como a correlação entre Pontos, Assistências e Rebotes.
6. **Tendências ao Longo do Tempo**: Plotei gráficos de linha mostrando a evolução das médias de Pontos, Rebotes e Assistências por temporada.
7. **Identificação de Outliers**: Identifiquei jogadores cujas performances se destacam em relação à média.
8. **Comparações entre Jogadores e Times**: Comparei jogadores e times específicos ao longo das temporadas em termos de pontos e outras métricas.

## 🛠️ Ferramentas Utilizadas

- **Python**
- **requests** 
- **pandas**
- **matplotlib**
- **seaborn**

## 🔍 Como Utilizar

1. Clone este repositório:
   ```bash
   git clone https://github.com/devleomarinho/nba-players-analysis.git

2. Execute o notebook com as análises:
```bash
   jupyter notebook nba_analysis_notebook.ipynb

```
## 📈 Exemplos de Visualizações

- **Boxplot de Pontos ao Longo das Temporadas**

![box_plot_pts_season](https://github.com/user-attachments/assets/df10cd31-676b-4bcc-8ac7-e8502c810e0e)

- **Boxplot de Rebotes ao Longo das Temporadas**

![box_plot_rebs_season](https://github.com/user-attachments/assets/5cb57166-db36-4afb-a32d-0dc61ba453a0)

- **Boxplot de Assistências ao Longo das Temporadas**

![box_plot_asts_season](https://github.com/user-attachments/assets/f0998ae0-955d-42c0-89d4-221015ae667b)

- **Tendência de Pontos, Rebotes e Assistências ao Longo do Tempo**


![tendencias](https://github.com/user-attachments/assets/4513437d-95b0-41b6-8895-9f4ab64c4085)

- **Comparativo entre dois jogadores (Lebron James X Kevin Durant)**

![lebronxdurant](https://github.com/user-attachments/assets/12343cfc-95a9-4054-a98c-c0c0e766c0c7)

- **Comparativo entre dois times (Los Angeles Lakers X Boston Celtics)**

![lalxceltics](https://github.com/user-attachments/assets/9e457a95-f8d4-428b-b3e1-84e1747ff745)






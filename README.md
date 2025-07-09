# Inteligência de Negócios - Trabalho 4
Sistemas de recomendação por meio de aprendizado supervisionado utilizando algoritmos de Classificação

## Base de Dados
- Base de dados escolhida: [Kaggle](https://www.kaggle.com/datasets/niharika41298/nutrition-details-for-most-common-foods/code)
- Base de dados tratada: [Google Planilhas](https://docs.google.com/spreadsheets/d/1-nJOtXDaHU-WekuMImalBGv_LQBZ3n-whrviVCkw6F4/edit?usp=sharing)

## Comandos para Venv do Python
1 Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
2 python -m venv .venv
3 .\.venv\Scripts\activate
4 pip install Flask pypmml pandas
8 code .
9 python app.py

## Melhores Acurácias
| Algoritmo | CS(i) | Clusters |
| --- | :---: | :---: |
| **k-Means** | 0.371 | 3 |
| **Fuzzy** | 0.396 | 7 |
| **k-Medoids** | 0.320 | 9 |
| **Hierárquico (Manhattan)** | 0.722 | 2 |
| **Hierárquico (Manhattan)** | 0.722 | 2 |

## Respectivos Gráficos

k-Means:
![Imagem - gráfico do k-Means](https://github.com/JoaoAugusto2020/IN-Trab3/blob/main/imgs/graficos/k-Means%20(3%20Clusters).png "k-Means")

Fuzzy:
![Imagem - gráfico do Fuzzy](https://github.com/JoaoAugusto2020/IN-Trab3/blob/main/imgs/graficos/Fuzzy%20(7%20Clusters).png "Fuzzy")

k-Medoids:
![Imagem - gráfico do k-Medoids](https://github.com/JoaoAugusto2020/IN-Trab3/blob/main/imgs/graficos/k-Medoids%20(9%20Clusters).png "k-Medoids")

Hierárquico:
![Imagem - gráfico do Hierárquico](https://github.com/JoaoAugusto2020/IN-Trab3/blob/main/imgs/graficos/Hierárquico-Manhattan%20(2%20Clusters).png "Hierárquico")

Hierárquico:
![Imagem - gráfico do Hierárquico](https://github.com/JoaoAugusto2020/IN-Trab3/blob/main/imgs/graficos/Hierárquico-Manhattan%20(2%20Clusters).png "Hierárquico")

## Resultado
Considerando as Silhuetas e os Gráficos do melhor resultado de todos os algoritmos, chega-se à conclusão de que o melhor algoritmo a ser usado no sistema é o k-Means com 3 clusters pois este possui uma silhueta com valor minimamente bom e um gráfico com cluster bem formados.

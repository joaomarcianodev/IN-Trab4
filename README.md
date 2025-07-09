# Inteligência de Negócios - Trabalho 4
Sistemas de recomendação por meio de aprendizado supervisionado utilizando algoritmos de Classificação

## Base de Dados
- Base de dados escolhida: [Kaggle](https://www.kaggle.com/datasets/uom190346a/sleep-health-and-lifestyle-dataset)
- Colunas Utilizadas:
1. Age, 
2. Sleep Duration, 
4. Physical Activity Level, 
7. Gender (to number), 
8. Occupation (to number),
9. BMI Category (to number),
3. Quality of Sleep, [REMOVIDO PELO CORRELATION FILTER]
5. Stress Level, [REMOVIDO PELO CORRELATION FILTER]
6. Sleep Disorder [TARGET]

## Comandos para Venv do Python
1 Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
2 python -m venv .venv
3 .\.venv\Scripts\activate
4 pip install Flask pypmml pandas
8 code .
9 python app.py

## Análise do Scorer de cada algoritmo
| Algoritmo | Acurácia | Kappa |
| --- | :---: | :---: |
| **Random Forest Learner** | 90,9% | 0,84% |
| **Decision Tree Learner** | 89,5% | 0,81% |
| **PNN Learner (DDA)** | 88,7% | 0,80% |
| **K Nearest Neighbor** | 86,9% | 0,76% |
| **SVM Learner** | 85,8% | 0,75% |

## Respectivos Scores
Random Forest Learner:
![Imagem - Scorer do Random Forest Learner](https://github.com/joaomarcianodev/IN-Trab4/blob/main/static/imgs/Scores/Scorer%20-%20Random%20Forest%20Learner.svg "Random Forest Learner")

Decision Tree Learner:
![Imagem - Scorer do Decision Tree Learner](https://github.com/joaomarcianodev/IN-Trab4/blob/main/static/imgs/Scores/Scorer%20-%20Decision%20Tree%20Learner.svg "Decision Tree Learner")

PNN Learner (DDA):
![Imagem - Scorer do PNN Learner (DDA)](https://github.com/joaomarcianodev/IN-Trab4/blob/main/static/imgs/Scores/Scorer%20-%20PNN%20Learner%20(DDA).svg "PNN Learner (DDA)")

K Nearest Neighbor:
![Imagem - Scorer do K Nearest Neighbor](https://github.com/joaomarcianodev/IN-Trab4/blob/main/static/imgs/Scores/Scorer%20-%20K%20Nearest%20Neighbor.svg "K Nearest Neighbor")

SVM Learner:
![Imagem - Scorer do SVM Learner](https://github.com/joaomarcianodev/IN-Trab4/blob/main/static/imgs/Scores/Scorer%20-%20SVM%20Learner.svg "SVM Learner")

## Resultado
Considerando a **Acurácia** de todos os algoritmos, chega-se à conclusão de que o melhor algoritmo de classificação a ser usado sistemas de recomendação por meio de aprendizado supervisionado é o **Random Forest Learner** pois este possui a maior acurácia, logo também, maior taxa de acertos nas previsões.

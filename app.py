from flask import Flask, request, render_template
from pypmml import Model
import pandas as pd

model = Model.fromFile('knime/sleep-health.pmml')

# valores Mínimos e Máximos para a normalização (baseado no dataset original)
# os nomes das chaves devem corresponder aos nomes dos campos no PMML.
LIMITES = {
    'Age': {'min': 27, 'max': 59},
    'Sleep Duration': {'min': 5.8, 'max': 8.5},
    'Physical Activity Level': {'min': 30, 'max': 90},
    'Gender (to number)': {'min': 0, 'max': 1},
    'Occupation (to number)': {'min': 0, 'max': 9},
    'BMI Category (to number)': {'min': 0, 'max': 2}
}

app = Flask(__name__, template_folder='templates')

@app.route('/analise')
def analise():
    return render_template('analise.html')

@app.route('/sobre')
def sobre():
    return render_template('sobre.html')

@app.route('/', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        try:
            # normalizar os dados
            def normalize(valor, min_val, max_val):
                if max_val == min_val:
                    return 0.0
                return (valor - min_val) / (max_val - min_val)

            # converter horas em float
            def converterHoras(tempoSonoStr):
                horas_str, minutos_str = tempoSonoStr.split(':')
                tempoSonoFloat = int(horas_str) + (int(minutos_str) / 60.0)
                print(f"O horario convertido ficou: {tempoSonoFloat}")
                return tempoSonoFloat

            # dados da requisição, tipo: dicionário (semelhante ao JSON)
            # os nomes das chaves (colunas) devem ser igual as colunas do PMML
            request_raw = {
                'Age': float(request.form['idade']),
                'Sleep Duration': converterHoras(request.form['tempoSono']),
                'Physical Activity Level': float(request.form['minutosAtividade']),
                'Gender (to number)': int(request.form['genero']),
                'Occupation (to number)': int(request.form['profissao']),
                'BMI Category (to number)': int(request.form['peso'])
            }

            # dados da requisição normalizados (dicionário)
            dados_normalizados = {}
            for coluna, valor in request_raw.items():
                min_val = LIMITES[coluna]['min']
                max_val = LIMITES[coluna]['max']
                
                dados_normalizados[coluna] = [normalize(valor, min_val, max_val)]

            # o resultado é um DataFrame do Pandas.
            previsao_dataFrame = model.predict(pd.DataFrame(dados_normalizados))

            # a biblioteca pypmml retorna a previsão em uma coluna chamada 'predicted_NOME_DA_VARIAVEL_ALVO'.
            diagnostico = previsao_dataFrame['predicted_Sleep Disorder'].iloc[0]

            # resultado traduzido
            if diagnostico == 'None':
                previsao_html = "Diagnóstico Previsto: Nenhum distúrbio do sono detectado."
            elif diagnostico == 'Sleep Apnea':
                previsao_html = "Diagnóstico Previsto: Apneia do Sono."
            elif diagnostico == 'Insomnia':
                previsao_html = "Diagnóstico Previsto: Insônia."
            else:
                previsao_html = f"Diagnóstico Previsto: {diagnostico}"

        except (ValueError, KeyError) as e:
            # KeyError acontece se um campo do formulário não for encontrado.
            # ValueError se a conversão para int/float falhar.
            previsao_html = f'Erro nos dados de entrada: {e}. Por favor, preencha todos os campos corretamente.'
        except Exception as e:
            previsao_html = f'Ocorreu um erro inesperado ao processar a requisição: {e}'
        
        return render_template('index.html', previsao_html=previsao_html, mostrar_boolean=True)
    else:
        return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)



#! DETALHES IMPORTANTES SOBRE O PYTHON
#* Lista (list) é isso: 
# nomes_frutas = ["maçã", "banana", "laranja"]

#* Dicionário (dict) é isso: 
# informacoes_pessoa = {
#    'nome': 'João Silva',
#    'idade': 20,
#    'cidade': 'Patrocínio',
#    'ativo': True
#    'data_criacao': None
# }

#* JSON (JavaScript Object Notation) é isso:
# dados_em_json = '{
#   "nome": "Maria Costa", 
#   "idade": 25, "habilidades": 
#       [
#       "Python", 
#       "SQL", 
#       "APIs"
#   ]
# }'

#* DataFrame (Pandas) é isso [dados tabulados]:
# import pandas as pd

# dados = {
#    'Nome': ['Carlos', 'Ana', 'Pedro'],
#    'Idade': [28, 34, 29],
#    'Cidade': ['Rio de Janeiro', 'Salvador', 'Belo Horizonte']
# }

# df = pd.DataFrame(dados)
# print(df)

#? DIFERENÇA importante entre Dicionário e JSON:
# Dicionário: É um objeto dentro do seu código Python. Você o utiliza para trabalhar com dados na memória, acessando, adicionando e modificando seus elementos de forma dinâmica.
# JSON: É uma string (texto puro). Ele não é usável diretamente para manipulação de dados em Python; sua finalidade é armazenar esses dados em um arquivo ou enviá-los pela internet para outra aplicação.
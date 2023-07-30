import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Função para converter avaliações de 1 a 5 em 100 a 500
def converter_avaliacao(valor):
    return valor * 100

# Função para calcular o valor final do imóvel
def calcular_valor_imovel(avaliacao_inicial, saude, seguranca, educacao, lazer, comercial):
    descontos = (saude + seguranca + educacao + lazer + comercial) / 5
    valor_final = avaliacao_inicial - descontos
    return descontos, valor_final

# Função para criar o gráfico de linha
def exibir_grafico(avaliacoes, descontos):
    categorias = ["Saúde", "Segurança", "Educação", "Lazer e Diversão", "Comercial"]
    
    plt.plot(categorias, avaliacoes, marker='o', linestyle='-', color='b', label='Avaliações')
    plt.plot(categorias, descontos, marker='o', linestyle='-', color='r', label='Descontos')
    
    plt.xlabel('Categorias')
    plt.ylabel('Avaliações/Descontos')
    plt.title('Avaliações e Descontos do Imóvel')
    plt.legend()
    plt.grid(True)
    st.pyplot()

# Configurações da página do Streamlit
st.set_page_config(page_title="Avaliação de Imóvel", layout="wide")

# Título e descrição da página
st.title("Avaliação de Imóvel")
st.write("Para uma melhor padronização, utilize a escala de 1 a 5, onde 1 indica péssimo e 5 indica ótimo.")

# Obter avaliações do usuário
avaliacao_inicial = st.number_input("Informe o valor da avaliação inicial do imóvel:", min_value=0.0)
saude = st.slider("Avaliação de Saúde:", min_value=1, max_value=5, step=1, value=3)
seguranca = st.slider("Avaliação de Segurança:", min_value=1, max_value=5, step=1, value=3)
educacao = st.slider("Avaliação de Educação:", min_value=1, max_value=5, step=1, value=3)
lazer = st.slider("Avaliação de Lazer e Diversão:", min_value=1, max_value=5, step=1, value=3)
comercial = st.slider("Avaliação Comercial:", min_value=1, max_value=5, step=1, value=3)

# Converter as avaliações de 1 a 5 para 100 a 500
avaliacao_inicial = converter_avaliacao(avaliacao_inicial)
saude = converter_avaliacao(saude)
seguranca = converter_avaliacao(seguranca)
educacao = converter_avaliacao(educacao)
lazer = converter_avaliacao(lazer)
comercial = converter_avaliacao(comercial)

# Calcular o valor final do imóvel
descontos, valor_final = calcular_valor_imovel(avaliacao_inicial, saude, seguranca, educacao, lazer, comercial)

# Exibir as informações
st.write(f"Valor dos Descontos: {descontos:.2f}")
st.write(f"Valor Final: {valor_final:.2f}")

# Exibir o gráfico de linha
avaliacoes = [saude, seguranca, educacao, lazer, comercial]
exibir_grafico(avaliacoes, [descontos] * len(avaliacoes))

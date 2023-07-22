import streamlit as st
import matplotlib.pyplot as plt

st.title("Olá, Seja Bem-vindo ao nosso código")
st.text("Para uma melhor padronização, nós utilizamos o método de avaliação Numérico de 0 a 10")
st.text("Onde 0 indica péssimo e 10 indica ótimo")

# Calcular o valor final do imóvel
def calcular_valor_imovel(avaliacao_inicial, saude, seguranca, educacao, lazer, comercial):
    descontos = (saude + seguranca + educacao + lazer + comercial) / 5
    valor_final = avaliacao_inicial - descontos
    return descontos, valor_final

# Gráfico de linha
def exibir_grafico(avaliacoes, descontos):
    categorias = ["Saúde", "Segurança", "Educação", "Lazer e Diversão", "Comercial"]

    plt.plot(categorias, avaliacoes, marker='o', linestyle='-', color='b', label='Avaliações')
    plt.plot(categorias, descontos, marker='o', linestyle='-', color='r', label='Descontos')

    plt.xlabel('Categorias')
    plt.ylabel('Avaliações/Descontos')
    plt.title('Avaliações e Descontos do Imóvel')
    plt.legend()
    plt.grid(True)
    plt.xticks(rotation=45)  # Para ajustar a rotação dos rótulos do eixo x
    plt.tight_layout()  # Para evitar cortar os rótulos no gráfico
    return plt

# Avaliações ao usuário
avaliacao_inicial = int(st.text_input("Informe o valor da avaliação inicial do imóvel: "))
saude = int(st.text_input("Avaliação de Saúde: "))
seguranca = int(st.text_input("Avaliação de Segurança: "))
educacao = int(st.text_input("Avaliação de Educação: "))
lazer = int(st.text_input("Avaliação de Lazer e Diversão: "))
comercial = int(st.text_input("Avaliação Comercial: "))

# Calcular o valor final do imóvel
descontos, valor_final = calcular_valor_imovel(avaliacao_inicial, saude, seguranca, educacao, lazer, comercial)

# Exibir as informações
st.text("Valor dos Descontos:", descontos)
st.text("Valor Final:", valor_final)

# Exibir o gráfico de linha
avaliacoes = [saude, seguranca, educacao, lazer, comercial]
plt = exibir_grafico(avaliacoes, [descontos]*len(avaliacoes))
st.pyplot(plt)

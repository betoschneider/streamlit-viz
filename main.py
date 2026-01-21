import streamlit as st
import pandas as pd
import numpy as np

# Função para gerar dados simulados com cache
@st.cache_data
def gerar_dados(pontos, seed):
    rng = np.random.default_rng(seed)
    y = rng.standard_normal(pontos)
    x = np.linspace(y[0], pontos + 1, pontos) * y.mean()
    return pd.DataFrame({"x": x, "y": y})

def main():
    st.set_page_config(
        page_title="Visualização de Dados com Streamlit",
        page_icon=":bar_chart:"
    )

    st.title("📈 Exploração de Dados com Streamlit")
    st.markdown("👈 Utilize a barra lateral para gerar novos dados")

    # Configuração de parâmetros na barra lateral
    with st.sidebar:
        st.write("## Parâmetros")
        pontos = st.slider("Pontos", 0, 500, 250)
        seed = st.number_input("Seed", 0, 100, 50)

    # Gestão de estado e cache dos dados
    if ("df" not in st.session_state) or (st.session_state.get("pontos") != pontos) or (st.session_state.get("seed") != seed):
        st.session_state.df = gerar_dados(pontos, seed)
        st.session_state.pontos = pontos
        st.session_state.seed = seed
    
    # Containers para organizar o layout
    grafico = st.container()
    tabela = st.container()

    # Exibição da tabela e edição de dados
    with tabela:
        st.write("## Dados")
        st.markdown("Essa tabela pode ser editada diretamente")
        df_editado = st.data_editor(
            st.session_state.df,
            key="editor_df",
        )
        st.session_state.df = df_editado

    # Renderização do gráfico
    with grafico:
        st.write("## Gráfico")
        st.line_chart(st.session_state.df)

if __name__ == "__main__":
    main()

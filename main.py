import streamlit as st
import altair as alt
import pandas as pd
import numpy as np

# Função para gerar dados simulados com cache
@st.cache_data
def gerar_dados(pontos, seed):
    rng = np.random.default_rng(seed)
    y = rng.standard_normal(pontos)
    x = np.linspace(y[0], pontos + 1, pontos) * y.mean()
    return pd.DataFrame({"x": x, "y": y})

def grafico_barras(df, bins=10, closed="right"):
    """
    closed:
        'right' -> (a, b]
        'left'  -> [a, b)
    """

    # Cria os bins
    bins_series = pd.cut(df["x"], bins=bins, right=(closed == "right"))

    # Extrai limites numéricos
    labels = []
    for interval in bins_series.cat.categories:
        left = interval.left
        right = interval.right

        if closed == "right":
            label = f"({left:.2f}, {right:.2f}]"
        else:
            label = f"[{left:.2f}, {right:.2f})"

        labels.append(label)

    # Aplica labels customizados
    df_bins = df.copy()
    df_bins["x_bin"] = pd.cut(
        df["x"],
        bins=bins,
        labels=labels,
        right=(closed == "right")
    )

    return (
        alt.Chart(df_bins)
        .mark_bar()
        .encode(
            x=alt.X(
                "x_bin:N",
                title="Intervalo de X",
                sort=labels
            ),
            y=alt.Y("mean(y):Q", title="Média de Y"),
            tooltip=[
                alt.Tooltip("mean(y):Q", title="Média de Y", format=".4f")
            ]
        )
        .properties(height=300)
    )


def box_plot(df):
    return (
        alt.Chart(df)
        .mark_boxplot(extent="min-max")
        .encode(
            y=alt.Y("y:Q", title="Distribuição de Y"),
            tooltip=["min(y):Q", "max(y):Q", "mean(y):Q"]
        )
        .properties(height=300)
    )


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
        pontos = st.slider("Quantidade de Pontos", 0, 500, 250)
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
        st.write("## Gráficos")

        st.subheader("📈 Linha")
        st.line_chart(st.session_state.df)

        st.subheader("📊 Barras (média de Y por intervalo de X)")
        bins = max(1, st.session_state.pontos // 10)
        chart = grafico_barras(
            st.session_state.df,
            bins=bins,
            closed="right"
        )
        st.altair_chart(chart, use_container_width=True)

        st.subheader("📦 Box Plot de Y")
        st.altair_chart(
            box_plot(st.session_state.df),
            use_container_width=True
        )


if __name__ == "__main__":
    main()

# 📈 Exploração de Dados com Streamlit

Este projeto é uma aplicação interativa desenvolvida com [Streamlit](https://streamlit.io/) para visualização e edição de dados gerados aleatoriamente.

## ✨ Funcionalidades

- **Geração Dinâmica de Dados**: Altere a quantidade de pontos e a semente (seed) aleatória através da barra lateral.
- **Gráficos Interativos**: Visualização em tempo real dos dados gerados via `st.line_chart`.
- **Edição de Dados**: Uma tabela interativa (`st.data_editor`) permite modificar os valores diretamente, refletindo instantaneamente no gráfico.
- **Performance**: Utiliza cache (`@st.cache_data`) para otimizar a regeneração de dados.

## 🚀 Como Executar

### Pré-requisitos

- Python 3.12+ 
- [uv](https://github.com/astral-sh/uv) (recomendado) ou pip

### Execução Local

1. Instale as dependências:
   ```bash
   uv sync
   ```
2. Inicie a aplicação:
   ```bash
   uv run streamlit run main.py
   ```

### Execução com Docker

O projeto já está configurado para rodar em containers utilizando a porta **8513**.

1. Suba o container:
   ```bash
   docker-compose up -d --build
   ```
2. Acesse em: `http://localhost:8513`

## 🛠️ Tecnologias Utilizadas

- **Python**: Linguagem principal.
- **Streamlit**: Framework para interface web.
- **Pandas/Numpy**: Manipulação e geração de dados.
- **Docker/Docker Compose**: Containerização.
- **uv**: Gerenciamento de pacotes e ambiente.

---
Desenvolvido como um exemplo de visualização rápida de dados.

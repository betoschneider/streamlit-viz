# Use uma imagem leve do Python
FROM python:3.12-slim

# Instala o uv para gerenciamento de dependências
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

# Define o diretório de trabalho
WORKDIR /app

# Copia os arquivos de configuração de dependências
COPY pyproject.toml uv.lock ./

# Instala as dependências do projeto (sem criar ambiente virtual no container para simplificar)
RUN uv sync --no-cache

# Copia o restante do código da aplicação
COPY . .

# Expõe a porta padrão do Streamlit (será mapeada no docker-compose)
EXPOSE 8501

# Comando para rodar a aplicação
# --server.address=0.0.0.0 é necessário para o Docker
CMD ["uv", "run", "streamlit", "run", "main.py", "--server.port=8501", "--server.address=0.0.0.0"]

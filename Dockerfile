FROM python:3.10-slim-buster

# Atualiza o pip
RUN pip install --upgrade pip

# Cria o diretório de trabalho no contêiner
WORKDIR /app

# Copia o arquivo requirements.txt para o contêiner
COPY requirements.txt .

# Instala as dependências do projeto a partir do arquivo requirements.txt
RUN pip install -r requirements.txt

# Copia o diretório src para o contêiner
COPY src/ /app/src

# Copia o arquivo setup.py para o contêiner
COPY setup.py /app

# Instala o pacote usando o setup.py
RUN python /app/setup.py sdist bdist_wheel
RUN pip install -e /app/.

# Define o comando de entrada para o streamlit
CMD [ "streamlit", "run", "/app/src/app.py"]

# Exponha a porta 8501 para o streamlit
EXPOSE 8501

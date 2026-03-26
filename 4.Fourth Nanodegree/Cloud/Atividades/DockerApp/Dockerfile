# Use a imagem oficial do Python 3.9 como base
FROM python:3.9
# Defina o diretório de trabalho dentro do contêiner
WORKDIR /app
# Copie o arquivo de código-fonte para o diretório de trabalho
COPY . /app
# Instale as dependências do aplicativo
RUN pip install flask
# Exponha a porta em que o aplicativo será executado
EXPOSE 3000
# Comando para iniciar o aplicativo
CMD python app.py
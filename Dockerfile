# Usar uma imagem oficial e leve do Python
FROM python:3.12-slim

# Definir a diretoria de trabalho dentro do contentor
WORKDIR /app

# Copiar apenas o ficheiro de dependências primeiro (otimiza o cache do Docker)
COPY requirements.txt .

# Instalar as dependências sem guardar em cache (para reduzir o tamanho final da imagem)
RUN pip install --no-cache-dir -r requirements.txt

# Copiar o resto do código da aplicação para a diretoria de trabalho
COPY . .

# Expor a porta que o Uvicorn vai utilizar
EXPOSE 8000

# Comando para iniciar a aplicação quando o contentor arrancar
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

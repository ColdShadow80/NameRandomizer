from fastapi import FastAPI, Query
from faker import Faker
from typing import List, Dict

app = FastAPI(
    title="API de Geração de Nomes",
    description="API para gerar nomes e apelidos aleatórios para dados de teste.",
    version="1.0.0"
)

# Inicializar o Faker com a localização portuguesa
# Pode ser alterado para 'pt_BR' para nomes brasileiros, 'en_US' para ingleses, etc.
fake = Faker('pt_PT')

@app.get("/", summary="Endpoint de Boas-vindas")
def root() -> Dict[str, str]:
    return {"mensagem": "API ativa! Acede a /docs para interagir com a documentação Swagger."}

@app.get("/api/nomes", summary="Gerar nomes e apelidos aleatórios")
def gerar_nomes(
    quantidade: int = Query(10, ge=1, le=1000, description="Número de nomes a gerar (entre 1 e 1000)")
) -> Dict[str, List[Dict[str, str]]]:
    """
    Devolve uma lista de dicionários, cada um contendo um 'nome' e um 'apelido'.
    """
    resultados = []
    for _ in range(quantidade):
        resultados.append({
            "nome": fake.first_name(),
            "apelido": fake.last_name()
        })
    
    return {"dados": resultados}

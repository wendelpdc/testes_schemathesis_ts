from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="API de Gestão de Usuários")

class User(BaseModel):
    username: str
    age: int

@app.post("/api/users/", status_code=201)
def create_user(user: User):
    # ERRO 1 (Segurança / DoS): Número absurdo causa crash no servidor (HTTP 500)
    if user.age > 99999:
        return 1 / 0  

    # ERRO 2 (Quebra de Contrato): Retorna string simples em vez do JSON esperado
    if user.username == "admin":
        return "Usuário admin criado!" 

    # CASO DE SUCESSO
    return {"id": 1, "username": user.username, "age": user.age}
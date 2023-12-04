from fastapi import FastAPI, HTTPException
from src.model.partida import Partida

app = FastAPI()
partida = Partida()

@app.post("/entrar_na_fila/{jogador}")
async def entrar_na_fila(jogador: str):
    partida.entrar_na_fila(jogador)
    return {"message": f"{jogador} entrou na fila."}

@app.get("/verificar_partida/{jogador}")
async def verificar_partida(jogador: str):
    return partida.verificar_partida(jogador)

@app.get("/ver_tabuleiro/{jogador}")
async def ver_tabuleiro(jogador: str):
    # Adicione lógica para verificar se o jogador está em uma partida
    if jogador not in partida.fila_jogadores:
        raise HTTPException(status_code=400, detail=f"{jogador} não está em uma partida.")

    # Adicione mais lógica conforme necessário
    tabuleiro = partida.obter_tabuleiro(jogador)
    
    return {"tabuleiro": tabuleiro}

@app.get("/ver_tabuleiro_fantasma/{jogador}")
async def ver_tabuleiro_fantasma(jogador: str):
    # Adicione lógica para verificar se o jogador está em uma partida
    if jogador not in partida.fila_jogadores:
        raise HTTPException(status_code=400, detail=f"{jogador} não está em uma partida.")

    # Adicione mais lógica conforme necessário
    tabuleiro_fantasma = partida.obter_tabuleiro_fantasma(jogador)
    
    return {"tabuleiro_fantasma": tabuleiro_fantasma}

@app.post("/colocar_peca/{jogador}/{nome_peca}/{linha}/{coluna}/{orientacao}")
async def colocar_peca(
    jogador: str, nome_peca: str, linha: int, coluna: int, orientacao: str
):
    try:
        partida.colocar_peca(jogador, nome_peca, linha, coluna, orientacao)
        return {"message": f"{jogador} colocou a peça {nome_peca}."}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.post("/realizar_disparo/{jogador}/{linha}/{coluna}")
async def realizar_disparo(jogador: str, linha: int, coluna: int):
    try:
        partida.realizar_disparo(jogador, linha, coluna)
        return {"message": f"{jogador} realizou um disparo."}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
from fastapi import FastAPI, HTTPException
from src.controller.tabuleirocontroller import TabuleiroController
from src.view.tabuleiroview import TabuleiroView

app = FastAPI()
tabuleiro_controller = TabuleiroController()


@app.post("/colocar_embarcacao/{jogador}/{tipo_embarcacao}/{linha}/{coluna}/{orientacao}")
async def colocar_embarcacao(
    jogador: str, tipo_embarcacao: str, linha: int, coluna: int, orientacao: str
):
    try:
        tabuleiro_controller.colocar_embarcacao(jogador, tipo_embarcacao, linha, coluna, orientacao)
        return {"message": f"Embarcação colocada com sucesso para {jogador}!"}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@app.post("/disparo/{jogador}/{linha}/{coluna}")
async def realizar_disparo(jogador: str, linha: int, coluna: int):
    try:
        mensagem = tabuleiro_controller.disparo(jogador, linha, coluna)
        return {"message": f"{mensagem} para {jogador}!"}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@app.get("/tabuleiro/{jogador}")
async def obter_tabuleiro(jogador: str):
    return {"tabuleiro": TabuleiroView.formatar_tabuleiro(tabuleiro_controller.obter_tabuleiro(jogador))}


@app.get("/tabuleiro_fantasma/{jogador}")
async def obter_tabuleiro_fantasma(jogador: str):
    return {
        "tabuleiro_fantasma": TabuleiroView.formatar_tabuleiro(tabuleiro_controller.obter_tabuleiro_fantasma(jogador)
        )
    }


from src.model.tabuleiro import TabuleiroModel
from src.view.tabuleiro_view import TabuleiroView

class TabuleiroController:
    def __init__(self):
        self.model = TabuleiroModel()
        self.view = TabuleiroView()

    def obter_tabuleiro(self, jogador):
        return self.model.obter_tabuleiro(jogador)
    
    def obter_tabuleiro_fantasma(self, jogador):
        return self.model.obter_tabuleiro_fantasma(jogador)
    
    def colocar_embarcacao(self, jogador, nome_peca, linha, coluna, orientacao):
        self.model.colocar_embarcacao(jogador, nome_peca, linha, coluna, orientacao)

    def disparo(self, jogador, linha, coluna):
        return self.model.disparo(jogador, linha, coluna)
        
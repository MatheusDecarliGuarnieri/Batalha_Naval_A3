from src.model.tabuleiro import TabuleiroModel
from src.view.tabuleiro_view import TabuleiroView

class TabuleiroController:
    def __init__(self):
        # Instancia o modelo do tabuleiro
        self.model = TabuleiroModel()
        self.view = TabuleiroView()

    def obter_tabuleiro(self, jogador):
        # Obtém o tabuleiro do modelo
        return self.model.obter_tabuleiro(jogador)
    
    def obter_tabuleiro_fantasma(self, jogador):
        # Obtém o tabuleiro fantasma do modelo
        return self.model.obter_tabuleiro_fantasma(jogador)
    
    def colocar_embarcacao(self, jogador, nome_peca, linha, coluna, orientacao):
        # Chama o método correspondente no modelo
        self.model.colocar_embarcacao(jogador, nome_peca, linha, coluna, orientacao)

    def disparo(self, jogador, linha, coluna):
        # Chama o método correspondente no modelo
        return self.model.disparo(jogador, linha, coluna)
        
from typing import List
from src.model.pecas_batalha_naval import PecasBatalhaNaval

class TabuleiroModel:
    def __init__(self):
         # Inicializa os tabuleiros para os jogadores
        self.tabuleiros = {
            'jogador1': [['~']*10 for _ in range(10)],
            'jogador2': [['~']*10 for _ in range(10)]
        }
        # Inicializa os tabuleiros fantasma para os jogadores
        self.tabuleiros_fantasma = {
            'jogador1': [['~']*10 for _ in range(10)],
            'jogador2': [['~']*10 for _ in range(10)]
        }
        # Instancia as peças do jogo
        self.pecas_batalha_naval = PecasBatalhaNaval()

    def colocar_embarcacao(self, jogador, nome_peca, linha, coluna, orientacao):
        # Obtém o tabuleiro do jogador
        tabuleiro = self.tabuleiros[jogador]
        # Obtém a peça correspondente ao nome
        peca = self.pecas_batalha_naval.obter_peca(nome_peca)

        if peca is None:
            raise ValueError(f"Tipo de embarcação '{nome_peca}' não encontrado.")

        if not (0 <= linha < 10 and 0 <= coluna < 10):
            raise ValueError("Coordenadas inválidas.")

        # Chama o método correspondente na classe PecasBatalhaNaval
        if nome_peca == 'PortaAvioes':
            self.pecas_batalha_naval.adicionar_peca_portaavioes(tabuleiro, linha, coluna, orientacao)
        elif nome_peca == 'Encouracado':
            self.pecas_batalha_naval.adicionar_peca_encouracado(tabuleiro, linha, coluna, orientacao)
        elif nome_peca == 'Cruzador':
            self.pecas_batalha_naval.adicionar_peca_cruzador(tabuleiro, linha, coluna, orientacao)
        elif nome_peca == 'Destroier':
            self.pecas_batalha_naval.adicionar_peca_destroier(tabuleiro, linha, coluna, orientacao)
        elif nome_peca == 'Submarino':
            self.pecas_batalha_naval.adicionar_peca_submarino(tabuleiro, linha, coluna)
        else:
            raise ValueError("Tipo de embarcação desconhecido.")
    
    #Lógica para realizar um disparo no tabuleiro
    def disparo(self, jogador, linha, coluna):
        tabuleiro = self.tabuleiros[jogador]
        tabuleiro_fantasma = self.tabuleiros_fantasma[jogador]
        
        # Verifica se as coordenadas são válidas
        if not (0 <= linha < 10 and 0 <= coluna < 10):
            raise ValueError("Coordenadas inválidas.")

        # Verifica se o ataque acertou ou errou
        if tabuleiro[linha][coluna] != '~':
            tipo_embarcacao = tabuleiro[linha][coluna]
            tabuleiro_fantasma[linha][coluna] = 'X'  # Marcando o ataque bem-sucedido no tabuleiro fantasma
            mensagem = f"Acertou o navio {tipo_embarcacao}!"
        else:
            tabuleiro_fantasma[linha][coluna] = 'O'  # Marcando a água no tabuleiro fantasma
            mensagem = "Água!"
        return mensagem

    #   Retorna Tabuleiro
    def obter_tabuleiro(self, jogador) -> List[List[str]]:
        return self.tabuleiros[jogador]
    
    #   Retorna Tabuleiro_Fantasma
    def obter_tabuleiro_fantasma(self, jogador) -> List[List[str]]:
        return self.tabuleiros_fantasma[jogador]
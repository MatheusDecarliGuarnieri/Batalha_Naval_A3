from typing import List
from src.model.pecas_batalha_naval import PecasBatalhaNaval

class TabuleiroModel():
    def __init__(self):
        self.tabuleiros = {
            'jogador1': [['~']*10 for _ in range(10)],
            'jogador2': [['~']*10 for _ in range(10)]
        }
        self.tabuleiros_fantasma = {
            'jogador1': [['~']*10 for _ in range(10)],
            'jogador2': [['~']*10 for _ in range(10)]
        }
        self.pecas_batalha_naval = PecasBatalhaNaval()

    def colocar_embarcacao(self, jogador, nome_peca, linha, coluna, orientacao):
        tabuleiro = self.tabuleiros[jogador]
        peca = self.pecas_batalha_naval.obter_peca(nome_peca)

        if peca is None:
            raise ValueError(f"Tipo de embarcação '{nome_peca}' não encontrado.")

        if not (0 <= linha < 10 and 0 <= coluna < 10):
            raise ValueError("Coordenadas inválidas.")
           
        for i in range(len(peca)):
            if nome_peca == 'PortaAvioes' and orientacao == 'horizontal':
                # Adiciona a peça 'P' em formato de T para 'PortaAvioes'
                tabuleiro[linha][coluna] = 'P1'
                tabuleiro[linha][coluna + 1] = 'P2'
                tabuleiro[linha ][coluna - 1] = 'P3'
                tabuleiro[linha + 1][coluna] = 'P4'
                tabuleiro[linha + 2][coluna] = 'P5'
            else:
                if orientacao == 'horizontal':
                    if coluna + i >= 10 or tabuleiro[linha][coluna + i] != '~':
                        raise ValueError("Posição ocupada por outro navio.")
                    tabuleiro[linha][coluna + i] = peca[i]
                                               
            if nome_peca == 'PortaAvioes' and orientacao == 'vertical':
                tabuleiro[linha][coluna] = 'P1'
                tabuleiro[linha - 1][coluna] = 'P2'
                tabuleiro[linha + 1][coluna] = 'P3'
                tabuleiro[linha][coluna + 1] = 'P4'
                tabuleiro[linha][coluna + 2] = 'P5'
            else:    
                if orientacao == 'vertical':
                    if linha + i >= 10 or tabuleiro[linha + i][coluna] != '~':
                        raise ValueError("Posição ocupada por outro navio.")
                    tabuleiro[linha + i][coluna] = peca[i]
                else:
                    raise ValueError("Orientação inválida.")

    # def verifica_posicao(self, linha, coluna):
    #     # Verifica se a posição está ocupada por uma peça
    #     return self.tabuleiro[linha][coluna] != '~'

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
        
    def obter_tabuleiro(self, jogador) -> List[List[str]]:
        return self.tabuleiros[jogador]

    def obter_tabuleiro_fantasma(self, jogador) -> List[List[str]]:
        return self.tabuleiros_fantasma[jogador]
        
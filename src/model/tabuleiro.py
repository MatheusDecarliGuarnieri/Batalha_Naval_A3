from typing import List
import json

class TabuleiroModel:
    def __init__(self):
        self.tabuleiros = {
            'jogador1': [['~']*10 for _ in range(10)],
            'jogador2': [['~']*10 for _ in range(10)]
        }
        self.tabuleiros_fantasma = {
            'jogador1': [['~']*10 for _ in range(10)],
            'jogador2': [['~']*10 for _ in range(10)]
        }
        self.embarcacao = {'A': 5, 'B': 4, 'S': 3, 'D': 3, 'P': 2}
    
    def colocar_embarcacao(self, jogador, tipo_embarcacao, linha, coluna, orientacao):
        tabuleiro = self.tabuleiros[jogador]

        if not (0 <= linha < 10 and 0 <= coluna < 10):
            raise ValueError("Coordenadas inválidas.")
        
        for i in range(self.embarcacao[tipo_embarcacao]):
            if orientacao == 'horizontal':
                if coluna + i >= 10 or tabuleiro[linha][coluna + i] != '~':
                    raise ValueError("Posição ocupada por outro navio.")
                tabuleiro[linha][coluna + i] = tipo_embarcacao
            elif orientacao == 'vertical':
                if linha + i >= 10 or tabuleiro[linha + i][coluna] != '~':
                    raise ValueError("Posição ocupada por outro navio.")
                tabuleiro[linha + i][coluna] = tipo_embarcacao
            else:
                raise ValueError("Orientação inválida.")

    def verifica_posicao(self, linha, coluna):
        # Verifica se a posição está ocupada por uma peça
        return self.tabuleiro[linha][coluna] != '~'

    def disparo(self, jogador, linha, coluna):
        tabuleiro = self.tabuleiros[jogador]
        tabuleiro_fantasma = self.tabuleiros_fantasma[jogador]
        
        # Verifica se as coordenadas são válidas
        if not (0 <= linha < 10 and 0 <= coluna < 10):
            raise ValueError("Coordenadas inválidas.")

        # Verifica se o ataque acertou ou errou
        if tabuleiro[linha][coluna] != ' ':
            tipo_embarcacao = tabuleiro[linha][coluna]
            tabuleiro_fantasma[linha][coluna] = 'X'  # Marcando o ataque bem-sucedido no tabuleiro fantasma
            return f"Acertou o navio {tipo_embarcacao}!"
        else:
            tabuleiro_fantasma[linha][coluna] = 'O'  # Marcando a água no tabuleiro fantasma
            return "Água!"
        
    def obter_tabuleiro(self, jogador) -> List[List[str]]:
        return self.tabuleiros[jogador]

    def obter_tabuleiro_fantasma(self, jogador) -> List[List[str]]:
        return self.tabuleiros_fantasma[jogador]

class TabuleiroView:
    @staticmethod
    def formatar_tabuleiro(tabuleiro: List[List[str]]) -> List[str]:
        formatted_tabuleiro = [' '.join(linha) for linha in tabuleiro]
        return formatted_tabuleiro
        
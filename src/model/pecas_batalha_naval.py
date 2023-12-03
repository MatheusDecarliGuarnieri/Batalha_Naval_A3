class PecasBatalhaNaval:
    def __init__(self):
        self.tipos_embarcacoes = {
            'Submarino': ['S1'] ,
            'Destroier': ['D1', 'D2'] ,
            'Cruzador': ['C1', 'C2', 'C3'],
            'Encouracado': ['E1', 'E2', 'E3', 'E4'],
            'PortaAvioes': ['P1', 'P2', 'P3', 'P4', 'P5']
        }

    def obter_peca(self, nome_peca):
        return self.tipos_embarcacoes.get(nome_peca, None)

    def adicionar_peca_portaavioes(self, tabuleiro, linha, coluna):
        # Verifica se a posição está dentro dos limites do tabuleiro
        if 0 <= linha < len(tabuleiro) and 0 <= coluna < len(tabuleiro[0]):
            # Adiciona a peça 'P' em formato de T
            tabuleiro[linha][coluna] = 'P1'
            tabuleiro[linha + 1][coluna] = 'P2'
            tabuleiro[linha + 2][coluna] = 'P3'
            tabuleiro[linha + 1][coluna + 1] = 'P4'
            tabuleiro[linha + 1][coluna + 2] = 'P5'


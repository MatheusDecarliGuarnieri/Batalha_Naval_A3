class PecasBatalhaNaval:
    def __init__(self):
        # Dicionário de tipos de embarcações e suas representações
        self.tipos_embarcacoes = {
            'Submarino': ['S'] ,
            'Destroier': ['D1', 'D2'] ,
            'Cruzador': ['C1', 'C2', 'C3'],
            'Encouracado': ['E1', 'E2', 'E3', 'E4'],
            'PortaAvioes': ['P1', 'P2', 'P3', 'P4', 'P5']
        }
        # Contadores de peças colocadas e limite máximo de peças
        self.pecas_colocadas = 0
        self.max_pecas = 8

    def obter_peca(self, nome_peca):
        # Obtém a representação da peça pelo nome
        return self.tipos_embarcacoes.get(nome_peca, None)
    
    # Adicione métodos para adicionar cada tipo de embarcação
    def adicionar_peca_portaavioes(self, tabuleiro, linha, coluna, orientacao):
        if self.pecas_colocadas >= self.max_pecas:
            print("Limite máximo de peças atingido.")
            return
        
        if orientacao == 'horizontal':
            for i in range(3):
                if coluna + i >= 10 or tabuleiro[linha][coluna + i] != '~':
                    raise ValueError("Posição ocupada por outro navio.")
                if not (0 <= linha < len(tabuleiro) and 0 <= coluna < len(tabuleiro[0])):
                    raise ValueError("Fora do Tabuleiro.")
                else:
                    tabuleiro[linha][coluna] = 'P1'
                    tabuleiro[linha + 1][coluna] = 'P2'
                    tabuleiro[linha + 2][coluna] = 'P3'
                    tabuleiro[linha + 1][coluna + 1] = 'P4'
                    tabuleiro[linha + 1][coluna + 2] = 'P5'
                self.pecas_colocadas += 1
                print(f"Peca PortaAvioes adicionada. Total de peças: {self.pecas_colocadas}")
                break
        
        elif orientacao == 'vertical':
            for i in range(3):
                if linha + i >= 10 or tabuleiro[linha + i][coluna] != '~':
                    raise ValueError("Posição ocupada por outro navio.")
                if not (0 <= linha < len(tabuleiro) and 0 <= coluna < len(tabuleiro[0])):
                    raise ValueError("Fora do Tabuleiro.")
                else:
                    tabuleiro[linha][coluna] = 'P1'
                    tabuleiro[linha][coluna + 1] = 'P2'
                    tabuleiro[linha][coluna + 2] = 'P3'
                    tabuleiro[linha + 1][coluna + 1] = 'P4'
                    tabuleiro[linha + 2][coluna + 1] = 'P5'
                self.pecas_colocadas += 1
                print(f"Peca PortaAvioes adicionada. Total de peças: {self.pecas_colocadas}")
                break
        else:
            raise ValueError("Orientação inválida.")

    def adicionar_peca_encouracado(self, tabuleiro, linha, coluna, orientacao):
        if self.pecas_colocadas >= self.max_pecas:
            print("Limite máximo de peças atingido.")
            return

        if not (0 <= linha < len(tabuleiro) and 0 <= coluna < len(tabuleiro[0])):
            raise ValueError("Fora do Tabuleiro.")

        if orientacao == 'horizontal':
            for i in range(4):
                if coluna + i >= 10 or tabuleiro[linha][coluna + i] != '~':
                    raise ValueError("Posição ocupada por outro navio.")
            for i in range(4):
                tabuleiro[linha][coluna + i] = f'E{i+1}'
            self.pecas_colocadas += 1
            print(f"Peca Encouracado adicionada. Total de peças: {self.pecas_colocadas}")

        elif orientacao == 'vertical':
            for i in range(4):
                if linha + i >= 10 or tabuleiro[linha + i][coluna] != '~':
                    raise ValueError("Posição ocupada por outro navio.")
                else:
                    tabuleiro[linha + i][coluna] = f'E{i+1}'
            self.pecas_colocadas += 1
            print(f"Peca Encouracado adicionada. Total de peças: {self.pecas_colocadas}")
        else:
            raise ValueError("Orientação inválida.")
        
    def adicionar_peca_cruzador(self, tabuleiro, linha, coluna, orientacao):
        if self.pecas_colocadas >= self.max_pecas:
            print("Limite máximo de peças atingido.")
            return
        
        if orientacao == 'horizontal':
            for i in range(3):
                if coluna + i >= 10 or tabuleiro[linha][coluna + i] != '~':
                    raise ValueError("Posição ocupada por outro navio.")
                if not (0 <= linha < len(tabuleiro) and 0 <= coluna < len(tabuleiro[0])):
                    raise ValueError("Fora do Tabuleiro.")
                else:
                    tabuleiro[linha][coluna + i] = f'C{i+1}'
                self.pecas_colocadas += 1
                print(f"Peca Cruzador adicionada. Total de peças: {self.pecas_colocadas}")
                break
        elif orientacao == 'vertical':
            for i in range(3):
                if linha + i >= 10 or tabuleiro[linha + i][coluna] != '~':
                    raise ValueError("Posição ocupada por outro navio.")
                if not (0 <= linha < len(tabuleiro) and 0 <= coluna < len(tabuleiro[0])):
                    raise ValueError("Fora do Tabuleiro.")
                else:
                    tabuleiro[linha + i][coluna] = f'C{i+1}'
                self.pecas_colocadas += 1
                print(f"Peca Cruzador adicionada. Total de peças: {self.pecas_colocadas}")
                break
        else:
            raise ValueError("Orientação inválida.")

    def adicionar_peca_destroier(self, tabuleiro, linha, coluna, orientacao):
        if self.pecas_colocadas >= self.max_pecas:
            print("Limite máximo de peças atingido.")
            return
        
        if not (0 <= linha < len(tabuleiro) and 0 <= coluna < len(tabuleiro[0])):
            raise ValueError("Fora do Tabuleiro.")
        
        if orientacao == 'horizontal':
            for i in range(2):
                if coluna + i >= 10 or tabuleiro[linha][coluna + i] != '~':
                    raise ValueError("Posição ocupada por outro navio.")
                for i in range(2):
                    tabuleiro[linha][coluna + i] = f'D{i+1}'
                self.pecas_colocadas += 1
                print(f"Peca Destroier adicionada. Total de peças: {self.pecas_colocadas}")
                break
        elif orientacao == 'vertical':
            for i in range(2):
                if linha + i >= 10 or tabuleiro[linha + i][coluna] != '~':
                    raise ValueError("Posição ocupada por outro navio.")
                for i in range(2):
                    tabuleiro[linha + i][coluna] = f'D{i+1}'
                self.pecas_colocadas += 1
                print(f"Peca Destroier adicionada.")
                    
        else:
            raise ValueError("Orientação inválida.")
        
    def adicionar_peca_submarino(self, tabuleiro, linha, coluna, orientacao):
        if self.pecas_colocadas >= self.max_pecas:
            print("Limite máximo de peças atingido.")
            return
        
        if not (0 <= linha < len(tabuleiro) and 0 <= coluna < len(tabuleiro[0])):
            raise ValueError("Fora do Tabuleiro.")

        for i in range(1):
            if coluna + i >= 10 or tabuleiro[linha][coluna + i] != '~':
                raise ValueError("Posição ocupada por outro navio.")
            else:
                tabuleiro[linha][coluna + i] = f'S'
            self.pecas_colocadas += 1
            print(f"Peca Submarino adicionada. Total de peças: {self.pecas_colocadas}")
            break

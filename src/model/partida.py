from typing import List, Tuple
from fastapi import HTTPException
from src.controller.tabuleiro_controller import TabuleiroController
from src.view.tabuleiro_view import TabuleiroView

class Partida:
    def __init__(self):
        self.fila_jogadores = []  # Fila para controlar a entrada de jogadores
        self.jogadores_na_partida = set()  # Conjunto para controlar os jogadores na partida
        self.tabuleiros = {}  # Dicionário para armazenar os tabuleiros dos jogadores
        self.partida_formada = False  # Atributo para rastrear se a partida foi formada

    def entrar_na_fila(self, jogador):
        self.fila_jogadores.append(jogador)
        self.formar_partida()  # Verificar se a condição para formar a partida é atendida sempre que um jogador entra na fila

    def formar_partida(self):
        if len(self.fila_jogadores) >= 2:
            # Remova dois jogadores da fila e adicione à partida
            jogador1 = self.fila_jogadores.pop(0)
            jogador2 = self.fila_jogadores.pop(0)

            # Adicione os jogadores ao conjunto de jogadores na partida
            self.jogadores_na_partida.add(jogador1)
            self.jogadores_na_partida.add(jogador2)

            # Inicialize os tabuleiros para os jogadores
            self.tabuleiros[jogador1] = [['~']*10 for _ in range(10)]
            self.tabuleiros[jogador2] = [['~']*10 for _ in range(10)]

            self.partida_formada = True
            print(f"A partida foi formada entre {jogador1} e {jogador2}.")

    def verificar_partida(self, jogador):
        if jogador not in self.fila_jogadores and jogador not in self.jogadores_na_partida:
            return {"message": f"{jogador} não está em uma partida.", "partida_formada": self.partida_formada}
        elif jogador in self.fila_jogadores:
            return {"message": f"{jogador}, aguarde a formação da partida.", "partida_formada": self.partida_formada}
        else:
            return {"message": f"{jogador}, a partida foi formada.", "partida_formada": self.partida_formada}

    def obter_tabuleiro(self, jogador):
        return self.tabuleiros.get(jogador, None)

    def colocar_peca(self, jogador, nome_peca, linha, coluna, orientacao):
        partida_atual = self.obter_partida_jogador(jogador)

        if jogador != partida_atual['jogador_atual']:
            raise ValueError("Não é a vez do jogador.")

        tabuleiro = partida_atual[jogador]['tabuleiro']
        self.validar_coordenadas(linha, coluna)

        super().colocar_embarcacao(jogador, nome_peca, linha, coluna, orientacao)
        partida_atual[jogador]['pecas_colocadas'] += 1

        if partida_atual[jogador]['pecas_colocadas'] == 8:
            proximo_jogador = jogador if jogador != partida_atual['jogador_atual'] else self.obter_outro_jogador(jogador)
            partida_atual['jogador_atual'] = proximo_jogador
            print(f"{jogador} colocou todas as peças. Agora é a vez de {proximo_jogador}.")

    def realizar_disparo(self, jogador, linha, coluna):
        partida_atual = self.obter_partida_jogador(jogador)

        if jogador != partida_atual['jogador_atual']:
            raise ValueError("Não é a vez do jogador.")

        tabuleiro = partida_atual[jogador]['tabuleiro']
        self.validar_coordenadas(linha, coluna)

        try:
            super().disparo(jogador, linha, coluna)
        except HTTPException as e:
            raise HTTPException(status_code=e.status_code, detail=str(e))

        if "Acertou" not in mensagem:
            proximo_jogador = self.obter_outro_jogador(jogador)
            partida_atual['jogador_atual'] = proximo_jogador
            print(f"Agora é a vez de {proximo_jogador}.")

    def validar_coordenadas(self, linha, coluna):
        if not (0 <= linha < 10 and 0 <= coluna < 10):
            raise ValueError("Coordenadas inválidas.")

    def obter_outro_jogador(self, jogador):
        partida_atual = self.obter_partida_jogador(jogador)
        jogadores_partida = [j for j in partida_atual.keys() if j != 'jogador_atual']
        return jogadores_partida[0]
from typing import List, Tuple
from src.controller.tabuleiro_controller import TabuleiroController
from src.view.tabuleiro_view import TabuleiroView

class Partida:
    def __init__(self):
        self.fila_jogadores = []  # Fila para controlar a entrada de jogadores
        self.jogadores_na_partida = set()  # Conjunto para controlar os jogadores na partida
        self.tabuleiros = {}
        self.tabuleiros_fantasma = {}  # Dicionário para armazenar os tabuleiros dos jogadores
        self.partida_formada = False  # Atributo para rastrear se a partida foi formada
        self.tabuleiro_controller = TabuleiroController()
        self.tabuleiro_view = TabuleiroView()  # Instanciar o TabuleiroController
        self.embarcacoes_colocadas = {jogador: 0 for jogador in ["jogador1", "jogador2"]}  # Rastrear número de embarcações colocadas
        self.turno_atual = "jogador1"

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

            # Inicialize os tabuleiros_fantasma para os jogadores
            self.tabuleiros_fantasma[jogador1] = [['~']*10 for _ in range(10)]
            self.tabuleiros_fantasma[jogador2] = [['~']*10 for _ in range(10)]

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
        # Verifica se o jogador está na partida
        if jogador not in self.jogadores_na_partida:
            return None  # Se o jogador não estiver na partida, retorna None

        return self.tabuleiros.get(jogador, None)
    
    def obter_tabuleiro_fantasma(self, jogador):
        # Verifica se o jogador está na partida
        if jogador not in self.jogadores_na_partida:
            return None  # Se o jogador não estiver na partida, retorna None

        return self.tabuleiros.get(jogador, None)

    def colocar_embarcacao(self, jogador, nome_peca, linha, coluna, orientacao):
        if jogador not in self.jogadores_na_partida:
            print(f"{jogador} não está na partida.")
            return

        if self.embarcacoes_colocadas[jogador] >= 8:
            print(f"{jogador} já colocou todas as 8 embarcações.")
            return
        
         # Obter o tabuleiro do jogador diretamente
        tabuleiro_do_jogador = self.tabuleiros[jogador]

        # Utilizar o método do TabuleiroController
        self.tabuleiro_controller.colocar_embarcacao(tabuleiro_do_jogador, nome_peca, linha, coluna, orientacao)

        # Atualizar o tabuleiro com a peça escolhida
        tabuleiro = self.tabuleiro_controller.obter_tabuleiro(jogador)
        formatted_tabuleiro = self.tabuleiro_view.formatar_tabuleiro(tabuleiro)
        print(f"Tabuleiro atualizado para {jogador}:\n{formatted_tabuleiro}")

        self.embarcacoes_colocadas[jogador] += 1
        print(f"{jogador} colocou {self.embarcacoes_colocadas[jogador]}/8 embarcações.")

        # Se ambos jogadores colocaram 8 embarcações, inicie o turno
        if all(embarcacoes == 8 for embarcacoes in self.embarcacoes_colocadas.values()):
            self.iniciar_turno()

    def iniciar_turno(self):
        print("Ambos jogadores colocaram 8 embarcações. O turno está iniciando.")
        
        while not self.verificar_fim_partida():
            jogador = self.turno_atual
            print(f"\nTurno de {jogador}.")

            # Mostrar o tabuleiro do jogador atual
            print(f"Tabuleiro de {jogador}:")
            self.mostrar_tabuleiro(jogador)

            # Adicione lógica adicional para interação com os jogadores, como realizar disparos
            linha = int(input(f"{jogador}, informe a linha do disparo: "))
            coluna = int(input(f"{jogador}, informe a coluna do disparo: "))

            # Realizar disparo
            mensagem = self.realizar_disparo(jogador, linha, coluna)
            print(mensagem)

            # Trocar o turno
            self.turno_atual = "jogador2" if jogador == "jogador1" else "jogador1"

    def realizar_disparo(self, jogador, linha, coluna):
        if jogador not in self.jogadores_na_partida:
            print(f"{jogador} não está na partida.")
            return "Jogador não está na partida."

        if jogador != self.turno_atual:
            print(f"Ainda não é o turno de {jogador}.")
            return "Ainda não é o seu turno."

        # Utilizar o método do TabuleiroController
        mensagem = self.tabuleiro_controller.disparo(self.tabuleiros[jogador], linha, coluna)

        # Adicione lógica adicional conforme necessário
        # Por exemplo, verificar se o disparo acertou todas as peças do oponente para encerrar a partida

        # Trocar o turno
        self.turno_atual = "jogador2" if jogador == "jogador1" else "jogador1"

        return mensagem

    def obter_outro_jogador(self, jogador):
        partida_atual = self.obter_partida_jogador(jogador)
        jogadores_partida = [j for j in partida_atual.keys() if j != 'jogador_atual']
        return jogadores_partida[0]
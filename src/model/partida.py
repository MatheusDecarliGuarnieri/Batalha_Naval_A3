from src.model.tabuleiro import TabuleiroModel
from src.view.tabuleiroview import TabuleiroView


class Partida(TabuleiroModel):
    _id: int
    _tabuleiro: TabuleiroModel()
    _contador_id = 0

    def __init__(self, jogador1, jogador2):
        self._jogador1 = jogador1
        self._jogador2 = jogador2

    @classmethod
    def get_novo_id(cls):
        cls._contador_id = cls._contador_id + 1
        return cls._contador_id

    @classmethod
    def comecar_partida(jogador1, tabuleiro):
        pass
        
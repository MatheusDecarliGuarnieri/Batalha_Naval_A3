from typing import List

class TabuleiroView:
    @staticmethod
    def formatar_tabuleiro(tabuleiro: List[List[str]]) -> List[str]:
        formatted_tabuleiro = [' '.join(linha) for linha in tabuleiro]
        return formatted_tabuleiro
from typing import List

class TabuleiroView:

    @staticmethod
    def formatar_tabuleiro(tabuleiro: List[List[str]]) -> List[str]:
        formatted_tabuleiro = []

        for linha in tabuleiro:
            formatted_linha = []
            for item in linha:
                if isinstance(item, list):
                    # Se o item for uma lista, unimos seus elementos em uma string
                    formatted_linha.append(' '.join(item))
                else:
                    formatted_linha.append(item)
            formatted_tabuleiro.append(' '.join(formatted_linha))

        return formatted_tabuleiro
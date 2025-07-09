from random import shuffle
from jogador import Jogador
from tabuleiro import Tabuleiro

class JogadorIA(Jogador):
    def __init__(self, tabuleiro: Tabuleiro, tipo: int):
        super().__init__(tabuleiro, tipo)

    def getJogada(self) -> (int, int):  # type: ignore
        matriz = self.tabuleiro.matriz
        IA = Tabuleiro.JOGADOR_X
        HUMANO = Tabuleiro.JOGADOR_0
        VAZIO = Tabuleiro.DESCONHECIDO

        def sequencia_vazia(jogador):
            adversario = Tabuleiro.JOGADOR_0 if jogador == Tabuleiro.JOGADOR_X else Tabuleiro.JOGADOR_X

            for l in range(3):
                linha = matriz[l]
                if linha.count(jogador) == 2 and linha.count(Tabuleiro.DESCONHECIDO) == 1:
                    if adversario not in linha:
                        for c in range(3):
                            if matriz[l][c] == Tabuleiro.DESCONHECIDO:
                                return (l, c)
            for c in range(3):
                col = [matriz[r][c] for r in range(3)]
                if col.count(jogador) == 2 and col.count(Tabuleiro.DESCONHECIDO) == 1:
                    if adversario not in col:
                        for r in range(3):
                            if matriz[r][c] == Tabuleiro.DESCONHECIDO:
                                return (r, c)

            diag1 = [matriz[i][i] for i in range(3)]
            if diag1.count(jogador) == 2 and diag1.count(Tabuleiro.DESCONHECIDO) == 1:
                if adversario not in diag1:
                    for i in range(3):
                        if matriz[i][i] == Tabuleiro.DESCONHECIDO:
                            return (i, i)
            diag2 = [matriz[i][2 - i] for i in range(3)]
            if diag2.count(jogador) == 2 and diag2.count(Tabuleiro.DESCONHECIDO) == 1:
                if adversario not in diag2:
                    for i in range(3):
                        if matriz[i][2 - i] == Tabuleiro.DESCONHECIDO:
                            return (i, 2 - i)

            return None
        # R1
        jogada = sequencia_vazia(IA)
        if jogada:
            return jogada

        # R2
        jogada = sequencia_vazia(HUMANO)
        if jogada:
            return jogada

        # R2 
        def cria_dupla():
            for l in range(3):
                for c in range(3):
                    if matriz[l][c] == VAZIO:
                        matriz[l][c] = IA
                        ameacas = 0
                        if sequencia_vazia(IA):
                            ameacas += 1
                        matriz[l][c] = VAZIO
                        if ameacas >= 2:
                            return (l, c)
            return None

        jogada = cria_dupla()
        if jogada:
            return jogada

        # R3
        if matriz[1][1] == VAZIO:
            return (1, 1)
        
        
        # R4
        cantos = [(0, 0), (0, 2), (2, 0), (2, 2)]
        opostos = {
            (0, 0): (2, 2),
            (0, 2): (2, 0),
            (2, 0): (0, 2),
            (2, 2): (0, 0)
        }
        for l, c in cantos:
            if matriz[l][c] == HUMANO:
                l_op, c_op = opostos[(l, c)]
                if matriz[l_op][c_op] == VAZIO:
                    return (l_op, c_op)


        # R5
        shuffle(cantos)
        for l, c in cantos:
            if matriz[l][c] == VAZIO:
                return (l, c)

        # R6
        livres = [(l, c) for l in range(3) for c in range(3) if matriz[l][c] == VAZIO]
        if livres:
            shuffle(livres)
            return livres[0]

        return None

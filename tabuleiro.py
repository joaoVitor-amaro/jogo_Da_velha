class Tabuleiro:
    DESCONHECIDO = 0
    JOGADOR_0 = 1
    JOGADOR_X = 4

    def __init__(self):
        self.matriz = [
            [Tabuleiro.DESCONHECIDO, Tabuleiro.DESCONHECIDO, Tabuleiro.DESCONHECIDO],
            [Tabuleiro.DESCONHECIDO, Tabuleiro.DESCONHECIDO, Tabuleiro.DESCONHECIDO],
            [Tabuleiro.DESCONHECIDO, Tabuleiro.DESCONHECIDO, Tabuleiro.DESCONHECIDO]
        ]

    def campeao_linha(self):
        for l in range(3):
            soma = sum(self.matriz[l])
            if soma == 3:
                return Tabuleiro.JOGADOR_0
            elif soma == 12:
                return Tabuleiro.JOGADOR_X
        return Tabuleiro.DESCONHECIDO

    def campeao_coluna(self):
        for c in range(3):
            soma = sum(self.matriz[l][c] for l in range(3))
            if soma == 3:
                return Tabuleiro.JOGADOR_0
            elif soma == 12:
                return Tabuleiro.JOGADOR_X
        return Tabuleiro.DESCONHECIDO

    def campeao_diagonal(self):
        diag1 = self.matriz[0][0] + self.matriz[1][1] + self.matriz[2][2]
        diag2 = self.matriz[0][2] + self.matriz[1][1] + self.matriz[2][0] 

        if diag1 == 3 or diag2 == 3:
            return Tabuleiro.JOGADOR_0
        elif diag1 == 12 or diag2 == 12:
            return Tabuleiro.JOGADOR_X
        return Tabuleiro.DESCONHECIDO

    def tem_campeao(self):
        for checar in [self.campeao_linha, self.campeao_coluna, self.campeao_diagonal]:
            vencedor = checar()
            if vencedor != Tabuleiro.DESCONHECIDO:
                return vencedor
        return Tabuleiro.DESCONHECIDO

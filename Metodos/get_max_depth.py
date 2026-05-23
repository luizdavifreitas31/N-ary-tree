# FUNÇÃO DE PROFUNDIDADE MÁXIMA (get_max_depth)

def get_max_depth(self):

    def profundidade(no):

        if no is None:
            return 0

        maior = 0
        filho = no.filho

        while filho:

            prof = profundidade(filho)

            if prof > maior:
                maior = prof

            filho = filho.irmao

        return maior + 1

    if self.raiz is None:
        return 0

    return profundidade(self.raiz) - 1

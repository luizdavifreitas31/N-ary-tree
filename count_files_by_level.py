def count_files_by_level(self):

    niveis = {}

    def contar(no, nivel):

        if no is None:
            return

        if nivel not in niveis:
            niveis[nivel] = 0

        niveis[nivel] += 1

        filho = no.prim_filho

        while filho:
            contar(filho, nivel + 1)
            filho = filho.irmao

    if self.raiz is None:
        return {}

    filho = self.raiz.prim_filho

    while filho:
        contar(filho, 1)
        filho = filho.irmao

    return niveis
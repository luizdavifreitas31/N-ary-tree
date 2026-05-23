# FUNÇÃO DE CONTAGEM POR NÍVEL (count_files_by_level)

def count_files_by_level(self):
    niveis = {}

    def contar(no, nivel):
        if no is None:
            return

        if no.is_file:
            if nivel not in niveis:
                niveis[nivel] = 0
            niveis[nivel] += 1

        filho = no.filho
        while filho:
            contar(filho, nivel + 1)
            filho = filho.irmao

    contar(self.raiz, 0)
    return niveis

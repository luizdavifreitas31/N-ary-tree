# FUNÇÃO DE EXISTÊNCIA (file_exists)

def file_exists(self, path):
    partes = [p for p in path.split('/') if p]

    if not partes:
        return True

    atual = self.raiz

    for parte in partes:
        filho_atual = atual.filho
        encontrou_neste_nivel = False

        while filho_atual is not None:
            if filho_atual.valor == parte:
                encontrou_neste_nivel = True
                atual = filho_atual
                break

            filho_atual = filho_atual.irmao

        if not encontrou_neste_nivel:
            return False

    return True

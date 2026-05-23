def get_directory_contents(self, caminho):
    partes = [p for p in caminho.split('/') if p]
    atual = self.raiz

    for parte in partes:
        filho_atual = atual.filho
        encontrou = False

        while filho_atual is not None:

            if filho_atual.valor == parte:
                encontrou = True
                atual = filho_atual
                break

            filho_atual = filho_atual.irmao

        if not encontrou:
            return None

    if atual.is_file:
        return None

    lista = []
    filho = atual.filho

    while filho:
        lista.append(filho.valor)
        filho = filho.irmao

    return lista

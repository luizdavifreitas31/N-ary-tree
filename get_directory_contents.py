def get_directory_contents(self, caminho):
    diretorio = self.busca(self.raiz, caminho)

    if diretorio is None:
        return None
        
    lista = []
    atual = diretorio.filho

    while atual:
        lista.append(atual.valor)
        atual = atual.irmao

    return lista

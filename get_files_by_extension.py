# Função auxiliar
def percorrer(self, no_atual, ext, caminho, resultado):
    if no_atual is None:
        return
    
    novo_caminho = caminho+"/"+no_atual.valor

    if no_atual.valor.endswith(ext):
        resultado.append(novo_caminho)

    filho = no_atual.filho

    while filho:
        self.percorrer(
            self.raiz,
            ext,
            "",
            resultado
        )
        return resultado


# Função Principal    
def get_files_by_extension(self, ext):
    resultado = []

    self.percorrer(
        self.raiz,
        ext,
        "",
        resultado
    )

    return resultado

# FUNÇÃO DE BUSCA POR EXTENSÃO (get_files_by_extension)

def get_files_by_extension(self, ext):
    resultado = []

    def dfs(node, path_atual):
        if node is None:
            return

        if node.valor == "/":
            caminho = ""

        else:
            caminho = path_atual + "/" + node.valor

        if node.is_file and node.valor.endswith(ext):
            resultado.append(caminho)

        filho = node.filho

        while filho:
            dfs(filho, caminho)
            filho = filho.irmao

    dfs(self.raiz, "")
    return resultado

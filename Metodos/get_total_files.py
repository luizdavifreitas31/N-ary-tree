# FUNÇÃO DE CONTAGEM TOTAL (get_total_files)

def get_total_files(self) -> int:
    def contar(node):
        if node is None:
            return 0
        total = 1 if node.is_file else 0
        total += contar(node.filho)
        total += contar(node.irmao)
        return total
    return contar(self.raiz)

"""
Funções: get_total_files() e is_valid()
"""
def get_total_files(raiz) -> int:
    """
    Retorna o total de arquivos (nós com is_file=True) na árvore.
    """
    def contar(node):
        if node is None:
            return 0

        # Conta 1 se esse nó for arquivo, 0 se for diretório
        total = 1 if node.is_file else 0

        # Desce para o primeiro filho (próximo nível da árvore)
        total += contar(node.filho)

        # Avança para o próximo irmão (mesmo nível da árvore)
        total += contar(node.irmao)

        return total

    return contar(raiz)


def is_valid(raiz) -> bool:
    """
    Valida se a estrutura da árvore está correta.
    """
    def verificar(node, pai_esperado):
        if node is None:
            return True

        # Verificação 1: o ponteiro pai está correto?
        if node.pai != pai_esperado:
            return False

        # Verificação 2: há irmãos com valor duplicado?
        # Percorre todos os irmãos do nível atual e guarda os valores vistos
        vistos = set()
        irmao_atual = node
        while irmao_atual is not None:
            if irmao_atual.valor in vistos:
                return False          # Duplicata encontrada
            vistos.add(irmao_atual.valor)
            irmao_atual = irmao_atual.irmao

        # Desce para os filhos (passando o nó atual como pai esperado)
        if not verificar(node.filho, node):
            return False

        # Avança para o próximo irmão (mantendo o mesmo pai esperado)
        if not verificar(node.irmao, pai_esperado):
            return False

        return True

    return verificar(raiz, None)

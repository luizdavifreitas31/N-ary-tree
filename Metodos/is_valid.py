# FUNÇÃO DE VALIDAÇÃO (is_valid)

def is_valid(self) -> bool:
    def verificar(node, pai_esperado):

        if node is None:
            return True

        if node.pai != pai_esperado:
            return False

        vistos = set()
        irmao_atual = node

        while irmao_atual is not None:

            if irmao_atual.valor in vistos:
                return False

            vistos.add(irmao_atual.valor)
            irmao_atual = irmao_atual.irmao

        if not verificar(node.filho, node):
            return False

        if not verificar(node.irmao, pai_esperado):
            return False

        return True

    return verificar(self.raiz, None)

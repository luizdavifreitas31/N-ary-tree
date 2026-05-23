class no:
    def __init__(self, valor):
        self.valor = valor
        self.filho = None
        self.irmao = None
        self.pai = None
        self.is_file = False


class FileSystemTree:
    def __init__(self):
        self.raiz = no("/")

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

    # FUNÇÃO DE INSERÇÃO (add_file)

    def add_file(self, path):
        partes = [p for p in path.split('/') if p]

        if not partes:
            return False

        atual = self.raiz

        for i, parte in enumerate(partes):
            eh_ultimo = (i == len(partes) - 1)
            filho_atual = atual.filho
            encontrou = False
            ultimo_irmao = None

            while filho_atual is not None:

                if filho_atual.valor == parte:
                    encontrou = True
                    break

                ultimo_irmao = filho_atual
                filho_atual = filho_atual.irmao

            if encontrou:

                if eh_ultimo:
                    return False

                atual = filho_atual

            else:
                novo_no = no(parte)
                novo_no.pai = atual

                if eh_ultimo:
                    novo_no.is_file = True

                if atual.filho is None:
                    atual.filho = novo_no

                else:
                    ultimo_irmao.irmao = novo_no

                atual = novo_no

        return True

    # FUNÇÃO DE LISTAGEM (get_directory_contents)

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

    # FUNÇÃO DE PROFUNDIDADE MÁXIMA (get_max_depth)

    def get_max_depth(self):

        def profundidade(no):

            if no is None:
                return 0

            maior = 0
            filho = no.filho

            while filho:

                prof = profundidade(filho)

                if prof > maior:
                    maior = prof

                filho = filho.irmao

            return maior + 1

        if self.raiz is None:
            return 0

        return profundidade(self.raiz) - 1

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

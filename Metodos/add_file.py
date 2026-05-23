# FUNÇÃO DE INSERÇÃO (add_file)
import no


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

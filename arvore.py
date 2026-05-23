import no


class arvore:
    def __init__(self):
        self.raiz = None

    def busca(self, raiz_pai, chave):
        if raiz_pai == None:
            return None
        if raiz_pai.chave == chave:
            return raiz_pai

        atual = raiz_pai.filho

        while atual:
            resp = self.busca(atual, chave)
            if resp:
                return resp
            atual = atual.irmao

        return None

    def insere(self, raiz, nova_chave, chave_pai):

        pai = self.busca(raiz, chave_pai)
        if pai is None:
            return False

        filho = no.no(nova_chave)

        atual_i = pai.filho

        if atual_i is None:
            pai.filho = filho
        else:
            while atual_i.irmao:
                atual_i = atual_i.irmao
            atual_i.irmao = filho

        return True

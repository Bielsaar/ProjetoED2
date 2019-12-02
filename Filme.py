class Filme:
    def __init__(self, nome=None, ano=None, aid=None):
        self._nome = nome
        self._aid = aid
        self._ano = ano

    def set_nome(self, nome):
        self._nome = nome

    def get_nome(self):
        return self._nome

    def set_aid(self, aid):
        self._aid = aid

    def get_aid(self):
        return self._aid

    def set_ano(self, ano):
        self._ano = ano

    def get_ano(self):
        return self._ano

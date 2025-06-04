"""
Definição de classe
"""


class Livro:
    def __init__(self, titulo, autor, editora):
        self._titulo = titulo
        self._autor = autor
        self._editora = editora

    @property
    def titulo(self):
        return self._titulo

    @titulo.setter
    def titulo(self, novo_titulo):
        if novo_titulo != str:
            raise SyntaxError("Título inválido!")
        self._titulo = novo_titulo
        print("Título alterado com sucesso!")

    @property
    def autor(self):
        return self._autor

    @autor.setter
    def autor(self, novo_autor):
        if novo_autor != str:
            raise SyntaxError("Formato inválido!")
        self._autor = novo_autor
        print("Autor alterado com sucesso!")

    @property
    def editora(self):
        return self._editora

    @editora.setter
    def editora(self, nova_editora):
        if nova_editora != str:
            raise SyntaxError("Formado inválido!")
        self._editora = nova_editora
        print("Editora alterado com sucesso!")

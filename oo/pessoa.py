class Pessoa():
    def __init__(self, nome=None, idade=None):
        self.nome = nome
        self.idade = idade
    def cumprimentar(self):
        return f'Olá {id(self)}'

if __name__ == '__main__':
    p = Pessoa(nome='Diego', idade=33)
    print(p.nome, p.idade)


class Programa :
    def __init__(self, nome, ano) -> None:
        self._nome = nome.title()
        self.ano = ano
        self._likes = 0

    @property
    def likes(self) :
        return self._likes

    def dar_like(self) :
        self._likes += 1

    @property
    def nome(self) :
        return self._nome
    
    @nome.setter
    def nome(self, novo_nome) :
        self._nome = novo_nome.title()

class Filme(Programa) :
    def __init__(self, nome, ano, duracao) -> None:
        super().__init__(nome, ano)
        self.duracao = duracao

class Serie(Programa) :
    def __init__(self, nome, ano, temporadas) -> None:
        super().__init__(nome, ano)
        self.temporadas = temporadas
        

vingadores = Filme("vingadores - guerra infinita", 2018, 160)
vingadores.dar_like()

print(f'{vingadores.nome} - {vingadores.ano} - {vingadores.duracao}: {vingadores.likes}')

atlanta = Serie("atlanta", 2018, 2)
atlanta.dar_like()
atlanta.nome = "atlanta - a terra esquecida"

print(f'{atlanta.nome} - {atlanta.ano} - {atlanta.temporadas}: {atlanta.likes}')

filmes_e_series = [vingadores, atlanta]

for programa in filmes_e_series :
    detalhes = programa.duracao if hasattr(programa, "duracao") else programa.temporadas
    print(f'{programa.nome} - {programa.ano} - {detalhes} : {programa.likes}')

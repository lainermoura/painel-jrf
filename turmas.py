class Turma:
    def __init__(self, numero):
        self.numero = numero

class PrimeiraTurma(Turma):
    def __init__(self):
        super().__init__(1)
        self.presidente = "Juan Rodrigues Penna da Costa"
        self.julgadores = ["Isabella Perez Caldas Schettini", "Leonardo Miranda Filho"]
        self.secretario = "Haroldo de Oliveira Almeira Filho"

class SegundaTurma(Turma):
    def __init__(self):
        super().__init__(2)
        self.presidente = "Cid Augusto Mendes Cunha"
        self.julgadores = ["Marcio Contente Arese", "Daniel Julian Ulieldin"]
        self.secretario = "João Gabriel Costa"

class TerceiraTurma(Turma):
    def __init__(self):
        super().__init__(3)
        self.presidente = "Raphael Saraiva Guingo"
        self.julgadores = ["Francisco da Cunha Ferreira", "Maria Helena Alves Oliveira"]
        self.secretario = "Vitor Ferreira Figueira"

class QuartaTurma(Turma):
    def __init__(self):
        super().__init__(4)
        self.presidente = "Alessandra Silveira Santos da Silva"
        self.julgadores = ["Reginaldo Barreiros de Almeida Filho", "Ian Brandão Ligorio Alves"]
        self.secretario = "Diego de Mendonça dos Santos"

class QuintaTurma(Turma):
    def __init__(self):
        super().__init__(5)
        self.presidente = "Thiago Villela Visconti"
        self.julgadores = ["Alexandre Corrêa Grassi Bissacot", "Thiago Pereira Rodrigues Cerqueira e Castro"]
        self.secretario = "Elias Ramos Verdin"

class SextaTurma(Turma):
    def __init__(self):
        super().__init__(6)
        self.presidente = "Vitor Paulo Marins de Mattos"
        self.julgadores = ["Guilherme Bittencourt da Silva", "Bruno Radamés Madureira"]
        self.secretario = "Cristina Leonor da Silva Leles Mello e Alvim"

class SetimaTurma(Turma):
    def __init__(self):
        super().__init__(7)
        self.presidente = "Fabio Dorigo"
        self.julgadores = ["Renan José Silveira de Moraes", "Márcio Mateus de Macedo"]
        self.secretario = "Diogo Mascarenhas"

class OitavaTurma(Turma):
    def __init__(self):
        super().__init__(8)
        self.presidente = "Vinícius Carlos Ferreira do Fundo"
        self.julgadores = ["Alexandre Salim Saud de Oliveira", "Fábio Hottz Longo"]
        self.secretario = "Fernando Gonçalves Castanheira Júnior"

class NonaTurma(Turma):
    def __init__(self):
        super().__init__(9)
        self.presidente = "Nylfson Rodrigues Borges Nogueira"
        self.julgadores = ["Guilherme Marques Ribeiro", "Átila Dias Conceição"]
        self.secretario = "Larissa Pinho Amaral"

class DecimaTurma(Turma):
    def __init__(self):
        super().__init__(10)
        self.presidente = "Gabriel Franco Pereira"
        self.julgadores = ["Pedro Canabrava Maia", "Camilo Duquesnois Dubois Brito"]
        self.secretario = "Maria Teresa Pereira Alves Mendes"



    def get_presidente(self):
        return self.presidente

    def get_julgadores(self):
        return ', '.join(self.julgadores)

    def get_secretario(self):
        return self.secretario


turmas = {
    1: PrimeiraTurma(),
    2: SegundaTurma(),
    3: TerceiraTurma(),
    4: QuartaTurma(),
    5: QuintaTurma(),
    6: SextaTurma(),
    7: SetimaTurma(),
    8: OitavaTurma(),
    9: NonaTurma(),
    10: DecimaTurma()
}


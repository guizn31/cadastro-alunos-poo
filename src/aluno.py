class Aluno:
    def __init__(self, nome, cpf, data_nascimento, telefone=None):
        self.nome = nome
        self.cpf = cpf
        self.data_nascimento = data_nascimento
        self.telefone = telefone

    def __str__(self):
        return f"Nome: {self.nome}, CPF: {self.cpf}"
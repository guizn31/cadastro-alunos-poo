import sqlite3
from aluno import Aluno

DB_PATH = 'src/alunos.db'

class Crud:
    def __init__(self):
        self.conexao = sqlite3.connect(DB_PATH)
        self.cursor = self.conexao.cursor()

    def __del__(self):
        self.conexao.close()

    def criar_aluno(self, aluno: Aluno):
        self.cursor.execute("INSERT INTO Aluno (nome, cpf, data_nascimento, telefone) VALUES (?, ?, ?, ?)",
            (aluno.nome, aluno.cpf, aluno.data_nascimento, aluno.telefone))
        self.conexao.commit()
        return self.cursor.lastrowid

    def ler_alunos(self):
        self.cursor.execute("SELECT id, nome, cpf, data_nascimento, telefone FROM Aluno")
        alunos_data = self.cursor.fetchall()
        alunos = []
        for data in alunos_data:
            aluno = Aluno(data[1], data[2], data[3], data[4])
            aluno.id = data[0] # Adiciona o ID ao objeto Aluno
            alunos.append(aluno)
        return alunos

    def ler_aluno_por_id(self, aluno_id):
        self.cursor.execute("SELECT id, nome, cpf, data_nascimento, telefone FROM Aluno WHERE id = ?", (aluno_id,))
        data = self.cursor.fetchone()
        if data:
            aluno = Aluno(data[1], data[2], data[3], data[4])
            aluno.id = data[0]
            return aluno
        return None

    def atualizar_aluno(self, aluno_id, aluno: Aluno):
        self.cursor.execute("UPDATE Aluno SET nome = ?, cpf = ?, data_nascimento = ?, telefone = ? WHERE id = ?",
            (aluno.nome, aluno.cpf, aluno.data_nascimento, aluno.telefone, aluno_id))
        
        self.conexao.commit()
        return self.cursor.rowcount > 0

    def deletar_aluno(self, aluno_id):
        self.cursor.execute("DELETE FROM Aluno WHERE id = ?", (aluno_id,))
        self.conexao.commit()
        return self.cursor.rowcount > 0
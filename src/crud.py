import sqlite3
from banco import get_connection  # Conexão com o banco
from aluno import Aluno           # Modelo Aluno

DB_PATH = 'src/alunos.db'

class Crud:

    def create_aluno(aluno):
        sql = """INSERT INTO aluno (nome, cpf, data_nascimento, status)
        VALUES (?,?,?,?)"""
        with get_connection() as conn:
            cur = conn.execute(sql, (aluno.nome, aluno.cpf,
            aluno.data_nascimento, aluno.status))
            return cur.lastrowid
    
    def read_aluno_by_id(id):
        sql = "SELECT * FROM aluno WHERE id = "
        with get_connection() as conn:
            cur = conn.execute(sql, (id,))
            return cur.fetchone() # Retorna None se não encontrar

    def read_alunos():
        sql = "SELECT * FROM aluno ORDER BY id DESC"
        with get_connection() as conn:
            cur = conn.execute(sql)
            return cur.fetchall()
    
    def update_aluno(id, novos_dados):
        sql = "UPDATE aluno SET status = ? WHERE id = ?"
        with get_connection() as conn:
            cur = conn.execute(sql, (novos_dados["status"], id))
            return cur.rowcount > 0 # True se atualizou, False se não encontrou
    
    def delete_aluno(id):
        sql = "DELETE FROM aluno WHERE id = ?"
        with get_connection() as conn:
            cur = conn.execute(sql, (id,))
            return cur.rowcount > 0
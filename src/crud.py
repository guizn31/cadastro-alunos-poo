# crud.py
import sqlite3
from typing import List, Tuple, Dict

DB_FILE = "alunos.db"

def _get_conn():
    return sqlite3.connect(DB_FILE)

def init_db():
    conn = _get_conn()
    cur = conn.cursor()
    cur.execute("""
    CREATE TABLE IF NOT EXISTS aluno (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        cpf TEXT NOT NULL UNIQUE,
        data_nascimento TEXT,
        status TEXT
    )
    """)
    conn.commit()
    conn.close()

class Crud:
    """
    Implementação simples com métodos estáticos para facilitar o uso direto:
    Crud.create_aluno(...)
    Crud.read_alunos()
    Crud.update_aluno(...)
    Crud.delete_aluno(...)
    """
    @staticmethod
    def create_aluno(nome: str, cpf: str, data: str, status: str) -> int:
        conn = _get_conn()
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO aluno (nome, cpf, data_nascimento, status) VALUES (?, ?, ?, ?)",
            (nome, cpf, data, status)
        )
        conn.commit()
        last_id = cur.lastrowid
        conn.close()
        return last_id

    @staticmethod
    def read_alunos() -> List[Tuple]:
        conn = _get_conn()
        cur = conn.cursor()
        cur.execute("SELECT id, nome, cpf, data_nascimento, status FROM aluno")
        rows = cur.fetchall()
        conn.close()
        return rows

    @staticmethod
    def update_aluno(cpf: str, campos: Dict[str, str]) -> int:
        """
        Atualiza campos do aluno identificado pelo CPF.
        campos exemplo: {"status": "Inativo"}
        Retorna número de linhas afetadas.
        """
        if not campos:
            return 0
        set_clause = ", ".join(f"{k}=?" for k in campos.keys())
        params = list(campos.values()) + [cpf]
        conn = _get_conn()
        cur = conn.cursor()
        cur.execute(f"UPDATE aluno SET {set_clause} WHERE cpf = ?", params)
        conn.commit()
        linhas = cur.rowcount
        conn.close()
        return linhas

    @staticmethod
    def delete_aluno(cpf: str) -> int:
        conn = _get_conn()
        cur = conn.cursor()
        cur.execute("DELETE FROM aluno WHERE cpf = ?", (cpf,))
        conn.commit()
        linhas = cur.rowcount
        conn.close()
        return linhas

# Inicializa DB ao importar (garante que a tabela exista)
init_db()

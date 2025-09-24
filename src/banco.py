import sqlite3                    # Driver do SQLite já vem no Python
from pathlib import Path          # Manipula caminhos de arquivos

DB_PATH = 'src/alunos.db'

def get_connection():
    """Abre uma conexão SQLite e liga as chaves estrangeiras."""
    conn = sqlite3.connect(DB_PATH)
    conn.execute("PRAGMA foreign_keys = ON")
    return conn

def criar_tabela_aluno():
    conexao = sqlite3.connect(DB_PATH)
    cursor = conexao.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Aluno (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        cpf TEXT UNIQUE NOT NULL,
        data_nascimento TEXT NOT NULL,
        telefone TEXT
    );
    ''')
    conexao.commit()
    conexao.close()

if __name__ == '__main__':
    criar_tabela_aluno()
    print("-----------------------------------------------------")
    print(f"Banco de dados e tabela 'Aluno' criados em {DB_PATH}")
    print("-----------------------------------------------------")

import sqlite3 

DB_PATH = 'src/alunos.db'

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

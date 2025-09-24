from aluno import Aluno
from crud import Crud

def main():
    print("=== TESTANDO CRUD ===")
    
    # CREATE
    aluno1 = Aluno(nome="João", cpf="12345678900",
    data_nascimento="2005-05-10", status="ativo")
    novo_id = Crud.create_aluno(aluno1)
    print("Novo aluno criado com ID: ", novo_id)
    
    # READ por ID
    print("Buscando aluno criado...")
    print(Crud.read_aluno_by_id(novo_id))
    
    # READ lista
    print("Listando todos os alunos: ")
    print(Crud.read_alunos())
    
    # UPDATE
    print("Atualizando status do aluno...")
    Crud.update_aluno(novo_id, {"status": "inativo"})
    print(Crud.read_aluno_by_id(novo_id))
    
    # DELETE
    print("Removendo aluno...")
    Crud.delete_aluno(novo_id)
    print(Crud.create_alunoread_aluno_by_id(novo_id)) # Deve retornar None
    
    if __name__ == "__main__": 
        main()
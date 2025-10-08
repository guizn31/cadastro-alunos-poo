import tkinter as tk

def criar_janela_principal():
    janela = tk.Tk()
    janela.title("Sistema de Cadastro de Alunos - TechEduca")
    janela.geometry("400x400") # Define o tamanho da janela
    janela.configure(bg="#f0f0f0") # Define a cor de fundo da janela

    # Adiciona o texto de identificação da tela
    tk.Label(janela, text="Cadastro de Alunos", font=("Arial", 16, "bold"), bg="#f0f0f0").pack(pady=10)

    # Adiciona o texto indicando onde vai ser preenchido o nome do aluno
    tk.Label(janela, text="Nome do Aluno:", bg="#f0f0f0").pack()
    entrada_nome = tk.Entry(janela, width=40) # Variável que cria o widget para preencher o nome do aluno
    entrada_nome.pack(pady=5) # Cria a orientação do widget

    # Adiciona o texto indicando onde vai ser preenchido o cpf do aluno
    tk.Label(janela, text="CPF:", bg="#f0f0f0").pack() 
    entrada_cpf = tk.Entry(janela, width=40) # Variável que cria o widget para preencher o nome do aluno
    entrada_cpf.pack(pady=5) # Cria a orientação do widget

    # Adiciona o texto indicando onde vai ser preenchido o status do aluno
    tk.Label(janela, text="Status (Ativo/Inativo):", bg="#f0f0f0").pack()
    entrada_status = tk.Entry(janela, width=40) # Variável que cria o widget para preencher o status do aluno
    entrada_status.pack(pady=5) # Cria a orientação do widget

    # Cria os botões: seu tamanho, cor e orientação
    tk.Button(janela, text="Cadastrar", width=15, bg="#4CAF50", fg="white").pack(pady=5)
    tk.Button(janela, text="Atualizar", width=15, bg="#2196F3", fg="white").pack(pady=5)
    tk.Button(janela, text="Excluir", width=15, bg="#f44336", fg="white").pack(pady=5)
    tk.Button(janela, text="Consultar", width=15, bg="#9C27B0", fg="white").pack(pady=5)
    
    # Coloca a janela para rodar em loop
    janela.mainloop()

if __name__ == "__main__":
    criar_janela_principal()
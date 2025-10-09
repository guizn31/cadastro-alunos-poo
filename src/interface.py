import tkinter as tk
from tkinter import ttk, messagebox
from crud import Crud

def criar_janela_principal():
    janela = tk.Tk()
    janela.title("Sistema de Cadastro de Alunos - TechEduca")
    # centraliza a janela
    janela.configure(bg="#00fa9a")
    janela.minsize(500, 500)

    colunas = ("id", "nome", "cpf", "data_nascimento", "status")
    tabela = ttk.Treeview(janela, columns=colunas, show="headings", height=10)
    for c in colunas:
        tabela.heading(c, text=c.title())
        tabela.column(c, width=120 if c != "id" else 60, anchor="center")
    tabela.pack(pady=10, fill="both", expand=True)

    # Adiciona o texto de identificação da tela
    tk.Label(janela, text="Cadastro de Alunos", font=("Arial", 16, "bold"), bg="#13ee9a").pack(pady=10)

    # Adiciona o texto indicando onde vai ser preenchido o nome do aluno
    tk.Label(janela, text="Nome do Aluno:", bg="#00fa9a").pack()
    entrada_nome = tk.Entry(janela, width=40) # Variável que cria o widget para preencher o nome do aluno
    entrada_nome.pack(pady=5) # Cria a orientação do widget

    # Adiciona o texto indicando onde vai ser preenchido o cpf do aluno
    tk.Label(janela, text="CPF:", bg="#00fa9a").pack() 
    entrada_cpf = tk.Entry(janela, width=40) # Variável que cria o widget para preencher o nome do aluno
    entrada_cpf.pack(pady=5) # Cria a orientação do widget

    # Adiciona o texto indicando onde vai ser preenchido o cpf do aluno
    tk.Label(janela, text="Data de Nascimento:", bg="#00fa9a").pack() 
    entrada_data_nascimento = tk.Entry(janela, width=40) # Variável que cria o widget para preencher o nome do aluno
    entrada_data_nascimento.pack(pady=5) # Cria a orientação do widget

    # Adiciona o texto indicando onde vai ser preenchido o status do aluno
    tk.Label(janela, text="Status (Ativo/Inativo):", bg="#00fa9a").pack()
    entrada_status = tk.Entry(janela, width=40) # Variável que cria o widget para preencher o status do aluno
    entrada_status.pack(pady=5) # Cria a orientação do widget

    def limpar_campos():
        entrada_nome.delete(0, tk.END)
        entrada_cpf.delete(0, tk.END)
        entrada_data_nascimento.delete(0, tk.END)
        entrada_status.delete(0, tk.END)

    def carregar_lista():
        for item in tabela.get_children():
            tabela.delete(item)
        try:
            for a in Crud.read_alunos():  # retorno esperado: (id, nome, cpf, data_nascimento, status)
                tabela.insert("", "end", values=(a[0], a[1], a[2], a[3], a[4]))
        except Exception as e:
            messagebox.showerror("Erro", f"Falha ao carregar lista: {e}")
    
    def cadastrar():
        nome = entrada_nome.get().strip()
        cpf = entrada_cpf.get().strip()
        data = entrada_data_nascimento.get().strip()
        status = entrada_status.get().strip()
        if not (nome and cpf and data and status):
            messagebox.showerror("Erro", "Preencha todos os campos.")
            return
        try:
            Crud.create_aluno(nome, cpf, data, status)
            messagebox.showinfo("Sucesso", "Aluno cadastrado com sucesso!")
            carregar_lista()
            limpar_campos()
        except Exception as e:
            messagebox.showerror("Erro", f"Não foi possível cadastrar: {e}")

    def atualizar():
        cpf = entrada_cpf.get().strip()
        novo_status = entrada_status.get().strip()
        if not cpf or not novo_status:
            messagebox.showerror("Erro", "Informe CPF e novo status.")
            return
        try:
            linhas = Crud.update_aluno(cpf, {"status": novo_status})  # se seu update for por ID, adapte aqui
            if not linhas:
                messagebox.showwarning("Aviso", "Nenhum registro atualizado. Verifique o CPF.")
            else:
                messagebox.showinfo("Sucesso", "Status atualizado!")
                carregar_lista()
        except Exception as e:
            messagebox.showerror("Erro", f"Não foi possível atualizar: {e}")
    
    def excluir():
        cpf = entrada_cpf.get().strip()
        if not cpf:
            messagebox.showerror("Erro", "Informe o CPF para excluir.")
            return
        try:
            linhas = Crud.delete_aluno(cpf)  # se seu delete for por ID, adapte aqui
            if not linhas:
                messagebox.showwarning("Aviso", "Nenhum registro excluído. Verifique o CPF.")
            else:
                messagebox.showinfo("Sucesso", "Aluno excluído!")
                carregar_lista()
                limpar_campos()
        except Exception as e:
            messagebox.showerror("Erro", f"Não foi possível excluir: {e}")

    # Cria os botões: seu tamanho, cor e orientação
    tk.Button(janela, text="Cadastrar", width=15, bg="#4CAF50", fg="white",
          command=cadastrar).pack(pady=5)

    tk.Button(janela, text="Atualizar", width=15, bg="#2196F3", fg="white",
            command=atualizar).pack(pady=5)

    tk.Button(janela, text="Excluir", width=15, bg="#f44336", fg="white",
            command=excluir).pack(pady=5)

    tk.Button(janela, text="Consultar", width=15, bg="#9C27B0", fg="white",
            command=carregar_lista).pack(pady=5)
    
    carregar_lista()

    # Coloca a janela para rodar em loop
    janela.mainloop()

if __name__ == "__main__":
    criar_janela_principal()


    
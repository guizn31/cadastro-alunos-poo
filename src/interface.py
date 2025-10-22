import tkinter as tk
from tkinter import ttk, messagebox
from crud import Crud

def criar_janela_principal():
    janela = tk.Tk()
    janela.title("Sistema de Cadastro de Alunos - TechEduca")
    janela.geometry("600x500") # Define o tamanho da janela
    janela.configure(bg="#f0f0f0") # Define a cor de fundo da janela

    # --- BARRA DE RELATÓRIOS (FILTROS) ---
    barra = tk.Frame(janela, bg="#f0f0f0")
    barra.pack(pady=5, fill="x")

    tk.Label(barra, text="Buscar por nome:", bg="#f0f0f0").pack(side="left", padx=(0,6))
    entrada_busca_nome = tk.Entry(barra, width=30)
    entrada_busca_nome.pack(side="left")

    var_somente_ativos = tk.BooleanVar()
    ck_ativos = tk.Checkbutton(barra, text="Somente Ativos", bg="#f0f0f0", variable=var_somente_ativos)
    ck_ativos.pack(side="left", padx=10)

    # Botões de ação do relatório
    tk.Button(barra, text="Buscar", command=lambda: carregar_relatorio()).pack(side="left", padx=5)
    tk.Button(barra, text="Limpar Filtros", command=lambda: limpar_filtros()).pack(side="left", padx=5)
    tk.Button(barra, text="Atualizar", command=lambda: carregar_relatorio()).pack(side="left", padx=5)

    colunas = ("id", "nome", "cpf", "data_nascimento", "status")
    tabela = ttk.Treeview(janela, columns=colunas, show="headings", height=10)
    for c in colunas:
        tabela.heading(c, text=c.title())
        tabela.column(c, width=120 if c != "id" else 60, anchor="center")
        tabela.column("id", width=60, anchor="center")
        tabela.column("nome", width=200, anchor="w")
        tabela.column("cpf", width=140, anchor="center")
        tabela.column("data_nascimento", width=120, anchor="center")
        tabela.column("status", width=100, anchor="center")
    tabela.pack(pady=10, fill="both", expand=True)

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

    # Adiciona o texto indicando onde vai ser preenchido o cpf do aluno
    tk.Label(janela, text="Data de Nascimento:", bg="#f0f0f0").pack() 
    entrada_data_nascimento = tk.Entry(janela, width=40) # Variável que cria o widget para preencher o nome do aluno
    entrada_data_nascimento.pack(pady=5) # Cria a orientação do widget

    # Adiciona o texto indicando onde vai ser preenchido o status do aluno
    tk.Label(janela, text="Status (Ativo/Inativo):", bg="#f0f0f0").pack()
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
    
    carregar_lista()
    
    def aplicar_filtros(alunos, nome_busca, somente_ativos):
        # alunos: lista de tuplas (id, nome, cpf, data_nascimento, status)
        if nome_busca:
            nb = nome_busca.strip().lower()
            alunos = [a for a in alunos if nb in (a[1] or "").lower()]
        if somente_ativos:
            alunos = [a for a in alunos if (a[4] or "").strip().lower() == "ativo"]
        return alunos

    def carregar_relatorio():
        # Limpa a tabela e carrega com base nos filtros
        for item in tabela.get_children():
            tabela.delete(item)
        try:
            dados = Crud.read_alunos()
            dados = aplicar_filtros(dados, entrada_busca_nome.get(), var_somente_ativos.get())
            if not dados:
                messagebox.showinfo("Relatório", "Nenhum registro encontrado para os filtros informados.")
            for a in dados:
                tabela.insert("", "end", values=(a[0], a[1], a[2], a[3], a[4]))
        except Exception as e:
            messagebox.showerror("Erro", f"Falha ao gerar relatório: {e}")

    def limpar_filtros():
        entrada_busca_nome.delete(0, tk.END)
        var_somente_ativos.set(False)
        carregar_relatorio()

    # Coloca a janela para rodar em loop
    janela.mainloop()

if __name__ == "__main__":
    criar_janela_principal()
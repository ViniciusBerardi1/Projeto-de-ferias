import tkinter as tk
from tkinter import messagebox, simpledialog

# Lista para armazenar os membros
membros = []


def adicionar_membro():
    nome = simpledialog.askstring("Nome", "Digite o nome do membro:")
    if not nome:
        return
    idade = simpledialog.askstring("Idade", "Digite a idade do membro:")
    if not idade:
        return
    email = simpledialog.askstring("Email", "Digite o email do membro:")
    if not email:
        return

    membro = {
        "nome": nome,
        "idade": idade,
        "email": email
    }

    membros.append(membro)
    messagebox.showinfo("Sucesso", "Membro adicionado com sucesso!")


def exibir_membros():
    if not membros:
        messagebox.showinfo("Membros", "Nenhum membro cadastrado.")
    else:
        membros_str = ""
        for idx, membro in enumerate(membros, start=1):
            membros_str += f"Membro {idx}:\nNome: {membro['nome']}\nIdade: {membro['idade']}\nEmail: {membro['email']}\n\n"
        messagebox.showinfo("Membros Cadastrados", membros_str)


def buscar_membro():
    nome = simpledialog.askstring("Buscar Membro", "Digite o nome do membro:")
    if not nome:
        return

    encontrado = False
    for membro in membros:
        if membro["nome"].lower() == nome.lower():
            encontrado = True
            membro_str = f"Nome: {membro['nome']}\nIdade: {membro['idade']}\nEmail: {membro['email']}"
            messagebox.showinfo("Membro Encontrado", membro_str)
            break
    if not encontrado:
        messagebox.showinfo("Erro", "Membro não encontrado.")


def excluir_membro():
    nome = simpledialog.askstring(
        "Excluir Membro", "Digite o nome do membro a excluir:")
    if not nome:
        return

    for membro in membros:
        if membro["nome"].lower() == nome.lower():
            membros.remove(membro)
            messagebox.showinfo("Sucesso", "Membro excluído com sucesso!")
            return

    messagebox.showinfo("Erro", "Membro não encontrado.")


# Criação da janela principal
root = tk.Tk()
root.title("Cadastro de Membros do Clube")
root.geometry("350x300")  # Definindo o tamanho da janela

# Frame para centralizar os botões
frame = tk.Frame(root)
frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

# Botões para as funcionalidades
btn_adicionar = tk.Button(
    frame, text="Adicionar Novo Membro", command=adicionar_membro, width=20)
btn_exibir = tk.Button(
    frame, text="Exibir Todos os Membros", command=exibir_membros, width=20)
btn_buscar = tk.Button(
    frame, text="Buscar Membro por Nome", command=buscar_membro, width=20)
btn_excluir = tk.Button(
    frame, text="Excluir Membro", command=excluir_membro, width=20)
btn_sair = tk.Button(
    frame, text="Sair", command=root.quit, width=20)

# Posicionamento dos botões na janela
btn_adicionar.pack(pady=5)
btn_exibir.pack(pady=5)
btn_buscar.pack(pady=5)
btn_excluir.pack(pady=5)
btn_sair.pack(pady=5)

# Execução da janela principal
root.mainloop()

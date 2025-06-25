import tkinter as tk
from tkinter import messagebox
import requests

import tkinter as tk
from tkinter import ttk, messagebox
import requests

API_BASE = "http://localhost:5000/"

# Configuração dos campos por entidade
FIELDS = {
    "pacientes": ["nome", "cpf", "data_nascimento", "telefone", "prontuario"],
    "medicos":   ["nome", "cpf", "data_nascimento", "telefone", "crm", "especialidade_id"],
    "consultas": ["paciente_id", "medico_id", "data_consulta", "horario"],
    "tratamentos": ["descricao", "data_inicio", "data_fim", "consulta_id"],
    "posologias": ["medicamento_id", "tratamento_id", "receita", "qtd_utilizada"],
    "medicamentos": ["nome", "dosagem", "forma_apresentacao", "qtd_estoque"]
}


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Clínica Médica")
        self.geometry("300x350")
        tk.Label(self, text="Bem-vindo à Clínica Médica", font=("Arial", 16)).pack(pady=20)

        for ent in FIELDS:
            btn = tk.Button(self, text=ent.capitalize(), width=25,
                            command=lambda e=ent: WindowCRUD(self, e))
            btn.pack(pady=5)


class WindowCRUD(tk.Toplevel):
    def __init__(self, master, entidade):
        super().__init__(master)
        self.entidade = entidade
        self.title(entidade.capitalize())
        self.geometry("700x500")

        # Botões de operação
        frm = tk.Frame(self)
        frm.pack(fill="x", pady=10)
        for op in ("Listar", "Criar", "Editar", "Deletar"):
            tk.Button(frm, text=op, command=getattr(self, op.lower())).pack(side="left", padx=5)

        # Configuração da tabela Colunas
        cols = ["id"] + FIELDS[entidade]
        self.tree = ttk.Treeview(self, columns=cols, show="headings")
        for c in cols:
            self.tree.heading(c, text=c.replace("_", " ").capitalize())
            self.tree.column(c, width=100)
        self.tree.pack(expand=True, fill="both")

    def listar(self):
        try:
            r = requests.get(f"{API_BASE}/{self.entidade}")
            r.raise_for_status()
            dados = r.json()
            self.tree.delete(*self.tree.get_children())
            for obj in dados:
                row = [obj.get(c) for c in ["id"] + FIELDS[self.entidade]]
                self.tree.insert("", "end", values=row)
        except Exception as e:
            messagebox.showerror("Erro ao listar", str(e))

    def criar(self):
        FormWindow(self, self.entidade, mode="criar")

    def editar(self):
        sel = self.tree.focus()
        if not sel:
            return messagebox.showwarning("Selecionar", "Nenhum item selecionado")
        FormWindow(self, self.entidade, mode="editar", selected=sel)

    def deletar(self):
        sel = self.tree.focus()
        if not sel:
            return messagebox.showwarning("Selecionar", "Nenhum item selecionado")
        obj_id = self.tree.item(sel)["values"][0]
        if messagebox.askyesno("Confirmar", f"Deletar {self.entidade[:-1]} id={obj_id}?"):
            try:
                r = requests.delete(f"{API_BASE}/{self.entidade}/{obj_id}")
                r.raise_for_status()
                self.listar()
            except Exception as e:
                messagebox.showerror("Erro ao deletar", str(e))


class FormWindow(tk.Toplevel):
    def __init__(self, master, entidade, mode="criar", selected=None):
        super().__init__(master)
        self.entidade = entidade
        self.mode = mode
        self.selected = selected
        self.title(f"{mode.capitalize()} {entidade[:-1]}")
        self.geometry("400x400")

        frm = tk.Frame(self)
        frm.pack(pady=10, padx=10)
        self.vars = {f: tk.StringVar() for f in FIELDS[entidade]}

        for i, f in enumerate(FIELDS[entidade]):
            tk.Label(frm, text=f.replace("_", " ").capitalize() + ":").grid(row=i, column=0, sticky="e", pady=5)
            tk.Entry(frm, textvariable=self.vars[f], width=30).grid(row=i, column=1, pady=5)

        # Botão para criar ou atualizar
        btn_frame = tk.Frame(self)
        btn_frame.pack(pady=10)

        action_label = "Criar" if mode == "criar" else "Atualizar"
        tk.Button(btn_frame, text=action_label, width=20, command=self.submit).pack()

        # Preencher os dados se for modo de edição
        if mode == "editar":
            data = master.tree.item(selected)["values"]
            for idx, f in enumerate(FIELDS[entidade], start=1):
                self.vars[f].set(data[idx])
            self.obj_id = data[0]

    def submit(self):
        payload = {k: v.get() for k, v in self.vars.items()}
        try:
            if self.mode == "criar":
                r = requests.post(f"{API_BASE}/{self.entidade}", json=payload)
            else:
                r = requests.put(f"{API_BASE}/{self.entidade}/{self.obj_id}", json=payload)
            r.raise_for_status()
            messagebox.showinfo("Sucesso", f"{self.entidade[:-1].capitalize()} {'criado' if self.mode=='criar' else 'atualizado'}")
            self.master.listar()
            self.destroy()
        except Exception as e:
            messagebox.showerror("Erro", str(e))


if __name__ == "__main__":
    App().mainloop()
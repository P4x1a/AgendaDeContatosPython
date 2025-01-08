import json
import csv

def adicionar_contato(agenda, nome, telefone, email):
    if nome in agenda:
        print("Contato já existe.")
    else:
        agenda[nome] = {"telefone": telefone, "email": email}
        print("Contato adicionado com sucesso.")

def remover_contato(agenda, nome):
    if nome in agenda:
        del agenda[nome]
        print("Contato removido com sucesso.")
    else:
        print("Contato não encontrado.")

def editar_contato(agenda, nome):
    if nome in agenda:
        print(f"Editando contato: {nome}")
        telefone = input("Novo Telefone: ")
        email = input("Novo E-mail: ")
        agenda[nome] = {"telefone": telefone, "email": email}
        print("Contato atualizado com sucesso.")
    else:
        print("Contato não encontrado.")

def listar_contatos(agenda):
    if agenda:
        for nome, info in agenda.items():
            print(f"Nome: {nome}, Telefone: {info['telefone']}, E-mail: {info['email']}")
    else:
        print("Agenda vazia.")

def buscar_contato(agenda, nome):
    if nome in agenda:
        info = agenda[nome]
        print(f"Nome: {nome}, Telefone: {info['telefone']}, E-mail: {info['email']}")
    else:
        print("Contato não encontrado.")

def salvar_agenda(agenda, filename):
    with open(filename, 'w') as file:
        json.dump(agenda, file)
    print("Agenda salva com sucesso.")

def carregar_agenda(filename):
    try:
        with open(filename, 'r') as file:
            agenda = json.load(file)
        return agenda
    except FileNotFoundError:
        return {}

def exportar_contatos(agenda, filename):
    try:
        with open(filename, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Nome", "Telefone", "E-mail"])
            for nome, info in agenda.items():
                writer.writerow([nome, info["telefone"], info["email"]])
        print("Contatos exportados com sucesso.")
    except Exception as e:
        print(f"Erro ao exportar contatos: {e}")

def importar_contatos(filename):
    try:
        agenda = {}
        with open(filename, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                agenda[row["Nome"]] = {"telefone": row["Telefone"], "email": row["E-mail"]}
        print("Contatos importados com sucesso.")
        return agenda
    except Exception as e:
        print(f"Erro ao importar contatos: {e}")
        return {}

from agenda import (
    adicionar_contato,
    remover_contato,
    editar_contato,
    listar_contatos,
    buscar_contato,
    salvar_agenda,
    carregar_agenda,
    exportar_contatos,
    importar_contatos
)

def main():
    agenda = carregar_agenda("agenda.json")

    while True:
        print("\nAgenda de Contatos")
        print("1. Adicionar contato")
        print("2. Remover contato")
        print("3. Listar todos os contatos")
        print("4. Buscar contato pelo nome")
        print("5. Editar contato")
        print("6. Exportar contatos")
        print("7. Importar contatos")
        print("8. Salvar e sair")

        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            nome = input("Nome: ")
            telefone = input("Telefone: ")
            email = input("E-mail: ")
            adicionar_contato(agenda, nome, telefone, email)
        elif escolha == "2":
            nome = input("Nome do contato a ser removido: ")
            remover_contato(agenda, nome)
        elif escolha == "3":
            listar_contatos(agenda)
        elif escolha == "4":
            nome = input("Nome do contato a ser buscado: ")
            buscar_contato(agenda, nome)
        elif escolha == "5":
            nome = input("Nome do contato a ser editado: ")
            editar_contato(agenda, nome)
        elif escolha == "6":
            filename = input("Digite o nome do arquivo para exportar: ")
            exportar_contatos(agenda, filename)
        elif escolha == "7":
            filename = input("Digite o nome do arquivo para importar: ")
            agenda.update(importar_contatos(filename))
        elif escolha == "8":
            print("Saindo da agenda de contatos.")
            salvar_agenda(agenda, "agenda.json")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()

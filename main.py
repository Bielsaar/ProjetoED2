from Filme import Filme
from No import Node
ids = 0
def menu():
    print("="*50)
    print("1- Inserir um filme")
    print("2- Procurar um Filme pelo nome")
    print("3- Procurar um Filmes pelo ID")
    print("4- Listar todos os Filmes")
    print("5- Saber a altura da arvore")
    print("6- Esta balanceada? ")
    print("7- Sair")
    print("="*50)
    choice = int(input("Option: "))
    return choice

def create_Filme_and_insert(root):
    nome = input("Nome do Filme: ")
    global ids 
    ids += 1
    ano = int(input("Ano de lançamento: "))
    filme = Filme(nome, ano, ids)
    root = root.insert(filme)
    return root

def search(root, nome):
    result = root.search_by_name(nome)
    if result is not None:
        print(result.get_nome())
        print(result.get_ano())
        print(result.get_aid())
    else:
        print("Filme nao encontrado")


def main():
    root = Node()
    choice = menu()
    while choice != 7:
        if  choice == 1:
            root  = create_Filme_and_insert(root)
        elif choice == 2:
            nome = input("Nome do Filme: ")
            search(root, nome)
        elif choice == 3:
            ano = int(input("ID: "))
            root.search_by_id(ano)
        elif choice == 4:
            print("Lista de todas os Filmes: ")
            root.list_items()
        elif choice == 5:
            print("Altura da arvore: ", root.height(root) - 1)
        elif choice == 6:
            result = root.is_balanced(root)
            if result == True:
                print("Arvore balanceada")
                print(root)
            else:
                print("Arvore nao esta balanceada")
        choice = menu()
if __name__ == "__main__":
    main()

from matplotlib import pyplot as plt

print("Gerenciamento de Estoque")
nome = input("digite seu nome: ")
acessar = input(f"\n Olá {nome}, digite (e) para entrar ou (s) para sair: ").lower()

estoque = []
contador_id = 1

def cadastrar_item():
    global contador_id
    nomeprod = input("Insira o nome do produto: ")
    categoria = input("Insira qual a categoria do produto: ")

    try:
        quantidade = int(input("Digite a quantidade do produto: "))
    except ValueError:
        print("ERRO: você, digitou um valor invalido8")
        return

    try:
        preço = float(input(f"Digite o valor do produto (ex:10.99): "))
    except ValueError:
        print("ERRO: O valor deve ser um número. Operação cancelada.")
        return

    valor_total = preço * quantidade

    item = {
        "id": contador_id,
        "nome": nomeprod,
        "categoria": categoria,
        "quantidade": quantidade,
        "valor": preço,
        "valor_total": valor_total
    }
    estoque.append(item)
    print(f" Item cadastrado com ID: {contador_id}.")
    contador_id += 1

def listar_itens():
    if not estoque:
        print("\n Estoque Vazio.")
        return

    for item in estoque:
        print(f"ID: {item['id']}")
        print(f"Nome: {item['nome']}")
        print(f"Categoria: {item['categoria']}")
        print(f"quantidade em estoque: {item['quantidade']}")
        print(f"Valor do produto: {item['valor']:.2f}")
        print(f"Valor total do produto no estoque: {item['valor_total']:.2f}")
        if item['quantidade'] < 5:
            print("--- ATENÇÃO: Baixo estoque! ---")
def excluir_item():
    if not estoque:
        print("\n[!] Não há itens para excluir.")
        return
    try:
        id_excluir = int(input("Digite o ID do item a excluir: "))
        quantidade_remocao = int(input("Digite a quantidade a ser removida: "))

    except ValueError:
        print("[!] Entrada inválida. Digite um número inteiro.")
        return

    item_encontrado = False
    for item in estoque:
        if item["id"] == id_excluir:
            if quantidade_remocao <= item["quantidade"]:
                item["quantidade"] -= quantidade_remocao
                item["valor_total"] = item["quantidade"] * item["valor"]
                print(f"[ok] {quantidade_remocao} unidades do item com ID: {id_excluir} removidas. Quantidade restante: {item['quantidade']}.")
            else:
                print(f"[!] Quantidade a remover ({quantidade_remocao}) é maior do que a quantidade em estoque ({item['quantidade']}). Removendo o item completamente.")
                estoque.remove(item)
                print(f"[ok] Item com ID: {id_excluir}, excluído completamente.")
            item_encontrado = True
            break
    if not item_encontrado:
        print(f"[!] ID: {id_excluir} não encontrado. ")

def grafico_estoque():
    if not estoque:
        print("\nNão há produtos cadastrados para gerar gráfico.")
        return

    nomes = [produto["nome"] for produto in estoque]
    quantidades = [produto["quantidade"] for produto in estoque]

    plt.figure(figsize=(5, 2))
    plt.bar(nomes, quantidades, color='purple')
    plt.title("Estoque por Produto")
    plt.xlabel("Produtos")
    plt.ylabel("Quantidade")
    plt.tight_layout()
    plt.show()

def menu():
    while True:
        print("\n =================GRENCIAMENTO DE ESTOQUE=================")
        print("1) Cadastrar item")
        print("2) Listar itens")
        print("3) Excluir item")
        print("4) Ver gráfico do estoque")
        print("s) Sair")

        opcao = input("Escolha: ").lower()
        if opcao == "1":
            cadastrar_item()
        elif opcao == "2":
            listar_itens()
        elif opcao == "3":
            excluir_item()
        elif opcao == "4":
            grafico_estoque()
        elif opcao == "s":
            print("Saindo do menu...")
            return "s"
        else:
            print("[!] opção inválida.")

if acessar == "e":
    menu()

print("\nSaindo do sistema.")
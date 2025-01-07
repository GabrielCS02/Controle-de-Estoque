# Sistema de Controle de Estoque
estoque = {}

def menu():
    print("\n--- Sistema de Controle de Estoque ---")
    print("1. Adicionar Produto")
    print("2. Atualizar Produto")
    print("3. Excluir Produto")
    print("4. Remover Quantidade do Estoque")
    print("5. Visualizar Estoque")
    print("6. Sair")
    return input("Escolha uma opção: ")

def adicionar_produto():
    while True:
        nome = input("Digite o nome do produto: ").strip()
        if any(char.isalpha() for char in nome):  # Verifica se contém pelo menos uma letra
            break
        else:
            print("O nome do produto deve conter pelo menos uma letra. Tente novamente.")
    
    if nome in estoque:
        print("Produto já existe no estoque!")
    else:
        preco = float(input("Digite o preço do produto: "))
        quantidade = int(input("Digite a quantidade em estoque: "))
        estoque[nome] = {"preço": preco, "quantidade": quantidade}
        print("Produto adicionado com sucesso!")

def atualizar_produto():
    nome = input("Digite o nome do produto que deseja atualizar: ").strip()
    if nome in estoque:
        preco = float(input("Digite o novo preço do produto: "))
        quantidade = int(input("Digite a nova quantidade em estoque: "))
        estoque[nome] = {"preço": preco, "quantidade": quantidade}
        print("Produto atualizado com sucesso!")
    else:
        print("Produto não encontrado no estoque!")

def excluir_produto():
    nome = input("Digite o nome do produto que deseja excluir: ").strip()
    if nome in estoque:
        del estoque[nome]
        print("Produto excluído com sucesso!")
    else:
        print("Produto não encontrado no estoque!")

def remover_quantidade_produto():
    nome = input("Digite o nome do produto para remover do estoque: ").strip()
    if nome in estoque:
        quantidade_atual = estoque[nome]["quantidade"]
        print(f"Quantidade atual do produto '{nome}': {quantidade_atual}")
        quantidade_remover = int(input("Digite a quantidade a ser removida: "))
        
        if quantidade_remover > 0 and quantidade_remover <= quantidade_atual:
            estoque[nome]["quantidade"] -= quantidade_remover
            print(f"Quantidade de {quantidade_remover} removida do produto '{nome}'.")
            if estoque[nome]["quantidade"] == 0:
                print(f"Produto '{nome}' está com estoque zerado!")
        else:
            print("Quantidade inválida! A quantidade a ser removida deve ser positiva e menor ou igual à quantidade em estoque.")
    else:
        print("Produto não encontrado no estoque!")

def visualizar_estoque():
    if estoque:
        print("\n--- Estoque Atual ---")
        for nome, info in estoque.items():
            print(f"Nome: {nome}, Preço: R${info['preço']:.2f}, Quantidade: {info['quantidade']}")
    else:
        print("O estoque está vazio!")

# Loop Principal
while True:
    opcao = menu()
    if opcao == "1":
        adicionar_produto()
    elif opcao == "2":
        atualizar_produto()
    elif opcao == "3":
        excluir_produto()
    elif opcao == "4":
        remover_quantidade_produto()
    elif opcao == "5":
        visualizar_estoque()
    elif opcao == "6":
        print("Saindo do sistema...")
        break
    else:
        print("Opção inválida! Tente novamente.")

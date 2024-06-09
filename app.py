import os 

restaurantes = [{"nome": "PizzaCrack", "categoria": "Pizza", "ativo": False}, {"nome": "Pedro", "categoria": "Pizza", "ativo": False} ]

def printar_menu():
    print("1. Adicionar Restaurante")
    print("2. Listar Restaurantes")
    print("3. Ativar Restaurante")
    print("4. Sair")

def titulo_para_funcoes(titulo):
    os.system("cls")
    print(f"{titulo}\n")

def alterar_ativacao():
    titulo_para_funcoes("Alterando estado do restaurante")
    restaurante_encontrado = False
    nome = input("Digite o nome do restaurante que deseja alterar o estado: ")
    
    for restaurante in restaurantes:
            if restaurante["nome"] == nome:
                restaurante_encontrado = True    
                restaurante["ativo"] =  not restaurante["ativo"]
                alterado = "Restaurante Ativado com sucesso\n" if restaurante["ativo"] else "Restaurante desativado com sucesso\n"
                print(alterado)
    
    if restaurante_encontrado == False:
        print("Restaurante não encontrado")    
        
    voltar_menu()

def listar_restaurantes():
    titulo_para_funcoes("Listando Restaurantes")
    
    for restaurante in restaurantes:
        nome_restaurante = restaurante["nome"]
        categoria_restaurante = restaurante["categoria"]
        ativo = "Ativo" if restaurante["ativo"] else "Desativado"
        print(f"{nome_restaurante} | {categoria_restaurante} | {ativo}")
    voltar_menu()

def adicionar_restaurante():
    titulo_para_funcoes("Adicionando Restaurantes")
    nome = input("Digite o nome do restaurante: ")
    categoria = input("Digite a categoria do restaurante: ")
    dicionario = {"nome": nome, "categoria": categoria, "ativo": False}
    restaurantes.append(dicionario)
    print("Restaurante cadastrado com sucesso\n")
    voltar_menu()


def finalizar_programa():
    titulo_para_funcoes("Finalizando Programa")
    print("Programa finalizado com sucesso")

def voltar_menu():
    input("Aperte qualquer tecla para voltar ao menu principal: ")
    main()


def opcao_invalida():
    os.system("cls")
    print("Opção escolhida Invalida\n")
    voltar_menu()




def escolher_opcao():
    try:
        opcao = int(input("Digite uma opção: "))

        if opcao == 1:
            adicionar_restaurante()
        elif opcao == 2:
            listar_restaurantes()
        elif opcao == 3:
            alterar_ativacao()
        elif opcao == 4:
            finalizar_programa()
        else:
            opcao_invalida()
    except:
        opcao_invalida()




def main():
    os.system("cls")
    printar_menu()
    escolher_opcao()

if __name__ ==("__main__"):
    main()


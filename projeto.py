while True:
    print("Olá! Seja bem vindo(a) ao Gestor de Portifólio da Mari!!")
    print("Caso não saiba os comandos, digite: SABER_MAIS abaixo.")
    comando = str(input("Digite um comando: ")).upper()

    if comando == "SABER_MAIS":
        print("No momento temos três comandos: ABOUT, QUIT e ADD.\nABOUT: Mostra algumas informações sobre o programa.\nQUIT: Encerra o programa.\nADD: Cadastrar um novo projeto ao portifólio.")
        print("Voltando ao menu...")
              
    elif comando == "ABOUT":
        print("Este software é um Gestor de Portifólio, desenvolvido pela Mariana Batista dos Santos!\nEle é um projeto para a disciplina de Raciocínio Computacional")
        print("Voltando ao menu...")

    elif comando == "QUIT":
        print("Saindo do Gestor de Portifólio.")
        print("Até Logo, obrigada!")
        break
    
    elif comando == "ADD":
        numero_projetos = int(input("Quantos projetos gostaria de cadastrar? "))
        if numero_projetos <= 0:
            print("Não é possível cadastrar um número negativo ou zero projetos.")
        else: 
            for nome in range(numero_projetos):
                nome_projeto = input(f"Digite o nome do projeto {nome + 1}: ")
                print(f"Projeto '{nome_projeto}' cadastrado com sucesso!")
            if numero_projetos == numero_projetos:
                print("Todos os projetos foram cadastrados!")
                print("Voltando ao menu...")

    else:
        print("ERRO:Comando não encontrado")
        print("Voltando ao menu...")
    
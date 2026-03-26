print("Olá! Seja bem vindo(a) ao Gestor de Portifólio da Mari!!")
print("Caso não saiba os comandos, digite: SABER_MAIS abaixo.")
comando = str(input("Digite um comando: ")).upper()
if comando == "SABER_MAIS":
    print("No momento temos dois comandos: ABOUT e QUIT.\nABOUT: Mostra algumas informações sobre o programa.\nQUIT: Encerra o programa.")
elif comando == "ABOUT":
    print("Este software é um Gestor de Portifólio, desenvolvido pela Mariana Batista dos Santos!\nEle é um projeto para a disciplina de Raciocínio Computacional")
elif comando == "QUIT":
    print("Saindo do Gestor de Portifólio.")
else:
    print("ERRO:Comando não encontrado")
print("Até Logo, obrigada!")
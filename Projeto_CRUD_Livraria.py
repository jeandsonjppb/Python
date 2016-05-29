#Funções gerais
def menu():
    print("╔══════════════╗")
    print("║■■■■■■■■■■■■■■║")
    print("║ Ᵽутноп Ḇоокѕ ║")
    print("║■■■■■■■■■■■■■■║")
    print("║",3*" ","MENU",3*" ","║")
    print("╠","[1]Cadastrar","╣")
    print("╠","[2]Listar"," "*2,"╣")
    print("╠","[3]Procurar"," ""╣")
    print("╠","[4]Vender"," "*2,"╣")
    print("╠","[5]Sair"," "*4,"╣")
    print("╚══════════════╝")
def cadastro():
    print("╔══════════════╗")
    print("║■■■■■■■■■■■■■■║")
    print("║   CADASTRO   ║")
    print("║■■■■■■■■■■■■■■║")
    print("╚══════════════╝")
    livros.append(lerLivro())
    livros.append(lerQuant())
    arq = open("livraria.txt","a")
    print(livros, file = arq)
    arq.close()
    if continuarCadastrando() == True:
        cadastro()
def listar():
    print("╔══════════════╗")
    print("║■■■■■■■■■■■■■■║")
    print("║    LISTAR    ║")
    print("║■■■■■■■■■■■■■■║")
    print("╚══════════════╝")
    print("  Índice |"," "*12,"Título"," "*13,"|","Quantidade")
    indice=0
    for livro in livros:
        indice+=1
        print(" "*3,indice," "*2,"|",livro,"|"," "*3,livros[1]," "*4)

def pesquisar():
    print("╔══════════════╗")
    print("║■■■■■■■■■■■■■■║")
    print("║   PROCURAR   ║")
    print("║■■■■■■■■■■■■■■║")
    print("╚══════════════╝")
    opcao = ""
    while opcao != "N":
            pesquisa = input("Informe o título do livro:")
            if pesquisa not in livros:
                print("O livro:",pesquisa,", não esta cadastrado.")
                opcao2 = str.upper(input("Deseja cadastrar?[S/N]:"))
                if opcao2 == "S":
                    livros.append(pesquisa)
                    livros.append(lerQuant())
            else:
                print("O livro:",pesquisa,", está cadastrado.")
            opcao = str.upper(input("Continuar pesquisando?[S/N]:"))
def vendas():#falta as funcionalidades
    print("╔══════════════╗")
    print("║■■■■■■■■■■■■■■║")
    print("║    VENDAS    ║")
    print("║■■■■■■■■■■■■■■║")
    print("╚══════════════╝")
    if len(livros) == 0:
        print("Nenhum livro foi cadastrado. Vá até a opção CADASTRAR e cadastre o livro.")
    else:
        listar()
        vendido = int(input("Digite o índice do livro vendido:"))
            
#Funções de tratamento de erro
def lerLivro():
  while True:
    titulo = input("Digite o título do livro:")
    if len(titulo) < 4 or len(titulo) > 30:
      print("Erro!!! - O título deve conter de 4 a 30 caracteres.")
    else:
      return titulo
def cadastrarLivro():
  while True:
      entrada = input("Deseja cadastrar livros?[S/N]:")
      if entrada == "S" or entrada == "s":
        return True
      elif entrada == "N" or entrada == "n":
        return False
      else:
          print("ERRO!!! - Entrada Inválida, Digite 'S'|'s' ou 'N'|'n'")
def continuarCadastrando():
  while True:
      entrada = input("Continuar cadastrando livros?[S/N]:")
      if entrada == "S" or entrada == "s":
        return True
      elif entrada == "N" or entrada == "n":
        return False
      else:
          print("ERRO!!! - Entrada Inválida, Digite 'S'|'s' ou 'N'|'n'")
def lerQuant():
    while True:
        try:
            quant = int(input("Digite a quantidade para estoque:"))
            return quant
        except:
            print("ERRO!!! - A quantidade deve ser maior que 0 e não pode conter letras.")
def lerOpcoes():
    opcoes = [1,2,3,4,5]
    while True:
        try:
            opcao = int(input("Opção:"))
            if opcao not in opcoes:
                print("ERRO!!! - As opções são: 1,2,3,4 ou 5")
            else:
                return opcao
        except:
            print("ERRO!!! - As opções são: 1,2,3,4 ou 5 | Não pode conter letras!")

#Programa Principal  
livros = []
opcao = ""
while opcao != "5":
    menu()
    opcao = lerOpcoes()
    if opcao == 1:
        cadastro()
    elif opcao == 2:
        if len(livros) == 0:
            print("Nenhum livro foi cadastrado.")
            if cadastrarLivro() == True:
                cadastro()            
        else:          
            listar()
    elif opcao == 3:
        pesquisar()
    elif opcao == 4:
        vendas()
    else:
        print("Programa Finalizado!!!")
        arq = open("livraria.txt", "r")
        livros = arq.read()
        arq.close()
        break
         



import json
import os
import time

# --------------------------------------- FUNÇÕES: GLOBAL ------------------------------------------

caminhoDoArquivo = "animais.json"

def limpar_console():
    os.system('cls' if os.name == 'nt' else 'clear')
    
def PararOuContinuar():
    print("")
    opc = int(input("Deseja continuar?\n1 - Voltar | 2 - Encerrar o programa: "))
    if opc == 1:
        return True
    elif opc == 2:
        print("Finalizando o programa!")
        return False
    else:
        print("Opção inválida. Encerrando o programa.")
        return False


# --------------------------------------- MENU PRINCIPAL --------------------------------------------------

def MenuPrincipal():
    limpar_console()
    largura = 50
    print("\n" + "=" * largura)
    print(f"{'🐾  M E U   N O V O   P E T  🐾':^{largura}}")
    print("=" * largura)
    
    print(f"{'      / \\__            /\\   /\\':^{largura}}")
    print(f"{'     (    @\\___       { `---` }':^{largura}}")
    print(f"{'     /         O      /     \\  ':^{largura}}")
    print(f"{'   /   (_____ /      (       ) ':^{largura}}")
    print(f"{'  /_____ /   U        \\_ _ _/  ':^{largura}}")
    
    print("=" * largura)
    print(f"{'Bem-vindo(a) ao sistema de cadastro de pets!':^{largura}}")
    print(f"{'AUmentamos famílias desde 2012!':^{largura}}")
    print("=" * largura)
    print("Vamos começar? 🐶🐇")
    print("1 - Sistema de Pets")
    print("2 - Sistema de Adotantes")
    print("3 - Sistema de Doações")
    print("0 - Encerrar o programa")
    print("=" * largura + "\n")
    
    opcMenuPrincipal = (int(input("Insira a opção desejada: ")))
    
    match(opcMenuPrincipal):
        case 1:
            SistemaAnimais()
        case 2:
            print("Sistema de Adotantes...")
        case 3:
            print("Sistema de Doações...")
        case 0:
            print("Encerrando o programa... AUté mais!")
        case _:
            print("Opção inválida. Sistema encerrado.")


# --------------------------------------- FUNÇÕES SISTEMA ANIMAL ------------------------------------------

def CadastrarAnimal(nomeDoAnimal, sexoDoAnimal, especieDoAnimal, racaDoAnimal, idadeDoAnimal):
    nome = nomeDoAnimal
    sexo = sexoDoAnimal
    especie = especieDoAnimal
    raca = racaDoAnimal
    idade = int(idadeDoAnimal)
    
    animal = {
        "nome": nome,
        "sexo": sexo,
        "especie": especie,
        "raca": raca,
        "idade": idade
    }
    
    if os.path.exists(caminhoDoArquivo):
        with open(caminhoDoArquivo, 'r') as arquivo:
            try:
                animais = json.load(arquivo)
            except json.JSONDecodeError:
                animais = []
    else:
        animais = []
    
    animais.append(animal)
    
    with open(caminhoDoArquivo, 'w') as arquivo:
        json.dump(animais, arquivo, indent=4, ensure_ascii=False)
    
    print("Cadastrando animal...")
    time.sleep(2)
    print("Animal cadastrado com sucesso!")


def VisualizarAnimais():
    if os.path.exists(caminhoDoArquivo):
        with open(caminhoDoArquivo, 'r') as arquivo:
            animais = json.load(arquivo)
        
        if animais:
            i = 1
            for animal in animais:
                print(f"Animal {i}:")
                print(f"Nome: {animal['nome']}")
                print(f"Sexo: {animal['sexo']}")
                print(f"Espécie: {animal['especie']}")
                print(f"Raça: {animal['raca']}")
                print(f"Idade: {animal['idade']} anos")
                print("*******************************")
                i += 1
                time.sleep(0.5)
        else:
            print("Nenhum animal cadastrado.")
    else:
        print("Arquivo de animais não encontrado.")


def AtualizarAnimal(indice, novo_nome, novo_sexo, nova_especie, nova_raca, nova_idade):
    if os.path.exists(caminhoDoArquivo):
        with open(caminhoDoArquivo, 'r') as arquivo:
            animais = json.load(arquivo)
            if 1 <= indice <= len(animais):
                animais[indice - 1]['nome'] = novo_nome
                animais[indice - 1]['sexo'] = novo_sexo
                animais[indice - 1]['especie'] = nova_especie
                animais[indice - 1]['raca'] = nova_raca
                animais[indice - 1]['idade'] = int(nova_idade)

                with open(caminhoDoArquivo, 'w') as arquivo:
                    json.dump(animais, arquivo, indent=4, ensure_ascii=False)
                print("Atualizando o cadastro do animal...")   
                time.sleep(2)
                print("Cadastro atualizado com sucesso!")
            else:
                print("Índice inválido.")
    else:
        print("Arquivo de animais não encontrado.")


def ExcluirAnimal(indice):
    if os.path.exists(caminhoDoArquivo):
        with open(caminhoDoArquivo, 'r') as arquivo:
            animais = json.load(arquivo)
            if 1 <= indice <= len(animais):
                del animais[indice - 1]
                with open(caminhoDoArquivo, 'w') as arquivo:
                    json.dump(animais, arquivo, indent=4, ensure_ascii=False)  
                print("Deletando o animal do sistema...") 
                time.sleep(2)
                print("Animal deletado com sucesso!")
            else:
                print("Índice inválido.")
    else:
        print("Arquivo de animais não encontrado.")


def SistemaAnimais():
    while True:
        limpar_console()
        print("\n" + "=" * 40)
        print(f"{'CADASTRO: PETS':^40}")
        print("=" * 40)
        print("1 - Cadastrar Animal")
        print("2 - Visualizar Animais Cadastrados")
        print("3 - Atualizar Cadastro de Animal")
        print("4 - Excluir Cadastro de Animal")
        print("5 - Voltar para o Menu Principal")
        print("0 - Encerrar o Programa")
        print("=" * 40)

        opc = int(input("\nSelecione uma opção: "))
        match(opc):
            case 1:
                limpar_console()
                nomeDoAnimal = input("Digite o nome do animal: ")
                sexoDoAnimal = input("Digite o sexo do animal (M/F): ")
                especieDoAnimal = input("Digite a espécie do animal: ")
                racaDoAnimal = input("Digite a raça do animal: ")
                idadeDoAnimal = int(input("Digite a idade do animal: "))
                CadastrarAnimal(nomeDoAnimal, sexoDoAnimal, especieDoAnimal, racaDoAnimal, idadeDoAnimal)
            case 2:
                limpar_console()
                VisualizarAnimais()
            case 3:
                limpar_console()
                VisualizarAnimais() 
                indice = int(input("Digite o índice do animal que deseja atualizar: "))
                novo_nome = input("Digite o novo nome do animal: ")
                novo_sexo = input("Digite o novo sexo do animal (M/F): ")
                nova_especie = input("Digite a nova espécie do animal: ")
                nova_raca = input("Digite a nova raça do animal: ")
                nova_idade = int(input("Digite a nova idade do animal: "))
                AtualizarAnimal(indice, novo_nome, novo_sexo, nova_especie, nova_raca, nova_idade)
            case 4:
                limpar_console()
                VisualizarAnimais()
                indice = int(input("Insira o índice do animal que deseja deletar: "))
                ExcluirAnimal(indice)
            case 5:
                MenuPrincipal()
                break
            case 0:
                print("Finalizando o programa!")
                return False
            case _:
                limpar_console()
                print("Opção inválida! Você será redirecionado ao SistemaAnimais Principal.")
                print("-" * 10)
                continue

        if not PararOuContinuar():
            break

# --------------------------------------- MAIN ------------------------------------------

MenuPrincipal()

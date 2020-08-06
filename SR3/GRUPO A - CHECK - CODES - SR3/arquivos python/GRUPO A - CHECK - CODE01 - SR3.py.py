import sys #biblioteca para encerrar o programa
import serial #biblioteca que faz a conexão entre o arduino e o python

#dicionario com nome e tags dos alunos

alunos = {"2 55 70 48 48 51 53 70 54 48 65 66 54 4": "lucca",
          "2 55 70 48 48 51 53 70 54 48 65 66 54 5": "afonso",
          "2 55 70 48 48 51 53 70 54 48 65 66 54 6": "isalu",
          "2 55 70 48 48 51 53 70 54 48 65 66 54 3": "agra",
          "2 55 70 48 48 51 53 65 70 50 65 67 70 3": "parisio",
          "2 55 70 48 51 53 65 70 50 65 67 70 8": "liliane",
          "2 55 70 48 51 53 65 70 50 65 67 70 9": "bruno"}

tagrfid = []

#função para input login do professor

def professor_login(nome):
    nome_login = input('LOGIN: ')
    if nome_login == 'professor':
        professor_senha()
    else:
        print("\nLOGIN INVÁLIDO!\n")
        professor_login(nome)

#função para input da senha do professor

def professor_senha():
    senha = input('SENHA: ')
    if senha == 'professor123':
        print('\nBEM VINDO, {}!'.format(nome.upper()))
    else:
        print("\nSENHA INVÁLIDA!\n")
        professor_senha()
    cadastro()

#função para o professor inserir os dados da aula e nomear o arquivo final

def cadastro():
    global nomecompleto, curso
    print("\nINFORME OS DADOS DA AULA:")
    print("\n1 - CC (CIÊNCIA DA COMPUTAÇÃO)\n2 - DD (DESIGN)\n3 - CC & DD\n")
    try:
        curso = int(input("CURSO: "))
        if curso == 1:
            curso = 'CC'
        elif curso == 2:
            curso = 'DD'
        elif curso == 3:
            curso = 'CC&DD'
        else:
            print("OPÇÃO INVÁLIDA!")
            cadastro()
    except ValueError:
        print("OPÇÃO INVÁLIDA")
        cadastro()
    disciplina = str(input("DISCIPLINA: "))
    periodo = input("PERÍODO: ")
    turma = str(input("TURMA: "))
    data = input("DATA (EX: 16.06): ")
    nome_completo = curso.title() + '-' + disciplina.title() + '-' + periodo.title() + 'P' + '-' + 'T' + turma.title() + '-' + data.title()
    nomecompleto = nome_completo
    menu()

#função do menu principal

def menu():
    opcao = ''
    while opcao != 'sair':
        print("\n1 - LISTAR ALUNOS")
        print("2 - INICIAR RASTREAMENTO")
        print("3 - CRIAR ARQUIVO COM A LISTA DE ALUNOS AUSENTES")
        print("SAIR - ENCERRAR PROGRAMA")
        try:
            opcao = (input("\nDIGITE UMA DAS OPÇÕES ACIMA: "))

            if opcao == '1':
                listar_alunos()
            elif opcao == '2':
                print("1 - INICIAR\n2 - CANCELAR ")
                op = int(input("TEM CERTEZA QUE DESEJA INICIAR O RASTREAMENTO? "))
                if op == 1:
                    print("RASTREAMENTO INICIADO!")
                    rastreamento()
                elif op == 2:
                    menu()
                else:
                    print("OPÇÃO INVÁLIDA!")
            elif opcao == '3':
                criar_lista_ausentes()
            elif opcao == 'sair' or 'SAIR' or 'Sair':
                sys.exit()
            else:
                print("OPÇÃO INVÁLIDA!")
                menu()
        except ValueError:
            continue

#função que faz a listagem dos alunos, corresponde a opção 1 do menu

def listar_alunos():
    arq = open('alunos cadastrados.txt', 'r', encoding='utf8')
    listaralunos = arq.read()
    print(listaralunos)

#função que da incio ao rastreamento das tags com o arduino, corresponde a opção 2 do menu

def rastreamento():
    i = 0
    ser = serial.Serial("COM5", baudrate=9600, timeout=1)
    while 1:
        arduinoData = ser.readline().decode("ascii")
        if len(arduinoData) > 15:
            print(arduinoData.lstrip())
            tagrfid.append(arduinoData.lstrip() + "\n")

        elif arduinoData == "stop":
            break
    arquivo = open("presentes.txt", "w")
    arquivo.writelines(tagrfid)

    print("RASTREAMENTO FINALIZADO!")

#função que cria o arquivo com o numero das tags dos alunos ausentes

def criar_lista_ausentes():
    alunos = open('alunos.txt', 'r')
    presentes = open('presentes.txt', 'r')

    listalunos = alunos.readlines()
    listapresentes = presentes.readlines()

    result = listalunos
    i = 0
    for i in listalunos[:]:
        if i in listapresentes:
            result.remove(i)

        else:
            ausentes = open('ausentes.txt', 'a')
            ausentes.write(i)
            ausentes.close()
    criar_lista_prof()

#função que cria o arquivo final com os nomes dos alunos ausentes, corresponde a opção 3 do menu

def criar_lista_prof():
    nova = open(nomecompleto.upper() + '.csv', 'w')
    with open('ausentes.txt', 'r') as file:
        for i in file:
            nova2 = (alunos.get(i.rstrip()))
            nova.writelines(str(nova2) + '\n')
    nova.close()

#inicio do codigo

print("BEM VINDO(A) AO SISTEMA CHECK!\n")
nome = input("DIGITE O SEU NOME: ")
professor_login(nome)
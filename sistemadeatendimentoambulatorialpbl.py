#Autor: Antônio Felipe Ferreira de Jesus Moreira
#Componente curricular: Algoritimos I
#Concluido em 03/02/2020
#declaro que este código foi elaborado por mim de forma individual e não contém
#nenhum trecho de código de outro colega ou de outro autor, tais como provindos
#de livros e apostilas, e páginas ou documentos eletrônicos da internet. Qualquer
#trecho de código de outra autoria  que não a minha está destacado com uma citação
#para o autor e a fonte do código, e estou ciente que estes trechos não serão considerados
#para fins de avaliação
from datetime import time
pacientes_comuns_dermatologia = {}
pacientes_prioridade_dermatologia = {}
pacientes_comuns_endocrinologia = {}
pacientes_prioridade_endocrinologia = {}
pacientes_comuns_ortopedia = {}
pacientes_prioridade_ortopedia = {}
pacientes_atendidos = {}
pacientes_atendidos_prioridade = {}
pacientes_atendidos_comum = {}
pacientes_atendidos_dermatologia = {}
pacientes_atendidos_endocrinologia = {}
pacientes_atendidos_ortopedia = {}
pacientes_atendidos_comum_dermatologia = {}
pacientes_atendidos_comum_endocrinologia = {}
pacientes_atendidos_comum_ortopedia = {}
pacientes_atendidos_prioridade_dermatologia = {}
pacientes_atendidos_prioridade_endocrinologia = {}
pacientes_atendidos_prioridade_ortopedia = {}
em_atendimento_dermatologia = {}
em_atendimento_endocrinologia = {}
em_atendimento_ortopedia = {}
em_atendimento = {}
opcao = 0
numero_senha = 1
tempo_espera = 0
tempo_atendimento = 0

def hora(hora):
    h = hora // 60
    m = hora % 60
    hora = h, ':', m

def chamar_paciente_cd():
    pcd = pacientes_comuns_dermatologia.values()
    PCD = list(pcd)
    Pcd = PCD[0]
    print (Pcd)
    
def chamar_paciente_pd():
    ppd = pacientes_prioridade_dermatologia.values()
    PPD = list(ppd)
    Ppd = PPD[0]
    print(Ppd)
    
def chamar_paciente_ce():
    pce = pacientes_comuns_endocrinologia.values()
    PCE = list(pce)
    Pce = PCE[0]
    print (Pce)
    
def chamar_paciente_pe():
    ppe = pacientes_prioridade_endocrinologia.values()
    PPE = list(ppe)
    Ppe = PPE[0]
    print(Ppe)
    
def chamar_paciente_co():
    pco = pacientes_comuns_ortopedia.values()
    PCO = list(pco)
    Pco = PCO[0]
    print (Pco)
    
def chamar_paciente_po():
    ppo = pacientes_prioridade_ortopedia.values()
    PPO = list(ppo)
    Ppo = PPO[0]
    print (Ppo)
    
def adicionar_lista(lista):
    info_paciente = 'Nome do paciente: ', nome_paciente, 'Senha: ', senha, 'Tempo de espera: ', tempo_espera, 'Tempo de atendimento: ', tempo_atendimento
    lista[senha] = info_paciente
    
def gerar_senha(lista):
    print(nome_paciente, 'Senha: ', senha)
    info_paciente = 'Nome do paciente: ', nome_paciente, 'Senha: ', senha, 'Tempo de espera: ', tempo_espera, 'Tempo de atendimento: ', tempo_atendimento
    lista[senha] = info_paciente
    
def exclusao ():
    excluir = input('Digite a senha: ')
    try:
        del pacientes_comuns_dermatologia [excluir]
    except:
        try:
            del pacientes_prioridade_dermatologia [excluir]
        except:
            try:
                del pacientes_comuns_endocrinologia [excluir]
            except:
                try:
                    del pacientes_prioridade_endocrinologia [excluir]
                except:
                    try:
                      del pacientes_comuns_ortopedia [excluir]
                    except:
                        del pacientes_prioridade_ortopedia [excluir]
                        
while opcao != 9:
    print('1. Emitir nova senha')
    print('2. Chamar paciente para atendimento')
    print('3. Pular paciente')
    print('4. Encerrar uma consulta')
    print('5. Exibir fila de espera')
    print('6. Exibir pacientes atendidos no dia')
    print('7. Exibir tempo médio de espera dos pacientes')
    print('8. Exibir tempo médio de atendimento dos pacientes')
    print('9. Sair')
    opcao = int(input('Digite sua opção: '))
    
    if opcao == 1:
        nome_paciente = input('Digite o nome do paciente: ')
        print('1. Comum', '\n2. Prioritário')
        risco_paciente = int(input('Digite o número da classificassão de risco: '))
        print('1. Dermatologia', '\n2. Endocrinologia', '\n3. Ortopedia')
        escpecialidade_consulta = int(input('Digite o número da especialidade: ' ))
        hora_chegada = int(input('Digite a hora(0 a 23) e os minutos (0 a 59) de chegada do paciente, sem nenhum ponto, espaço, ou outro caracter entre eles: '))
        senha = 0
        info_paciente = 0
        str_senha = str(numero_senha)
        if risco_paciente == 1:
            if escpecialidade_consulta == 1:
                senha = 'cd' + str_senha
                gerar_senha(pacientes_comuns_dermatologia)
            elif escpecialidade_consulta == 2:
                senha = 'ce' + str_senha
                gerar_senha(pacientes_comuns_endocrinologia)
            else:
                senha = 'co' + str_senha
                gerar_senha(pacientes_comuns_ortopedia)
        else:
            if escpecialidade_consulta == 1:
                senha = 'pd' + str_senha
                gerar_senha(pacientes_prioridade_dermatologia)
            elif escpecialidade_consulta == 2:
                senha = 'pe' + str_senha
                gerar_senha(pacientes_prioridade_endocrinologia)
            else:
                senha = 'po' + str_senha
                gerar_senha(pacientes_prioridade_ortopedia)
        numero_senha += 1
        
    elif opcao == 2:
        consultorio_a_ser_chamado = int(input('Digite o número do consultório a ser chamado\n1. Dermatologia\n2. '
                                              'Endocrinologia\n3. Ortopedia\n: '))
        if consultorio_a_ser_chamado == 1:
            if not any(pacientes_prioridade_dermatologia):
                chamar_paciente_cd()
            elif not any(pacientes_comuns_dermatologia):
                chamar_paciente_pd()
            else:
                if not any (pacientes_atendidos_dermatologia):
                    chamar_paciente_pd()
                else:
                    if pacientes_atendidos_dermatologia[senha][3] == c:
                        chamar_paciente_pd()
                    elif pacientes_atendidos_dermatologia[senha][3] == p:
                        if Ppd[1] > Pcd[1]:
                            chamar_paciente_cd()
                        elif Ppd[1] < Pcd [1]:
                            chamar_paciente_pd()
        elif consultorio_a_ser_chamado == 2:
            if not any(pacientes_prioridade_endocrinologia):
                chamar_paciente_ce()
            elif not any(pacientes_comuns_endocrinologia):
                chamar_paciente_pe()
            else:
                if not any (pacientes_atendidos_endocrinologia):
                    chamar_paciente_pe()
                else:
                    if pacientes_atendidos_endocrinologia[senha][3] == c:
                        chamar_paciente_pe()
                    elif pacientes_atendidos_endocrinologia[senha][3] == p:
                        if Ppe[1] > Pce[1]:
                            chamar_paciente_ce()
                        elif Ppe[1] < Pce [1]:
                            chamar_paciente_pe()
        else:
            if not any(pacientes_prioridade_ortopedia):
                chamar_paciente_co()
            elif not any(pacientes_comuns_ortopedia):
                chamar_paciente_po()
            else:
                if not any (pacientes_atendidos_ortopedia):
                    chamar_paciente_po()
                else:
                    if pacientes_atendidos_ortopedia[senha][3] == c:
                        chamar_paciente_po()
                    elif pacientes_atendidos_ortopedia[senha][3] == p:
                        if Ppo[1] > Pco[1]:
                            chamar_paciente_co()
                        elif Ppo[1] < Pco[1]:
                            chamar_paciente_po()
        print('Paciente', nome_paciente, '\nSenha: ', senha)
        if escpecialidade_consulta == 1:
            print('Favor, venha ao consultório 1 para a sua consulta')
            adicionar_lista(em_atendimento_dermatologia)
        elif escpecialidade_consulta == 2:
            print('Favor, venha ao consultório 2 para a sua consulta')
            adicionar_lista_(em_atendimento_endocrinologia)
        else:
            print('Favor, venha ao consultório 3 para a sua consulta')
            adicionar_lista(em_atendimento_ortopedia)
        adicionar_lista(em_atendimento)
        exclusao()
        hora_entrada = int(input('Digite a hora(0 a 23) e os minutos (0 a 59) de entrada do paciente no consultório, sem nenhum ponto, espaço, ou outro caracter entre eles: '))
        
    elif opcao == 3:
        exclusao()
        
    elif opcao == 4:
        consultorio = int(input('Digite o número do consultório: 1. Dermatologia, 2. Endocrinologia , 3. Ortopedia: ')) 
        if consultorio == 1:
            adicionar_lista(pacientes_atendidos_dermatologia)
        elif consultorio == 2:
            adicionar_lista(pacientes_atendidos_endocrinologia)
        else:
            adicionar_lista(pacientes_atendidos_ortopedia)
        excluir = input('Digite a senha: ')
        del em_atendimento[excluir]
        hora_saida = int(input('Digite a hora(0 a 23) e os minutos (0 a 59) de saída do paciente, sem nenhum ponto, espaço, ou outro caracter entre eles: '))
        
    elif opcao == 5:
        print('Pacientes em atendimento: ', em_atendimento)
        print('Pacientes em espera comuns do consultório de dermatoogia: ', pacientes_comuns_dermatologia)
        print('Pacientes em espera prioritários do consultório de dermatoogia: ', pacientes_prioridade_dermatologia)
        print('Pacientes em espera comuns do consultório de endocrinologia: ', pacientes_comuns_endocrinologia)
        print('Pacientes em espera prioritários do consultório de endocrinologia: ', pacientes_prioridade_endocrinologia)
        print('Pacientes em espera comuns do consultório de ortopedia: ', pacientes_comuns_ortopedia)
        print('Pacientes em espera prioritários do consultório de ortopedia: ', pacientes_prioridade_ortopedia)
        
    elif opcao == 6:
        print(pacientes_atendidos_dermatologia, 'Consultório 1, Dermatologia, Drª Silvia Melo')
        print(pacientes_atendidos_endocrinologia, 'Consultório 2, Endocrinologia, Dr Fernando Santos')
        print(pacientes_atendidos_ortopedia, 'Consultório 3, Ortopedia, Drª Maria do Carmo Silva')



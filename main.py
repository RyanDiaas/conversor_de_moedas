import requests #importando lib requests para acessar api
from datetime import datetime #importando lib para pegar o horário em que a conversão foi realizada.

def menu():
    '''Função usada para exibir o 1º menu do programa'''
    print('-' * 20)
    print('1 - Ver cotação;\n2 - Converter valor;\n3 - Sair.')
    print('-' * 20)

def moedas_disponiveis():
    '''Função usada para emitir todas as conversões possíveis no programa'''
    print('-' * 42)
    print('1 - [USD-BRL] - DOLAR PARA REAL\n'
          '2 - [CAD-BRL] - DOLAR CANADENSE PARA REAL\n'
          '3 - [EUR-BRL] - EURO PARA REAL')
    print('-' * 42)

def consulta_api(moeda):
    '''Função responsável por criar acesso e consultar API'''
    try:
        url = f'https://economia.awesomeapi.com.br/last/{moeda}'
        response = requests.get(url)
    except requests.RequestException:
        return None
    else:
        if response.status_code == 200:
            return response.json()
    return None

def cotacao_moeda(moeda):
    '''Função para obter especificamente a cotação e converte para o valor arredondado duas casas'''
    dados = consulta_api(moeda)
    if dados:
        moeda_chave = moeda.replace('-','')
        cotacao = round(float(dados[moeda_chave]['bid']), 2) #cotação arredondada para duas casas decimais e tipo float
        return cotacao
    else:
        return None

def conversao_moeda(moeda, valor):
    '''Função para converter valores'''
    cotacao = cotacao_moeda(moeda)
    if cotacao:
        return cotacao * valor
    else:
        return 'Não foi possível realizar a conversão'


print('--- CONVERSOR DE MOEDAS ---')

log_conversao = list() #Lista usada para armazenar os logs dentro dos cases de conversão.

while True:
    #Aqui começa o "programa principal"
    menu()
    try:
        opcao_inicial = int(input('>>> Digite o número da opção desejada: '))
    except ValueError:
        print('Digite um número inteiro...')
    else:
        match(opcao_inicial):
            case 1:
                moedas_disponiveis()
                try:
                    escolha_moeda = int(input('>>> Digite o número da opção desejada: '))
                except ValueError:
                    print('Erro: Digite um valor inteiro')
                else:
                    match(escolha_moeda):
                        case 1:
                            cotacao_atual = cotacao_moeda('USD-BRL')
                            print(f'\n[R$ 1,00 = {cotacao_atual} USD]\n')
                        case 2:
                            cotacao_atual = cotacao_moeda('CAD-BRL')
                            print(f'\n[R$ 1,00 = {cotacao_atual} CAD]\n')
                        case 3:
                            cotacao_atual = cotacao_moeda('EUR-BRL')
                            print(f'\n[R$ 1,00 = {cotacao_atual} EUR]\n')
                        case _:
                            print('Opção inválida.')
            case 2:
                moedas_disponiveis()
                try:
                    escolha_moeda = int(input('>>> Digite o número da opção desejada: '))
                except ValueError:
                    print('Erro: Digite um valor inteiro')
                else:
                    match(escolha_moeda):
                            case 1:
                                valor = float(input('\n>>> Digite o valor em DOLARES para conversão: '))
                                valor_convertido = conversao_moeda('USD-BRL', valor)
                                #Horário em que é realizado a conversão, serve para a saída.
                                momento_cotacao = datetime.now()
                                momento_formatado = momento_cotacao.strftime("%d/%m/%Y %H:%M")
                                #Saidas do projeto: 1ª adiciona ao final da lista, caso seja chamada e a segunda exibe no terminal
                                log_conversao.append(f'[{momento_formatado}] - {valor} USD = R$ {valor_convertido:.2f}\n')
                                print(f'[{momento_formatado}] - {valor} USD = R$ {valor_convertido:.2f}')

                            case 2:
                                valor = float(input('\n>>> Digite o valor em DOLAR CANADENSE para conversão: '))
                                valor_convertido = conversao_moeda('CAD-BRL', valor)
                                #Horário em que é realizado a conversão, serve para a saída.
                                momento_cotacao = datetime.now()
                                momento_formatado = momento_cotacao.strftime("%d/%m/%Y %H:%M")
                                #Saidas do projeto: 1ª adiciona ao final da lista, caso seja chamada e a segunda exibe no terminal
                                log_conversao.append(f'[{momento_formatado}] - {valor} CAD = R$ {valor_convertido:.2f}\n')
                                print(f'[{momento_formatado}] - CAD-BRL {valor} = R$ {valor_convertido:.2f} ')
                            case 3:
                                valor = float(input('\n>>> Digite o valor em EURO para conversão: '))
                                valor_convertido = conversao_moeda('EUR-BRL', valor)
                                #Horário em que é realizado a conversão, serve para a saída.
                                momento_cotacao = datetime.now()
                                momento_formatado = momento_cotacao.strftime("%d/%m/%Y %H:%M")
                                #Saidas do projeto: 1ª adiciona ao final da lista, caso seja chamada e a segunda exibe no terminal
                                log_conversao.append(f'[{momento_formatado}] - {valor} EUR = R$ {valor_convertido:.2f}\n')
                                print(f'[{momento_formatado}] - EUR {valor} = R$ {valor_convertido:.2f}')
                            case _:
                                print('Opção inválida.')     
            case 3:
                #Inserção de logs da conversão em arquivo de texto
                with open("log_conversao.txt", "a") as arquivo:
                    for i in log_conversao:
                        arquivo.write(i)
                break
            case _:
                print('>>> Opção inválida <<<')


print('Finalizando programa...')
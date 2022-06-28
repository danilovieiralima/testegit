import requests
import json


class CotacaoMoeda:

    def get_cotacao_dolar(self):
        cotacao_dolar = requests.get('https://economia.awesomeapi.com.br/last/USD-BRL')
        cotacao_dolar = cotacao_dolar.json()
        return str(cotacao_dolar['USDBRL']['bid'])

    def get_cotacao_euro(self):
        cotacao_euro = requests.get('https://economia.awesomeapi.com.br/last/EUR-BRL')
        cotacao_euro = cotacao_euro.json()
        return str(cotacao_euro['EURBRL']['bid'])

    def get_cotacao_bitcoin(self):
        cotacao_bitcoin = requests.get('https://economia.awesomeapi.com.br/last/BTC-BRL')
        cotacao_bitcoin = cotacao_bitcoin.json()
        return str(cotacao_bitcoin['BTCBRL']['bid'])


cotacoes = CotacaoMoeda()
while True:
    print('Suas opções são: \n[1] DÓLAR \n[2] EURO \n[3] BITCOIN')
    while True:
        escolher_cotacao = int(input('Digite a opção que você escolheu: '))
        if escolher_cotacao == 1:
            print(f'A cotação do Dólar é US${(cotacoes.get_cotacao_dolar())}')
            break
        elif escolher_cotacao == 2:
            print(f'A cotação do Euro é €{(cotacoes.get_cotacao_euro())}')
            break
        elif escolher_cotacao == 3:
            print(f'A cotação do Bitcoin é  ₿{(cotacoes.get_cotacao_bitcoin())}')
            break
        elif escolher_cotacao > 3 or escolher_cotacao < 1:
            print('Opção Inválida!')
    while True:
        resp = str(input('Quer continuar?[S/N] ')).strip().upper()[0]
        if resp in 'SN':
            break
        print(f'Erro!Digite apenas S ou N!')
    if resp == 'N':
        print('FIM DO PROGRAMA')
        break

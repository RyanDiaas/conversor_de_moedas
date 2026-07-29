# Conversor de Moedas

Projeto desenvolvido em Python com intuito de praticar consumo de APIs REST utilizando a biblioteca `requests`. O programa permite consultar a cotação atual de moedas e realizar conversões para Real (BRL) através da API AwesomeAPI.

---

## Funcionalidades

- Consultar cotação do Dólar (USD)
- Consultar cotação do Dólar Canadense (CAD)
- Consultar cotação do Euro (EUR)
- Converter valores para Real (BRL)
- Tratamento de erros de conexão
- Menu interativo no terminal
- Histórico de conversões

---

## Tecnologias utilizadas

- Python 3
- Requests
- AwesomeAPI

---

## Instalação

Clone o repositório:

```bash
git clone https://github.com/RyanDiaas/conversor_de_moedas.git
```

Entre na pasta:

```bash
cd conversor-moedas
```

Instale as dependências:

```bash
pip install requirements.txt
```

Execute o programa:

```bash
python main.py 

ou 

python3 main.py
```

---

## Exemplo de utilização terminal

```
--- COTAÇÃO DE MOEDAS ---

1 - Ver cotação
2 - Converter valor
3 - Sair

>>> Digite a opção desejada: 1

1 - USD-BRL
2 - CAD-BRL
3 - EUR-BRL

>>> Digite a moeda: 1

Cotação atual:
1 USD = R$ 5,43
```
---
## Exemplo de histórico de conversão
```
[28/07/2026 22:05] - 550.0 USD = R$ 2827.0
[28/07/2026 22:06] - 893.3 USD = R$ 4591.562
[28/07/2026 22:08] - 1621.0 EUR = R$ 9482.85
[28/07/2026 22:08] - 1512.0 CAD = R$ 5503.68
[28/07/2026 22:08] - 2030.0 CAD = R$ 7389.20
[28/07/2026 22:08] - 42.09 EUR = R$ 246.23
```
---

## API utilizada

Este projeto utiliza a API pública da AwesomeAPI para obter as cotações em tempo real.

https://docs.awesomeapi.com.br/api-de-moedas

---

## Conceitos praticados

- Funções
- Organização de código
- Consumo de APIs REST
- Requisições HTTP
- Manipulação de JSON
- Manipulação de arquivos de texto
- Tratamento de exceções
- Estruturas condicionais
- Estruturas de repetição

---

## Próximas melhorias

-  Suporte a mais moedas
-  Interface gráfica
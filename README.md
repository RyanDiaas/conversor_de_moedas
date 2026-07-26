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
pip install requests
```

Execute o programa:

```bash
python main.py
```

---

## Exemplo de utilização

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
- Tratamento de exceções
- Estruturas condicionais
- Estruturas de repetição

---

## Próximas melhorias

-  Suporte a mais moedas
-  Interface gráfica
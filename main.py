"""
Este script contém uma função que recebe um nome com as palavras
invertidas, reverte a ordem das palavras e restaura as palavras
para a forma correta, com a primeira letra maiúscula.

A função `inverter_nome(nome_invertido)` é a principal do script.
Ela realiza as seguintes operações:
1. Divide a string do nome invertido em palavras.
2. Inverte a ordem das palavras.
3. Reverte cada palavra individualmente e capitaliza a primeira
letra de cada uma.

O script também inclui um bloco de teste que demonstra o uso da
função, invertendo o nome
"Trelov Razec Odracir"
para
"Ricardo Cezar Volert".

Para executar o código, basta rodar o script diretamente, que o
nome processado será exibido no terminal.

Autor: Ricardo Cezar Volert
Data: 11-dez-2024
"""


def inverter_nome(nome_invertido: str) -> str:
    """
    Função que recebe um nome invertido, reverte a ordem das palavras
    e restaura as palavras para a forma correta com a primeira letra maiúscula.

    Parâmetros:
        nome_invertido (str): O nome com as palavras invertidas.

    Retorna:
        str: O nome original, com a ordem correta das palavras e com a
        primeira letra maiúscula.
    """
    if not nome_invertido:
        raise ValueError("O nome fornecido não pode ser vazio.")

    # Divide o nome em palavras e inverte a ordem delas
    palavras = nome_invertido.split()
    palavras_invertidas = palavras[::-1]

    # Inverte cada palavra individualmente e capitaliza a primeira letra
    palavras_capitalizadas = [
        palavra[::-1].capitalize() for palavra in palavras_invertidas
    ]
    nome_original = " ".join(palavras_capitalizadas)

    return nome_original


# Testando o algoritmo com exemplo
if __name__ == "__main__":
    NOME_INVERTIDO = "Trelov Razec Odracir"
    NOME_RESULTADO = inverter_nome(NOME_INVERTIDO)
    print(
        "Meu nome é:", NOME_RESULTADO
    )

# End of file: main.py

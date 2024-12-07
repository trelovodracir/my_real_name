def inverter_nome(nome_invertido: str) -> str:
    """
    Função que recebe um nome invertido, reverte a ordem das palavras
    e restaura as palavras para a forma correta com a primeira letra maiúscula.

    Parâmetros:
        nome_invertido (str): O nome com as palavras invertidas.

    Retorna:
        str: O nome original, com a ordem correta das palavras e com a primeira letra maiúscula.
    """
    if not nome_invertido:
        raise ValueError("O nome fornecido não pode ser vazio.")

    # Divide o nome em palavras e inverte a ordem delas
    palavras = nome_invertido.split()
    palavras_invertidas = palavras[::-1]
    
    # Inverte cada palavra individualmente e capitaliza a primeira letra
    nome_original = " ".join([palavra[::-1].capitalize() for palavra in palavras_invertidas])
    
    return nome_original


# Testando o algoritmo com exemplo
if __name__ == "__main__":
    nome_invertido = "Trelov Razec Odracir"
    nome_original = inverter_nome(nome_invertido)
    print("Meu nome é:", nome_original)

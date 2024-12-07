import pytest
from main import inverter_nome  # Importa a função a ser testada

@pytest.mark.parametrize(
    "entrada, esperado",
    [
        # Testa um nome completo invertido
        ("Trelov Razec Odracir", "Ricardo Cezar Volert"),
        # Testa um nome com uma única palavra
        ("Odracir", "Ricardo"),
        # Testa o comportamento com entrada vazia (exceção esperada)
        ("", ValueError),
        # Testa um nome com espaços extras entre as palavras
        (" Trelov   Razec   Odracir ", "Ricardo Cezar Volert"),
        # Testa casos especiais com caracteres especiais ou números
        ("321#@ Zeca", "Acez @#123"),
    ],
)
def test_inverter_nome(entrada, esperado):
    if isinstance(esperado, type) and issubclass(esperado, Exception):
        # Verifica se uma exceção é levantada para entradas inválidas
        with pytest.raises(esperado):
            inverter_nome(entrada)
    else:
        # Verifica o resultado esperado para entradas válidas
        assert inverter_nome(entrada) == esperado

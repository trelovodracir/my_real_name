import unittest
from main import inverter_nome  # Importa a função a ser testada

class TestInverterNome(unittest.TestCase):
    def test_nome_completo(self):
        """Testa um nome completo invertido."""
        self.assertEqual(
            inverter_nome("Trelov Razec Odracir"),
            "Ricardo Cezar Volert"
        )

    def test_nome_simples(self):
        """Testa um nome com uma única palavra."""
        self.assertEqual(inverter_nome("Odracir"), "Ricardo")

    def test_entrada_vazia(self):
        """Testa o comportamento com entrada vazia."""
        with self.assertRaises(ValueError):
            inverter_nome("")

    def test_nome_com_espacos_extras(self):
        """Testa um nome com espaços extras entre as palavras."""
        self.assertEqual(
            inverter_nome(" Trelov   Razec   Odracir "),
            "Ricardo Cezar Volert"
        )

    def test_nome_com_caracteres_especiais(self):
        """Testa casos especiais com nome com caracteres especiais ou números"""
        self.assertEqual(inverter_nome("321#@ Zeca"), "Acez @#123")


if __name__ == "__main__":
    unittest.main()

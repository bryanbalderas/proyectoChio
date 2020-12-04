from unittest import TestCase
from unittest.mock import patch, Mock
from PokeApi import PokeApi

class TestOperaciones(TestCase):

    @patch("PokeApi.PokeApi.write_pokemon_list", autospec = True)
    def test_write_pokemon_list(self, MockWrite):
        MockWrite.return_value = 151
        poke = PokeApi()
        esperado = 151
        real = poke.write_pokemon_list("oli")
        self.assertEqual(esperado, real)

    @patch("PokeApi.PokeApi.write_move_list", autospec = True)
    def test_write_move_list(self, MockMove):
        MockMove.return_value = """1 bailar el tucanazo,
                                2 oler a limón,
                                3 comer helado,
                                4 fumar un porro
                                """

        esperado = """1 bailar el tucanazo,
                                2 oler a limón,
                                3 comer helado,
                                4 fumar un porro
                                """
        poke = PokeApi()
        real = poke.write_move_list(poke)
        self.assertEqual(esperado, real)

    @patch("PokeApi.PokeApi.create_pokemon", autospec = True)
    def test_create_pokemon(self, MockPoke):
        MockPoke.return_value = {"id_pokedex": "lalala",
                                "especie": "cholo",
                                "tipo": "agresivo"
                                }

        esperado = {"id_pokedex": "lalala",
                                "especie": "cholo",
                                "tipo": "agresivo"
                                }
        poke = PokeApi()
        real = poke.create_pokemon(1, "jombalash")
        self.assertEqual(esperado, real)
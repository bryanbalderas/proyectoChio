from PokeApi import PokeApi
from unittest import TestCase
from unittest.mock import patch, Mock
from baseConection import *
from entrenador import entrenadorbase
import unittest

class TestOperaciones(unittest.TestCase):
    @patch("baseConection.DataBaseInteract.insert_user", autospec=True)
    def test_insert_user(self, MockUser):
        MockUser.return_value = True
        esperado = True
        base = DataBaseInteract()
        trainer = entrenadorbase()
        real = base.insert_user(trainer)
        return self.assertEqual(esperado, real)

    @patch("baseConection.DataBaseInteract.validate_user", autospec=True)
    def test_validate_user(self, MockValidate):
        MockValidate.return_value = [100]
        esperado = [100]
        base = DataBaseInteract()
        trainer = entrenadorbase()
        real = base.validate_user(trainer)
        self.assertEqual(esperado, real)

    @patch("baseConection.DataBaseInteract.inserta_poke", autospec=True)
    def test_inserta_poke(self, MockPoke):  
        MockPoke.return_value = {"id_equipo":1, "id_pokedex": 69,
                                "nombre": "tony",
                                "tipo":"loco", "especie": "inexistente",
                                "move_one": "bailar breakdance", "move_two": "hablar con su cruch",
                                "move_three": "viaje astral", "move_four": "manquear en lol" 
                                }

        esperado = {"id_equipo":1, "id_pokedex": 69,
                                "nombre": "tony",
                                "tipo":"loco", "especie": "inexistente",
                                "move_one": "bailar breakdance", "move_two": "hablar con su cruch",
                                "move_three": "viaje astral", "move_four": "manquear en lol" 
                                }
        base = DataBaseInteract()
        poke =  pokebase
        real = base.inserta_poke(poke)
        self.assertEqual(esperado, real)

    @patch("baseConection.DataBaseInteract.delete_poke", autospec=True)
    def test_consul_teams_by_trainer(self, MockDelete):
        MockDelete.return_value = "Se borraron los pokemon correctamente"#checar si regreso algo o nah xd
        esperado = "Se borraron los pokemon correctamente"
        base = DataBaseInteract()
        real = base.delete_poke()
        self.assertEqual(esperado, real)

    @patch("baseConection.DataBaseInteract.consul_team")
    def test_consul_team(self, MockConsulta):
        MockConsulta.return_value = [{
                        "nombre_equipo": "Asesinos",
                        "pokedex_id": 90,
                        "nombre": "Paquito",
                        "tipo": "zombie",
                        "especie": "Arseus",
                        "move_one": "volar",
                        "move_two": "nadar",
                        "move_three": "estudiar",
                        "move_four": "reprobar"
                        }]
        esperado = [{
                        "nombre_equipo": "Asesinos",
                        "pokedex_id": 90,
                        "nombre": "Paquito",
                        "tipo": "zombie",
                        "especie": "Arseus",
                        "move_one": "volar",
                        "move_two": "nadar",
                        "move_three": "estudiar",
                        "move_four": "reprobar"
                        }]
        base = DataBaseInteract()                        
        real = base.consul_team(80)
        self.assertEqual(esperado, real)

    @patch("baseConection.DataBaseInteract.consul_teams_by_trainer", autospec=True)
    def test_consul_teams_by_trainer_dos(self, MockConsul):
        MockConsul.return_value = [{"id_equipo": 1, "team_name": "Obscuros", 
                                "id_equipo": 2, "team_name": "1ra_gen",
                                "id_equipo": 3, "team_name": "hierba",
                                "id_equipo": 4, "team_name": "agua",
                                "id_equipo": 5, "team_name": "Legendarios",
                                "id_equipo": 6, "team_name": "Electricos",
                                "id_equipo": 7, "team_name": "random",
                                "id_equipo": 8, "team_name": "xd",
                                "id_equipo": 9, "team_name": "OP",
                                }]

        esperado = [{"id_equipo": 1, "team_name": "Obscuros", 
                                "id_equipo": 2, "team_name": "1ra_gen",
                                "id_equipo": 3, "team_name": "hierba",
                                "id_equipo": 4, "team_name": "agua",
                                "id_equipo": 5, "team_name": "Legendarios",
                                "id_equipo": 6, "team_name": "Electricos",
                                "id_equipo": 7, "team_name": "random",
                                "id_equipo": 8, "team_name": "xd",
                                "id_equipo": 9, "team_name": "OP",
                                }]

        base = DataBaseInteract()
        trainer = entrenadorbase()
        real = base.consul_teams_by_trainer(trainer)
        self.assertEqual(esperado, real)
    
    @patch("baseConection.DataBaseInteract.insert_team", autospec=True)
    def test_insert_team(self, MockTeam):
        MockTeam.return_value = True
        esperado = True
        base = DataBaseInteract()
        team = teambase()
        real = base.insert_team(team, 1)
        self.assertEqual(esperado, real)

    @patch("baseConection.DataBaseInteract.insert_pokemon", autospec=True)
    def test_insert_pokemon(self, MockPokemon):
        MockPokemon.return_value = False
        esperado = False
        pokemon = pokebase()
        base = DataBaseInteract()
        real = base.insert_pokemon(pokemon, 2)
        self.assertEqual(esperado, real)

    @patch("baseConection.DataBaseInteract.eliminarEquipo", autospec=True)
    def test_eliminarEquipo(self, MockDelTeam):
        MockDelTeam.return_value = False
        esperado = False
        base = DataBaseInteract()
        real = base.eliminarEquipo("Testing!", 4)
        self.assertEqual(esperado, real)

    #Mock para copiar y pegar when hayan más xd  
    # @patch("baseConection.DataBaseInteract.*****", autospec=True)
    # def test_consul_teams_by_trainer(self, MockAlgo):
    #     MockAlgo.return_value = []#checar si regreso algo o nah xd
    #     esperado = []
    #     base = DataBaseInteract()
    #     real = base.("oli")
    #     self.assertEqual(esperado, real)
    
if __name__ == "__main__":
    unittest.main()
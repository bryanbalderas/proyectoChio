from unittest import mock
import unittest
from unittest.mock import patch,MagicMock
from domainInsercion import insertarDatos
from pokemon import pokebase
from entrenador import entrenadorbase


class testMockDomain(unittest.TestCase):
    
    
    
    @patch('domainInsercion.insertarDatos.insert_entrenador_data',return_value=True)
    def test_funcionaCorrecto(self,mock_get):
     llamar=insertarDatos()
    
    
     read_data=entrenadorbase()
     read_data.nombre="juanitoperez"
     read_data.password="123"

     resultado_esperado=True
     resultado_actual=llamar.insert_entrenador_data("mock")
     
     assert resultado_esperado==resultado_actual
        
    @patch('domainInsercion.insertarDatos.eliminarEquipo',return_value="Se borraron los pokemon correctamente")
    def test_eliminar_equipo(self,mock_get):
     llamar=insertarDatos()
    
     resultado_esperado="Se borraron los pokemon correctamente"
     resultado_actual=llamar.eliminarEquipo("mock",1)
     
     assert resultado_esperado==resultado_actual
        
        
if __name__ == "__main__":
    unittest.main()
import unittest
from unittest.mock import patch
from io import StringIO
from Unit_conversor import convert_weight, convert_temperature

# Python


class TestDirectConversionFunctions(unittest.TestCase):
    @patch('builtins.input', side_effect=['9', '1', '2', '1', 'n'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_weight_invalid_origin(self, mock_stdout, mock_input):
        convert_weight()
        output = mock_stdout.getvalue()
        self.assertIn("¡UNIDAD DE ORIGEN NO VALIDA!", output)
        self.assertIn("CONVERSIÓN DE PESO", output)

    @patch('builtins.input', side_effect=['1', '9', '2', '1', 'n'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_weight_invalid_destino(self, mock_stdout, mock_input):
        convert_weight()
        output = mock_stdout.getvalue()
        self.assertIn("¡UNIDAD DE DESTINO NO VALIDA!", output)

    @patch('builtins.input', side_effect=['1', '2', 'abc', '1', '2', '2', 'n'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_weight_invalid_value(self, mock_stdout, mock_input):
        # Should raise ValueError, but your code does not handle it, so this will error.
        with self.assertRaises(ValueError):
            convert_weight()

    @patch('builtins.input', side_effect=['1', '2', '10', 's', '1', '2', '10', 'n'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_weight_repeat_conversion(self, mock_stdout, mock_input):
        convert_weight()
        output = mock_stdout.getvalue()
        self.assertGreater(output.count("Resultado: 10000.0 gramos"), 1)

    @patch('builtins.input', side_effect=['1', '2', '10', 'n'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_weight_conversion_once(self, mock_stdout, mock_input):
        convert_weight()
        output = mock_stdout.getvalue()
        self.assertIn("Resultado: 10000.0 gramos", output)
        self.assertIn("Conversión finalizada.", output)

    @patch('builtins.input', side_effect=['1', '9', '1', '2', '10', 'n'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_temperature_invalid_destino(self, mock_stdout, mock_input):
        convert_temperature()
        output = mock_stdout.getvalue()
        self.assertIn("El valor seleccionado no existe dentro de las opciones", output)

if __name__ == '__main__':
    unittest.main()
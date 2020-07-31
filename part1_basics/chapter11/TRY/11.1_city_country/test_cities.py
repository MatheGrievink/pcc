import unittest
from city_functions import city_country

class CitiesTestCase(unittest.TestCase):
    """Tests for 'city_functions.py'."""

    def test_cities_countries(self):
        """Do combinations like 'santiago, chile' work?"""
        formatted_message = city_country('santiago', 'chile')
        self.assertEqual(formatted_message, "Santiago, Chile.")


if __name__ == '__main__':
    unittest.main()
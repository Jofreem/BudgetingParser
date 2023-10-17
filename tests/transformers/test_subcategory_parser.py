from unittest import TestCase

from src.transformers.subcategory_parser import SubcategoryParser

class TestSubcategoryParser(TestCase):
    def setUp(self):
        self.subcategory_parser = SubcategoryParser()

    def test_sports(self):
        self.assertEqual(self.subcategory_parser.transform("K2 Skates"), "Sports")
        self.assertEqual(self.subcategory_parser.transform("REI 3920"), "Sports")
        self.assertEqual(self.subcategory_parser.transform("REI 912332"), "Sports")

    def test_moved_payments(self):
        self.assertEqual(self.subcategory_parser.transform("Capital One Online Pymt"), "Moved Money")
        self.assertEqual(self.subcategory_parser.transform("CAPITAL ONE MOBILE PYMT"), "Moved Money")

    def test_food(self):
        self.assertEqual(self.subcategory_parser.transform("Chick-Fil-A"), "Food")
        self.assertEqual(self.subcategory_parser.transform("This is a test Restaurant"), "Food")
        self.assertEqual(self.subcategory_parser.transform("Some Restaurant 12345"), "Food")

    def test_health(self):
        self.assertEqual(self.subcategory_parser.transform("SP Geologie"), "Health")
        self.assertEqual(self.subcategory_parser.transform("Neutrogenia"), "Health")
    
    def test_other(self):
        self.assertEqual(self.subcategory_parser.transform("Some other category"), "OTHER")
        self.assertEqual(self.subcategory_parser.transform("Some junk", "Dining"), "Dining")

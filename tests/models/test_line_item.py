from typing import Final
from unittest import TestCase
from unittest.mock import patch, Mock
from datetime import datetime
from decimal import Decimal
from src.models.line_item import LineItem
from src.transformers.subcategory_parser import SubcategoryParser

TEST_TRANSACTION_DATE: Final[datetime] = datetime(2023, 1, 12)
TEST_EXPENSE_DESCRIPTION: Final[str] = "Sample Expense"
TEST_CATEGORY: Final[str] = "Sample Category"
TEST_SOURCE: Final[str] = "Sample Source"
TEST_RAW_SUBCATEGORY: Final[str] = "Sample Subcategory"
TEST_DEBIT_AMOUNT: Final[Decimal] = Decimal("100.23")
TEST_CREDIT_AMOUNT: Final[Decimal] = Decimal("56.78")

class TestLineItem(TestCase):
    def setUp(self):
        self.valid_line_item = LineItem(
            transaction_date=TEST_TRANSACTION_DATE,
            expense_description=TEST_EXPENSE_DESCRIPTION,
            category=TEST_CATEGORY,
            source=TEST_SOURCE,
            raw_subcategory=TEST_RAW_SUBCATEGORY,
            debit_amount=TEST_DEBIT_AMOUNT
        )

    def test_init(self):
        self.assertEqual(self.valid_line_item.transaction_date, TEST_TRANSACTION_DATE)
        self.assertEqual(self.valid_line_item.expense_description, TEST_EXPENSE_DESCRIPTION)
        self.assertEqual(self.valid_line_item.category, TEST_CATEGORY)
        self.assertEqual(self.valid_line_item.source, TEST_SOURCE)
        self.assertEqual(self.valid_line_item.raw_subcategory, TEST_RAW_SUBCATEGORY)
        self.assertEqual(self.valid_line_item.debit_amount, TEST_DEBIT_AMOUNT)

    def test_failure(self):
        # Test invalid initialization (both debit and credit amounts provided)
        with self.assertRaises(ValueError):
            LineItem(
                transaction_date=TEST_TRANSACTION_DATE,
                expense_description=TEST_EXPENSE_DESCRIPTION,
                category=TEST_CATEGORY,
                source=TEST_SOURCE,
                raw_subcategory=TEST_RAW_SUBCATEGORY,
                debit_amount=TEST_DEBIT_AMOUNT,
                credit_amount=TEST_CREDIT_AMOUNT
            )

    @patch.object(SubcategoryParser, 'transform')
    def test_parse_subcategory(self, MockSubcategoryParser):
        # Mocks
        MockSubcategoryParser.return_value = "Parsed Subcategory"

        # Setup / Execute
        line_item = self.valid_line_item
        line_item.parse_subcategory()

        # Validate
        self.assertEqual(line_item.true_subcategory, "Parsed Subcategory")

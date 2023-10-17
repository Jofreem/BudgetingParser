from dataclasses import dataclass
from datetime import datetime
from decimal import Decimal
from typing import Optional

from src.transformers.subcategory_parser import SubcategoryParser

@dataclass
class LineItem:
    """
    Object that holds the attributes and data required for an Expense
    """

    transaction_date: datetime
    expense_description: str
    category: str
    source: str
    raw_subcategory: str
    debit_amount: Optional[Decimal] = None
    credit_amount: Optional[Decimal] = None
    true_subcategory: Optional[str] = None

    def __post_init__(self):
        if self.debit_amount is None and self.credit_amount is None:
            raise ValueError("Either 'Debit' or 'Credit' must be set, but not both.")
        elif self.debit_amount is not None and self.credit_amount is not None:
            raise ValueError("Both 'Debit' and 'Credit' cannot be set at the same time.")

    def parse_subcategory(self) -> None:
        self.true_subcategory = SubcategoryParser().transform(self.raw_subcategory, self.expense_description)


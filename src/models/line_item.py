from dataclasses import dataclass
from datetime import datetime
from decimal import Decimal
from typing import Optional

@dataclass
class LineItem:
    """
    Object that holds the attributes and data required for an Expense
    """

    date: datetime
    expense: str
    amount: Decimal
    category: str
    source: str
    raw_subcategory: str
    true_subcategory: Optional[str] = None

    def parse_subcategory(self) -> None:
        pass
        #self.true_subcategory = SubcategoryParser(self.subcategory)


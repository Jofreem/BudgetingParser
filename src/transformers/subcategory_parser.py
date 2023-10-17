import re

class SubcategoryParser:
    """
    TODO: Add in fuzzy string comparison (e.g. thefuzz package)
    """
    

    def __init__(self):
        self.knownLookups = {
            r"k2 skates": "Sports",
            r"capital one online pymt": "Moved Money", # Somehow flag this as a special type
            r"jersey mikes .*": "Food",
            r".* clerys .*": "Alcohol",
            r"dollar tree": "Misc",
            r"chick-fil-a": "Food",
            r".*restaurant.*": "Food",
            r"sp geologie": "Health",
            r"neutrogenia": "Health",
            r"rei.*": "Sports",
            r"capital one mobile pymt": "Moved Money", # For me this is always a check
        }

    def transform(self, raw_subcategory: str, expense_description: str = "OTHER") -> str:
        """
        Transforms the bank issues category into a human readable category
        Future work: Implement regex searching 
        (e.g. "* RESTAURANT" -> "Food")
        """
        raw_subcategory = raw_subcategory.lower()
        for pattern, category in self.knownLookups.items():
            if re.match(pattern, raw_subcategory):
                return category
        return expense_description
    

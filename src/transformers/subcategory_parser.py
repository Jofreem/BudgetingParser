import re

class SubcategoryParser:
    """
    TODO: Add in fuzzy string comparison (e.g. thefuzz package)
    """
    

    def __init__(self):
        # TODO: Make these case insensitive
        self.knownLookups = {
            r"K2 Skates": "Sports",
            r"Capital One Online Pymt": "Moved Money", # Somehow flag this as a special type
            r"Jersey Mikes .*": "Food",
            r".* Clerys .*": "Alcohol",
            r"Dollar Tree": "Misc",
            r"Chick-Fil-A": "Food",
            r".*Restaurant.*": "Food",
            r"SP Geologie": "Health",
            r"Neutrogenia": "Health",
            r"REI.*": "Sports",
            r"CAPITAL ONE MOBILE PYMT": "Moved Money", # For me this is always a check
        }

    def transform(self, raw_subcategory: str) -> str:
        """
        Transforms the bank issues category into a human readable category
        Future work: Implement regex searching 
        (e.g. "* RESTAURANT" -> "Food")
        """
        
        for pattern, category in self.knownLookups.items():
            if re.match(pattern, raw_subcategory):
                return category
        return "OTHER" # TODO: Switch this to be the default Category
    

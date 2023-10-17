# BudgetingParser
Parser to populate a google doc from Capital One exported financial data

## Usage

Start by creating a google_credentials.json file. This can be done by following the instructions on the google API website.


```
myenv\Scripts\activate
pip install -r .\requirements.txt
python .\main.py test_data.csv
```

## Tests
```
python -m unittest discover -s tests/transformers tests/models -p "test_*.py"
```
Runs all of the current unittests
import re
from validator import validator

print("""
----------------------------------------
|                                      |
|     Welcome to the CPF Validator     |
|                                      |
----------------------------------------
""")
print("Enter a CPF. Ex: 000.000.000-00")
cpf = input()

valid = re.search(r"[0-9]{3}\.?[0-9]{3}\.?[0-9]{3}\-?[0-9]{2}", cpf)

if not valid and len(cpf) not in (11, 15):
    raise TypeError("Invalid CPF Format!")

validator(cpf)

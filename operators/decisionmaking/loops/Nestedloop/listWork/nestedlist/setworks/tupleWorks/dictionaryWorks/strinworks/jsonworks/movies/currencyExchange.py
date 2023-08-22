rates={
    "USD": 1,
    "AED": 3.6725,
    "AFN": 86.0330,
    "ALL": 97.5499,
    "AMD": 386.9256,
    "ANG": 1.7900,
    "AOA": 824.0658,
    "ARS": 254.7465,
    "AUD": 1.5099,
    "AWG": 1.7900,
    "AZN": 1.6979,
    "BAM":1.7974,
    "INR":82.0914
  }
amount=int(input("enter a amount:"))
fromcurrencycode=input("enter a source code")
tocurrencycode=input("enter a destination currency code")
#equation=(amouny/fromcurrencycode_rate)*tocurrencycode_rate
fromrate= rates.get(fromcurrencycode)
torate=rates.get(tocurrencycode)
result=(amount/fromrate)*torate
print(result)
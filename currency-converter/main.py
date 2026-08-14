import requests
from_currency = input("From currency: ").upper()
to_currency = input("To currency: ").upper()
amount = float(input("Enter amount: "))
url = f"https://open.er-api.com/v6/latest/{from_currency}"
response = requests.get(url)
if response.status_code == 200:
    data = response.json()
    rate = data["rates"][to_currency]
    result = amount * rate
    print(f"{amount} {from_currency} = {result:.2f} {to_currency}")
else:
    print("Error:", response.status_code)
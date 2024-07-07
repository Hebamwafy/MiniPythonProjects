import requests

initial_currency = input("Enter the initial currency (e.g., USD): ").upper()
target_currency = input("Enter the target currency (e.g., EUR): ").upper()

while True:
    try:
        amount = float(input("Enter the amount: "))
        if amount <= 0:
            print("The amount must be more than 0.")
            continue
    except ValueError:
        print("The amount must be a numeric value!")
        continue
    break

url = f"https://api.apilayer.com/fixer/convert?to={target_currency}&from={initial_currency}&amount={amount}"

headers = {
  "apikey": "KCvCgChOu3vM66zztGQnMYUeHHM4NTuf"
}

response = requests.get(url, headers=headers)

if response.status_code != 200:
    print("Sorry, there was a problem, please try again later.")
    quit()

result = response.json()

if 'result' in result:
    conversion_result = result['result']
    print(f'{amount} {initial_currency} = {conversion_result} {target_currency}')
else:
    print("Error in the response from the API.")
